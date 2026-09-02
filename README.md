# Time

A meditation timer that gets the timing right. Live at
[time.creativekonsoles.com](https://time.creativekonsoles.com).

## What it does

Precise bells. Interval bells inside a sit, so a 40 minute session can chime at 10 and 30
without you setting three timers. Custom sounds, saved presets, and a session log that
exports to Apple Health.

Mobile-first PWA. Installs to a home screen and runs offline.

## The honest limitation, and what it led to

A PWA cannot reliably fire a sound when the phone is locked, backgrounded, or in Do Not
Disturb. That is not a bug to fix, it is the boundary of what a web app is allowed to do on
iOS, and it matters more here than almost anywhere else: a meditation timer whose closing
bell does not ring while your screen is off has failed at its one job.

So this repo stays a PWA and does the part a PWA does well, and a thin native iOS shell
wraps it to add real local notifications. Same app, one capability added at the layer that
is allowed to have it.

## Built from a spec

The feature list came from someone who actually sits, not from guessing at what a
meditation app should have. Interval bells and the session log both came from that
conversation, and neither would have been in a version I designed alone.

## Running it

```bash
make run
```

Python, Flask, PWA.
