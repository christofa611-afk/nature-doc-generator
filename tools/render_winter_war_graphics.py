#!/usr/bin/env python3
"""Render original, clearly schematic animated editorial graphics for the Winter War.
Requires ffmpeg on PATH. Uses only Python standard library and SVG frames.
These are explanatory graphics, not geographically precise maps or archival footage.
"""
import math, pathlib, subprocess, shutil

OUT = pathlib.Path("episodes/winter-war/generated")
FRAMES = OUT / "frames"
W, H, FPS = 1280, 720, 25
BG = "#101b25"
INK = "#edf2f4"
MUTED = "#a9b7c3"
RED = "#c95d4d"
BLUE = "#6fa7c8"
GOLD = "#d5b16b"
GREEN = "#84a98c"

def esc(s):
    return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def svg(title, subtitle, body, progress, footer):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="1280" height="720" fill="{BG}"/>
<path d="M0 112 H1280" stroke="#354656" stroke-width="2"/>
<text x="72" y="64" fill="{INK}" font-family="DejaVu Sans" font-size="31" font-weight="bold">{esc(title)}</text>
<text x="74" y="94" fill="{MUTED}" font-family="DejaVu Sans" font-size="16">{esc(subtitle)}</text>
{body}
<rect x="72" y="650" width="1136" height="5" rx="2" fill="#354656"/>
<rect x="72" y="650" width="{1136*progress:.1f}" height="5" rx="2" fill="{GOLD}"/>
<text x="72" y="687" fill="{MUTED}" font-family="DejaVu Sans" font-size="15">{esc(footer)}</text>
</svg>'''

def text(x,y,s,size=24,color=INK,weight="normal",anchor="start"):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="DejaVu Sans" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{esc(s)}</text>'

def line(x1,y1,x2,y2,color=INK,width=3,dash=""):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>'

def circle(x,y,r,color,label=None):
    s=f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'
    if label: s+=text(x,y+6,label,17,BG,"bold","middle")
    return s

def render(name, title, subtitle, build_body, footer, seconds=12):
    d=FRAMES/name
    if d.exists(): shutil.rmtree(d)
    d.mkdir(parents=True,exist_ok=True)
    total=FPS*seconds
    for i in range(total):
        p=i/(total-1)
        body=build_body(p)
        data=svg(title,subtitle,body,p,footer)
        (d/f"{i:04d}.svg").write_text(data,encoding="utf-8")
    target=OUT/f"{name}.mp4"
    cmd=["ffmpeg","-y","-loglevel","error","-framerate",str(FPS),"-i",str(d/"%04d.svg"),"-c:v","libx264","-pix_fmt","yuv420p","-movflags","+faststart",str(target)]
    subprocess.run(cmd,check=True)
    shutil.rmtree(d)
    print(f"Rendered {target}")

def theatre(p):
    # Schematic operational model, intentionally not a real map.
    parts=[]
    parts.append('<rect x="110" y="160" width="1060" height="420" rx="24" fill="#172a36" stroke="#496071" stroke-width="2"/>')
    parts.append('<path d="M170 360 C330 330 430 390 570 350 S850 320 1100 370" fill="none" stroke="#d6c28a" stroke-width="14" stroke-linecap="round"/>')
    parts.append(text(620,315,"NARROW ROAD / LINE OF COMMUNICATION",18,GOLD,"bold","middle"))
    parts.append(text(170,205,"FOREST",17,GREEN,"bold"))
    parts.append(text(1050,540,"FOREST",17,GREEN,"bold","end"))
    # opposing markers appear progressively
    for idx,(x,y) in enumerate([(250,280),(500,430),(760,260),(1010,430)]):
        if p > idx*.16:
            parts.append(circle(x,y,18,RED,"S"))
    if p>.45:
        for x in [360,650,900]:
            parts.append(line(x,220,x,500,GREEN,3,"9 9"))
    if p>.72:
        parts.append(text(640,520,"SUPPLY ROUTE DISRUPTED",22,RED,"bold","middle"))
    parts.append(text(640,600,"Simplified teaching diagram — not a scale map of a specific battle",15,MUTED,"middle"))
    return "".join(parts)

def timeline(p):
    parts=[]
    y=355
    parts.append(line(150,y,1130,y,"#607586",8))
    events=[
      (180,"30 NOV 1939","Invasion begins"),
      (465,"WINTER 1939–40","Defence and attrition"),
      (760,"FEB 1940","Soviet breakthrough"),
      (1090,"13 MAR 1940","Hostilities cease")
    ]
    for idx,(x,date,label) in enumerate(events):
        if p>idx*.22:
            parts.append(circle(x,y,15,[RED,GOLD,BLUE,GREEN][idx]))
            parts.append(text(x,300,date,19,INK,"bold","middle"))
            parts.append(text(x,405,label,16,MUTED,"normal","middle"))
    if p>.8:
        parts.append(text(640,520,"105 DAYS",48,GOLD,"bold","middle"))
        parts.append(text(640,565,"Finland remained independent; territorial concessions followed.",19,INK,"normal","middle"))
    return "".join(parts)

def treaty(p):
    parts=[]
    parts.append(text(640,195,"MOSCOW PEACE TREATY",27,INK,"bold","middle"))
    parts.append(text(640,240,"SIGNED 12 MARCH 1940",22,GOLD,"bold","middle"))
    parts.append(line(640,280,640,365,"#607586",4))
    parts.append(circle(640,390,15,BLUE))
    if p>.35:
        parts.append(text(640,450,"HOSTILITIES CEASED",23,INK,"bold","middle"))
        parts.append(text(640,490,"13 MARCH 1940",32,GOLD,"bold","middle"))
    if p>.7:
        parts.append(text(640,560,"Signature and ceasefire are different events.",18,MUTED,"normal","middle"))
    return "".join(parts)

if shutil.which("ffmpeg") is None:
    raise SystemExit("ffmpeg is required")
OUT.mkdir(parents=True,exist_ok=True)
render("motti_explainer","THE MOTTI METHOD","How a road-bound force could be isolated and divided",theatre,"Original schematic explanation — not a geographic battle map")
render("winter_war_timeline","THE WINTER WAR — 105 DAYS","A chronology of the 1939–1940 conflict",timeline,"Dates and chronology require final editorial verification")
render("peace_treaty_timing","THE PEACE SETTLEMENT","Treaty signature and cessation of hostilities",treaty,"Based on the Moscow Peace Treaty and protocol; verify wording against primary text")
