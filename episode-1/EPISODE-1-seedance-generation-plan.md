# 🦖 EPISODE 1 — SEEDANCE 2.0 GENERATION PLAN
### "Downtown Demolition" · T-Rex vs Spinosaurus · all 8 clips

This is the **live, executed** plan for generating the 8 fight clips on Higgsfield's
**Seedance 2.0** (`seedance_2_0`) model. Unlike the DoP kit, Seedance is a
reference-driven, identity-consistent video model — so every clip is generated
**image-to-video** from the *same two approved hero stills*. Same reference =
same dinosaur, shot to shot.

---

## 🔒 LOCKED INPUTS

**Two approved hero stills** (generated with `nano_banana_2`, 2K, 9:16, reused as
`image_references` on every clip):

| Ref | Media / job id | Subject |
|-----|----------------|---------|
| `TREX_REF`  | `2a6c7b99-c302-4b57-9b28-f5dd4e234408` | full-body T-Rex hero still |
| `SPINO_REF` | `44d098c1-e9aa-41a3-bae5-a56a79f23f06` | full-body Spinosaurus hero still |

**Locked model settings (identical on all 8 clips):**
- model: `seedance_2_0`
- aspect_ratio: `9:16` · resolution `720p` · mode `std`
- duration: `5s` · genre `epic` · `generate_audio: false` · bitrate `standard`

**Locked character blocks** (paste word-for-word into every prompt):
- **T-REX:** *a colossal kaiju-sized Tyrannosaurus rex with dark olive-green scaly
  hide, faded amber underbelly, three deep parallel red scars across its left
  shoulder, dull burnt-orange eyes, heavy muscular build and weathered cracked wet skin*
- **SPINO:** *a colossal kaiju-sized Spinosaurus with blue-grey hide and dark
  charcoal dorsal striping, a tall red-and-black sail, a long narrow crocodilian
  snout, a pale cream underbelly and lean powerful athletic build*
- **SCENE:** *rain-soaked neon-lit downtown city at night, towering hundreds of feet
  at true kaiju scale over the skyscrapers, tiny cars and buses far below on the
  flooded street for scale, searchlights and pyro flares, sheets of rain and steam,
  glistening wet scales, dramatic blockbuster lighting, photorealistic, hyper-detailed,
  vertical 9:16. Absolutely no people, no humans, no crowds anywhere in frame.*

---

## 🎬 THE 8 CLIPS (refs + motion)

| Clip | Shot | image_references |
|------|------|------------------|
| V1 | T-Rex erupts up through the street (entrance) | `TREX_REF` |
| V2 | Spino smashes head-first through a skyscraper (entrance) | `SPINO_REF` |
| V3 | The two face off across a flooded neon street (staredown) | `TREX_REF` + `SPINO_REF` |
| V4 | T-Rex charges and slams Spino through an office building | `TREX_REF` + `SPINO_REF` |
| V5 | Spino tail-swipes a row of cars + a bus into T-Rex | `SPINO_REF` + `TREX_REF` |
| V6 | Spino pins T-Rex against a skyscraper, jaws snapping | `SPINO_REF` + `TREX_REF` |
| V7 | T-Rex drives Spino backward through a giant neon billboard | `TREX_REF` + `SPINO_REF` |
| V8 | FINISHER — slow-mo neck clamp + slam, pavement craters | `TREX_REF` + `SPINO_REF` |

---

## ⚙️ EXECUTION NOTES
- Submitted via the Higgsfield MCP `generate_video` tool, `model: seedance_2_0`,
  each ref passed as a `medias[]` entry with role `image_references`.
- Seedance caps concurrent jobs (~3); submit in batches and back off on `429
  rate_limit_reached` rather than retrying tight.
- If the API returns a `preset_recommendation` notice instead of submitting,
  resubmit with `declined_preset_id` set to the offered preset to generate literally.
- Cost: ~22.5 credits per 720p/5s clip.
- Result URLs for each generated clip are recorded in `seedance-manifest.json`.

## ➡️ NEXT
Take V1–V8 into the **CapCut build sheet** (`CAPCUT-BUILD-SHEET-downtown-demolition.md`)
— overlays, health bars, nameplates, and VO are already prepared.

*RAWR FIGHTS · RESULTS ARE REAL ✓*
