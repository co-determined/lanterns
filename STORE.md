# Lanterns — store listing (CrazyGames)

*Everything the Developer Portal asks for, ready to paste. Assets in `store/` (regenerate with `python3 shots.py` while `python3 -m http.server 8799` runs in this folder). Upload bundle: `dist/lanterns_v1.0.zip` (built by `./build.sh`).*

**Name:** Lanterns
**Tagline (short description):** Swipe through the lanterns as they rise. A small, warm game that knows what time it is.

**Description:**
Paper lanterns drift up from the hills. Swipe through them to light them — several in one stroke for a combo, and watch for the rare blue wish lanterns and the big slow moon lanterns. The ones you light gather into a glowing sky that stays with you for the whole round; the ones you miss drift away.

Pick what you're in the mood for — or let the hour decide:
• Before bed — slow and warm. The sky turns amber, the chimes fall, the score fades, and the game ends by itself.
• Afternoon slump — three bright, quick minutes.
• Calming down — the lanterns rise at the pace of a slow breath.
• Just play — endless. Leaving is free; come back any time.

One file, no account, nothing to install. Works with mouse or touch.

**Controls:**
Mouse: click and drag through lanterns to light them; click a lantern to light just that one.
Touch: swipe through lanterns; tap to light one.
Top-left pill: change mood. Top-right: sound on/off.

**Category:** Casual · **Tags:** relaxing, arcade, one-button, swipe, lanterns, night, chill, calm, endless, mobile
**Age rating:** everyone (PEGI 3 content; site audience 13+ — nothing targeted at kids)
**Orientation:** both (responsive; portrait on phones, landscape on desktop)
**Languages:** English
**Multiplayer:** no · **In-game purchases:** no · **External links:** none

**Monetization (SDK v3, full-launch):** `gameplayStart/Stop` on every start, pause, mood-picker open, and end · `loadingStart/Stop` around SDK init · `happytime` on a 4+ combo and on a new best after the first round · **midgame ad** only at round end in the two arcade moods (afternoon slump, just play), never on the first round, never inside 3 minutes of the last one, audio ducked while it plays · **responsive banner** on the end card in those two moods, cleared when the card closes · no ads at all in *before bed* and *calming down* (the whole point of those modes is that nothing loud happens) · works with the SDK absent, disabled, or blocked — every call is wrapped.

**Privacy:** nothing leaves the device. The one-tap "how do you feel?" at the end of the two calm moods and the best score are stored in the browser's localStorage only.

**Publisher / payee:** MycoChat LLC (Seattle, WA; EIN on file). Tipalti payout onboarding needs the LLC's W-9 — one signature from Skylar, when the first €100 is in sight, not before.

**Assets (store/):**
- `cover_512.png` — 512×512 cover
- `cover_1920x1080.png` — landscape cover · `cover_1080x1920.png` — portrait cover
- `shot1_bed_early.png`, `shot2_bed_mid.png`, `shot3_bed_late.png`, `shot4_play.png`, `shot5_slump.png`, `shot6_calm.png` — gameplay screenshots, 1920×1080 (real renders of the game, not mockups)
- `phone_bed.png` (390×844), `iframe_800x450.png` — legibility checks at the smallest and portrait iframes; `end_bed.png` — the end card

**Originality statement (if asked):** original code (single HTML file, vanilla JS/canvas), original procedural art (no third-party assets), original audio (WebAudio synthesis at runtime). Built by the Syntonia household studio.
