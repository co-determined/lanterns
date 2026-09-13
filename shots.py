#!/usr/bin/env python3
"""Render Lanterns store assets with headless Chrome. Needs the game served at http://127.0.0.1:8799/ .
Usage: python3 shots.py   -> writes store/*.png"""
import subprocess, os, time, tempfile, sys
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE=[CH,"--headless=new","--disable-gpu","--hide-scrollbars","--no-first-run","--no-default-browser-check","--disable-background-networking","--disable-component-update","--no-service-autorun","--disable-sync","--metrics-recording-only","--virtual-time-budget=3000"]
os.makedirs("store",exist_ok=True)
def shot(name,size,q,timeout=25):
    out=f"store/{name}.png"
    if os.path.exists(out): os.unlink(out)
    w,h=map(int,size.split(","))
    scale=2 if min(w,h)<1000 else 1   # headless Chrome clamps the window to >=500px wide and steals ~87px of chrome: render 2x, downscale
    with tempfile.TemporaryDirectory(prefix="lshot_", ignore_cleanup_errors=True) as prof:
        cmd=BASE+[f"--screenshot={out}",f"--window-size={w*scale},{h*scale}",f"--user-data-dir={prof}",f"http://127.0.0.1:8799/index.html?{q}&nosdk=1"]
        p=subprocess.Popen(cmd,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); t0=time.time(); ok=False
        while time.time()-t0<timeout:
            if os.path.exists(out) and os.path.getsize(out)>0: time.sleep(0.6); ok=True; break
            time.sleep(0.25)
        p.kill(); p.wait(); time.sleep(0.4)
    if ok and scale!=1:
        from PIL import Image
        im=Image.open(out); im=im.resize((w,h),Image.LANCZOS); im.save(out)
    print(f"{name}: {'ok' if ok else 'FAILED'} {round(time.time()-t0,1)}s", flush=True)
SHOTS = sys.argv[1:] or ["all"]
S = {
 "cover_512":        ("512,512",   "qa=showcase&seed=21&sec=200&mode=bed&n=10&title=1"),
 "cover_1920x1080":  ("1920,1080", "qa=showcase&seed=3&sec=200&mode=bed&n=16&title=1"),
 "cover_1080x1920":  ("1080,1920", "qa=showcase&seed=8&sec=200&mode=bed&n=12&title=1"),
 "shot1_bed_early":  ("1920,1080", "qa=showcase&seed=31&sec=40&mode=bed&n=12"),
 "shot2_bed_mid":    ("1920,1080", "qa=showcase&seed=3&sec=200&mode=bed&n=16"),
 "shot3_bed_late":   ("1920,1080", "qa=showcase&seed=5&sec=430&mode=bed&n=8"),
 "shot4_play":       ("1920,1080", "qa=showcase&seed=7&sec=90&mode=play&n=16"),
 "shot5_slump":      ("1920,1080", "qa=showcase&seed=9&sec=150&mode=slump&n=18"),
 "shot6_calm":       ("1920,1080", "qa=showcase&seed=13&sec=120&mode=calm&n=10"),
 "phone_bed":        ("390,844",   "qa=showcase&seed=11&sec=200&mode=bed&n=8"),
 "iframe_800x450":   ("800,450",   "qa=showcase&seed=3&sec=200&mode=bed&n=10"),
 "end_bed":          ("1920,1080", "qa=showcase&seed=3&sec=470&mode=bed&n=10&end=1"),
}
for k,(size,q) in S.items():
    if SHOTS==["all"] or k in SHOTS: shot(k,size,q)
