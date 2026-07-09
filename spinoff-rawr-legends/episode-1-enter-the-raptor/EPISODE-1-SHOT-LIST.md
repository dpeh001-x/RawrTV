# 🥋🦖 EPISODE 1 — "ENTER THE RAPTOR"
### RAWR LEGENDS · The Dragon vs. The Raptor · 16:9 · one track: Onslaught1

**Set:** rain-soaked Hong Kong rooftop fight arena, night, neon (pink/cyan), steam, puddles.
**Consistency lever:** every clip is image-to-video driven from the hero stills in `/stills`.

---

## 🖼️ THE STILLS (generate these FIRST — done via Higgsfield MCP)

| Still | What it locks | Model | Job IDs (2 variants each) |
|---|---|---|---|
| S1 · The Dragon hero still | hero look: yellow jumpsuit, black stripes, bowl cut, claw-scratched chest | soul_2 | `7421845c-6279-424b-990c-47b57854f796`, `5884ed07-998b-4537-befc-0dc21ff2a2bd` |
| S2 · The Raptor hero still | creature look: dark-green hide, black tiger stripes, scars, amber eyes | nano_banana_pro | `87ca0059-3f85-48bd-9323-add149013030`, `f4003eac-21c2-40b2-ae8f-8fd8bf3ff229` |
| S3 · The Arena (empty set) | location: rooftop arena, neon dragon sign, lanterns | nano_banana_pro | `293ff1a6-7e57-49aa-a330-fc8fd0eabf52`, `803736f5-1ae9-4948-9e55-96a94966d4c4` |
| S4 · Key art / title card | grand-intro title drop: "ENTER THE RAPTOR" | nano_banana_pro | `752887f7-49d0-4181-91ec-361902e5f146`, `358a3dde-563f-4885-89d0-7f4aa417591c` |

All 8 variants are saved in `/stills`. **Winners picked:**
- **S1 → `S1-dragon-b.png`** (job `5884ed07`) — full jumpsuit + black belt, claw-scratched chest, rain. (variant `a` had chest artifacts, keep as reference only)
- **S2 → `S2-raptor-b.png`** (job `f4003eac`) — snarling jaw, amber eye, neon steam. (`a` = clean side profile, use as secondary angle reference)
- **S3 → `S3-arena-a.png`** (job `293ff1a6`) — symmetrical raised ring, giant neon dragon, lanterns, skyline. (`b` = elevated alt angle, usable for shot 10's God's-eye)
- **S4 → `S4-keyart-b.png`** (job `358a3dde`) — brush-style ENTER THE RAPTOR type, cyan-glow Dragon vs pink-glow Raptor. This is the title drop AND the YouTube thumbnail.

Reference the winner's **job_id** as the start-frame in every video generation below.

---

## 🎥 THE CLIPS — 12 shots, 12 UNIQUE ANGLES (the non-repeating rule)

Cut on the Onslaught1 beat grid. Angles never repeat — that's the series signature.

### ACT I — THE GRAND INTRODUCTION (~0:00–0:15, music: intro build)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 1 | The set awakens | **Slow drone push-in, high wide, descending** | S3 | neon flickers on sign by sign, rain, steam rises, empty arena breathing |
| 2 | The Dragon's entrance | **Low tracking shot from behind, slow-mo** | S1 | he walks through parting steam toward camera-away, knuckles crack, yellow suit glowing under neon |
| 3 | The Raptor's reveal | **Extreme close-up, dutch tilt** | S2 | amber eye snaps open in darkness, pupil contracts, rain drips off snout, low growl |
| 4 | Title drop | **Crash-zoom out from lightning strike** | S4 | key art slams in ON THE FIRST BIG HIT of Onslaught1 |

### ACT II — THE STANDOFF (~0:15–0:30)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 5 | Face-off | **Symmetrical wide profile, locked-off, both in frame** | S3 + S1 + S2 | 20 feet apart, rain between them, neither moves, lanterns sway |
| 6 | The Dragon reads him | **Over-the-Raptor's-shoulder, shallow focus** | S1 | slides into stance, beckons with fingers, iconic 'come here' gesture |
| 7 | The Raptor circles | **Ground-level worm's-eye, wide lens distortion** | S2 | sickle claws pass inches from lens through puddle, tail whips |

### ACT III — THE FIGHT (~0:30–0:55, music: full onslaught)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 8 | First exchange | **Whip-pan following the lunge** | S2 | raptor lunges, Dragon sidesteps, claws shred a lantern, sparks |
| 9 | The flurry | **Handheld shaky close, inside the fight** | S1 | punches and one-inch strikes vs snapping jaws, rain flying off impacts |
| 10 | The kick | **Top-down overhead (God's-eye)** | S3 + both | Dragon's flying side-kick connects, raptor skids across wet concrete through neon reflections |
| 11 | Last stand | **Reflection shot: action seen in a puddle, then tilt up** | S2 | raptor rises, shakes off rain, screams at the sky |
| 12 | The finish | **Slow push-in to hero freeze-frame, film-burn** | S1 | Dragon lands the final strike, freeze on impact, film grain burns out → RAWR LEGENDS end card |

**Angle audit ✓** drone push / low track / dutch ECU / crash-zoom / locked wide / over-shoulder /
worm's-eye / whip-pan / handheld / God's-eye / puddle-reflection / slow push freeze. **Zero repeats.**

---

## 🎵 MUSIC SYNC
- Track: `music/Onslaught1.mp3` (the series track — every episode)
- Higgsfield media_id `d48ff0d5-d756-4625-961e-7c8ed744bb2f`
- Map the beat grid in the editor first; clips 4, 8, 10, 12 land on hits.

## ⚙️ EXPORT
1920×1080 · 24 or 30fps · AI-disclosure ON · title: **RAWR LEGENDS Ep.1 — ENTER THE RAPTOR 🐉🦖**
