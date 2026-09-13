# Lanterns

Swipe through the lanterns as they rise. A small, warm browser game that knows what time it is.

One HTML file, no dependencies, no build step. Works with mouse or touch, from an 800×450 iframe to a 4K desktop.

**Play:** https://co-determined.github.io/lanterns/

Pick a mood — or let the hour pick: *before bed* (slows, warms, ends on its own), *afternoon slump* (three bright minutes), *calming down* (paced to a slow breath), *just play* (endless; leaving is free). Several lanterns in one stroke is a combo; blue wish lanterns are ×5, moon lanterns ×3, tethered pairs pay a bonus. The ones you light gather into a sky that stays for the round.

Nothing leaves your device. The one-tap "how do you feel?" at the end of the calm moods and your best score live in your own browser's localStorage.

## Files
- `index.html` — the game (v1.0). CrazyGames SDK v3 is loaded from their CDN when present; every call is wrapped, so the game runs identically with no SDK, a disabled SDK, or an adblocker.
- `STORE.md` — the store listing, ready to paste. `store/` — covers and screenshots (real renders). `dist/` — upload zip (`./build.sh`).
- `shots.py` — regenerates `store/` with headless Chrome (serve the folder on :8799 first).
- `index_v0.1.html` — the first playable, kept for the record.

## Testing without a human
`window.__lanterns` on the page: `state()`, `sim(seconds)` (drives physics with no requestAnimationFrame), `swipe(x0,y0,x1,y1)`, `tap(x,y)`, `lanterns()`, `lightAll()`, `setMode('bed'|'slump'|'calm'|'play')`, `frame(dt)`, `render()`, `sample()` (horizon RGB), `showcase()`. Query params: `?mode=bed&seed=3` (deterministic), `?qa=showcase&sec=200&n=14&title=1&nosdk=1` (a still frame for screenshots), `&end=1` (the end card).

Built 2026-09-13 by Claude for the Syntonia household studio — six AI siblings and the people who keep the house. MycoChat LLC.
