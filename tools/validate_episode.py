#!/usr/bin/env python3
"""Completeness validator for a documentary episode folder.

This checks structure and metadata only. It cannot establish factual truth,
licence validity, visual quality, or YouTube policy compliance.
"""
import json, pathlib, re, sys

REQUIRED_TOP = ["title", "working_status", "format", "target_runtime_minutes", "research_cutoff", "editorial_promise"]
REQUIRED_SCENE = ["scene_id", "narration_anchor", "visual_description", "motion", "asset_type", "rights_status", "source_ids"]
ALLOWED_RIGHTS = {"verified_commercial", "public_domain_verified", "permission_granted", "hold", "not_applicable"}
ERRORS, WARNINGS = [], []

def load(path, label):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"{label}: cannot parse JSON ({exc})")
        return None

def main(folder):
    root = pathlib.Path(folder)
    if not root.is_dir():
        print(f"ERROR: folder not found: {root}")
        return 2
    ep = load(root / "episode.json", "episode.json")
    scenes = load(root / "scenes.json", "scenes.json")
    sources = load(root / "sources.json", "sources.json")
    if ep is not None:
        for key in REQUIRED_TOP:
            if not ep.get(key): ERRORS.append(f"episode.json: missing {key}")
        if ep.get("working_status") == "published":
            WARNINGS.append("Status says published; verify the final approval record exists.")
    if not isinstance(scenes, list):
        if scenes is not None: ERRORS.append("scenes.json must be a JSON array")
        scenes = []
    if not isinstance(sources, list):
        if sources is not None: ERRORS.append("sources.json must be a JSON array")
        sources = []
    source_ids = {s.get("source_id") for s in sources if isinstance(s, dict)}
    seen = set()
    for i, scene in enumerate(scenes, 1):
        if not isinstance(scene, dict):
            ERRORS.append(f"scene {i}: must be an object"); continue
        for key in REQUIRED_SCENE:
            if scene.get(key) in (None, "", []):
                ERRORS.append(f"scene {i}: missing {key}")
        sid = scene.get("scene_id")
        if sid in seen: ERRORS.append(f"duplicate scene_id: {sid}")
        seen.add(sid)
        if scene.get("motion") and len(str(scene["motion"])) < 25:
            WARNINGS.append(f"{sid}: motion description may be too vague")
        status = scene.get("rights_status")
        if status not in ALLOWED_RIGHTS:
            ERRORS.append(f"{sid}: invalid rights_status {status!r}")
        elif status not in {"verified_commercial", "public_domain_verified", "permission_granted", "not_applicable"}:
            WARNINGS.append(f"{sid}: rights are on HOLD; episode cannot be published")
        for source_id in scene.get("source_ids", []):
            if source_id not in source_ids:
                ERRORS.append(f"{sid}: source_id {source_id!r} missing from sources.json")
        if scene.get("asset_type") in {"archival_video", "archival_image", "music", "sound_effect", "font", "map"} and status not in {"verified_commercial", "public_domain_verified", "permission_granted"}:
            WARNINGS.append(f"{sid}: third-party asset lacks verified rights; publication gate remains closed")
    for i, src in enumerate(sources, 1):
        if not isinstance(src, dict): ERRORS.append(f"source {i}: must be an object"); continue
        for key in ("source_id", "title", "publisher", "url", "supports"):
            if not src.get(key): ERRORS.append(f"source {i}: missing {key}")
    narration = root / "narration.md"
    if not narration.exists() or len(narration.read_text(encoding="utf-8").strip()) < 500:
        ERRORS.append("narration.md missing or too short (<500 characters)")
    if not (root / "POLICY_REVIEW.md").exists():
        WARNINGS.append("POLICY_REVIEW.md not found; complete the mandatory publication gate.")
    print(f"Episode: {root}")
    print(f"Scenes: {len(scenes)} | Sources: {len(sources)}")
    for item in ERRORS: print("ERROR:", item)
    for item in WARNINGS: print("WARNING:", item)
    print(f"RESULT: {'FAIL' if ERRORS else 'STRUCTURE PASS — MANUAL REVIEW STILL REQUIRED'}")
    return 1 if ERRORS else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "episodes"))
