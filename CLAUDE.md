# Time — Re-Entry File
*Re-entry: time*

## What This Is
**Time** — functional meditation timer. Clean, minimal, contemporary. Mobile-first PWA. Companion app to Melt.
Built on Tim's feature spec: precise bells, intervals, custom sounds, notifications, presets, iOS Shortcuts, session log with Apple Health export.

## Re-Entry Phrase
> "Re-entry: time"

## Current Status
🔨 Local dev — port 5568

## Stack
- Python + Flask (gunicorn in prod)
- Local dev: port 5568, host 127.0.0.1
- Prod: Railway, PORT env var, host 0.0.0.0
- Inter + JetBrains Mono fonts
- Dark minimal UI — charcoal/slate, violet accent (#a78bfa), mint running state (#34d399)

## File Structure
```
time/
├── app.py
├── templates/index.html
├── static/
│   ├── manifest.json
│   ├── sw.js
│   └── icons/
├── data/
│   └── sounds/        ← uploaded user sounds
├── requirements.txt
├── Procfile
├── railway.toml
├── Makefile
└── .env.example
```

## How to Run (Local)
```bash
cd ~/time && make setup && make run
```

## Tim's Feature Set (all implemented)
- [x] Duration picker + custom h:mm:ss input
- [x] Equal-length intervals with bell at each
- [x] Upload custom audio files (WAV/MP3/AIFF/OGG/M4A)
- [x] Alert mode: Audio / Vibrate+Notify / Silent
- [x] Save/edit multiple timer presets (long-press to delete)
- [x] Pause, restart, cancel
- [x] Wake Lock (screen stays on)
- [x] iOS Shortcuts trigger at start + end (Do Not Disturb etc.)
- [x] Session log (localStorage, 200 entries)
- [x] Apple Health export via iOS Shortcuts URL scheme
- [x] CSV export
- [x] Notification API (smartwatch buzz)
- [x] Animated SVG ring progress

## Design Tokens
- bg: #0f0f12
- surface: #1a1a20
- accent: #a78bfa (violet)
- accent2: #34d399 (mint — running state)

## What's Next
- [ ] Deploy to Railway → time.creativekonsoles.com
- [ ] iOS home screen icons (192×192 + 512×512 PNG)
- [ ] Connect to AILIV biomarker endpoint for meditation data

## Last Session
Built from Tim's feature spec. Full PWA: ring timer, intervals, custom sounds upload, alert modes, presets, Shortcuts, log + Apple Health + CSV export. Mobile-first, Inter + JetBrains Mono, violet/mint palette.

---
*Last updated: 2026-05-24*
