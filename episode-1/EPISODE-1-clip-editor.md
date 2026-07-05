# 🎛️ EPISODE 1 — CLIP PICKER & EDITOR

A review + revision loop for the eight Seedance 2.0 fight clips. Open the picker,
flag what you want changed, export the spec, paste it back to Claude to execute.

---

## 1. THE PICKER — `clip-picker.html`
Open **`episode-1/clip-picker.html`** in a browser (Chrome / Safari / Firefox).
It plays all 8 clips (streamed from Higgsfield's CDN) and gives each one four choices:

| Flag | Meaning |
|------|---------|
| **Keep** | leave the clip as-is |
| **Regenerate** | re-roll the same shot (same refs + prompt) for a better take; optionally override the prompt |
| **Extend last frame** | make a new clip that *continues* from this clip's final frame (adds motion/length) |
| **Edit prompt** | keep the shot but change it per your notes (e.g. "more dust", "spino roars", "camera pushes in") |

Add per-clip **notes**, an optional **duration** (4–15s), and an optional **full
prompt override**, then click **Generate edit spec** → **Copy** and paste the JSON to Claude.

---

## 2. THE EDIT SPEC (what the picker exports)
```json
{
  "episode": "Episode 1 — Downtown Demolition (T-Rex vs Spinosaurus)",
  "model": "seedance_2_0",
  "actions": [
    { "id": "V4", "action": "regenerate", "shot": "...", "refs": ["TREX_REF","SPINO_REF"],
      "source_url": "https://.../V4.mp4", "duration": 5,
      "notes": "bigger dust cloud, slower impact", "prompt_override": null },
    { "id": "V6", "action": "extend", "refs": ["SPINO_REF","TREX_REF"],
      "source_url": "https://.../V6.mp4", "duration": 5,
      "notes": "spino keeps the pin, snaps twice, then t-rex kicks free" },
    { "id": "V7", "action": "edit", "refs": ["TREX_REF","SPINO_REF"],
      "source_url": "https://.../V7.mp4", "duration": 5,
      "notes": "make the billboard glow brighter and shatter fully" }
  ]
}
```
Only flagged clips appear in `actions`. `keep` clips are omitted.

---

## 3. HOW CLAUDE EXECUTES EACH ACTION
All generation uses the Higgsfield MCP `generate_video` tool, `model: seedance_2_0`,
with the locked settings (9:16, 720p, `std`, `epic`, no audio) unless the spec overrides them.

**`regenerate`** — resubmit the shot with the same `image_references` (TREX_REF
`2a6c7b99-c302-4b57-9b28-f5dd4e234408`, SPINO_REF `44d098c1-e9aa-41a3-bae5-a56a79f23f06`).
The prompt is the locked prompt for that shot, plus any `notes` folded in, or fully
replaced by `prompt_override` if present.

**`edit`** — same as regenerate, but the locked prompt is *modified* per `notes`
(the shot stays; only the requested details change). Character blocks stay word-for-word.

**`extend`** — continue from the clip's final frame:
1. Grab the last frame of `source_url` (extract with ffmpeg, or re-frame via Higgsfield), upload it → `media_id`.
2. New `generate_video` with that frame as the `start_image` role + a continuation prompt from `notes`.
3. The two dino hero stills ride along as `image_references` so identity holds.

**Rules for every action**
- Character blocks (T-Rex / Spino) are pasted verbatim — never paraphrased.
- Concurrency is capped (~3); Claude batches and backs off on `429 rate_limit_reached`.
- If the API returns a `preset_recommendation`, Claude resubmits with `declined_preset_id`.
- Each new result's job id + URL is appended to `seedance-manifest.json` (revisions keep the
  original clip id with a `-r2`, `-ext` suffix so nothing is overwritten).

---

## 4. THE LOOP
1. Open `clip-picker.html` → flag clips → export spec.
2. Paste the spec to Claude → Claude regenerates / extends / edits.
3. Claude updates `seedance-manifest.json` and refreshes the picker's baked-in URLs.
4. Re-open the picker, review the new takes, repeat until every clip is a **Keep**.
5. Ship the final 8 into `CAPCUT-BUILD-SHEET-downtown-demolition.md`.

*RAWR FIGHTS · RESULTS ARE REAL ✓*
