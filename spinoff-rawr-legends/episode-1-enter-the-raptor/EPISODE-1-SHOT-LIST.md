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
- **S1 → `S1-dragon-e.png`** (job `1d7acb72`, nano_banana_pro) — **true-likeness pass**: full jumpsuit, claw-scratched chest, coiled stance in the rain. THE hero reference for all clips.
  - `S1-dragon-f.png` (job `9d342be0`) — jumpsuit stripped to the waist, battle-damaged: use as the Act III mid-fight look (shots 9–12).
  - `S1-dragon-c/d.png` (soul_2 likeness pass) + `a/b` (first pass) — alternates/reference only.
- **S2 → `S2-raptor-b.png`** (job `f4003eac`) — snarling jaw, amber eye, neon steam. (`a` = clean side profile, use as secondary angle reference)
- **S3 → `S3-arena-a.png`** (job `293ff1a6`) — symmetrical raised ring, giant neon dragon, lanterns, skyline. (`b` = elevated alt angle, usable for shot 10's God's-eye)
- **S4 → `S4-keyart-b.png`** (job `358a3dde`) — brush-style ENTER THE RAPTOR type, cyan-glow Dragon vs pink-glow Raptor. This is the title drop AND the YouTube thumbnail.

Reference the winner's **job_id** as the start-frame in every video generation below.

---

## 🎥 THE CLIPS — 15 shots, 15 UNIQUE ANGLES (the non-repeating rule)

Cut on the Onslaught1 beat grid. Angles never repeat — that's the series signature.
The fight is built around Bruce's three signature weapons, in escalating order:
**nunchaku combos → flying kick → one-inch punch (the finisher).**

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

### ACT III — THE FIGHT (~0:30–0:50, music: full onslaught)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 8 | First exchange | **Whip-pan following the lunge** | S2 | raptor lunges, Dragon sidesteps at the last inch, claws shred a lantern, sparks and paper embers |
| 9 | Nunchaku reveal | **Rack focus: raptor's snapping jaws foreground → Dragon behind** | S1-e | jaws snarl in blurred foreground; focus snaps to the Dragon pulling nunchaku from his belt, one slow warm-up spin, eyes locked |
| 10 | THE CRAZY COMBO | **180° orbiting arc shot, speed-ramped** | S1-f | camera circles him as the nunchaku blurs: double figure-8s, behind-the-back pass, under-the-arm catch, neck wrap and re-draw — rain whipping off the chains in spirals, neon streaks smearing |
| 11 | Combo connects | **Handheld shaky close, inside the fight** | S1-f + S2 | end of the combo cracks across the raptor's jaw mid-lunge, spit and rain flying, raptor staggers sideways |
| 12 | THE FLYING KICK | **Top-down overhead (God's-eye)** | S3-b + both | Dragon launches — full flying side-kick connects square in the ribs, raptor skids across the wet ring through neon reflections, lanterns scatter |
| 13 | Last stand | **Reflection shot: action in a puddle, then tilt up** | S2 | the raptor rises one final time, shakes off rain, screams at the sky — it's not done |

### THE FINISHER — ONE-INCH PUNCH (~0:50–0:60, music: final hit + tail-out)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 14 | One inch | **Locked-off macro insert, extreme close-up** | S1-f | DEAD SILENCE beat: his open palm settles ONE INCH from the raptor's heaving chest scales, fingers slowly curl into a fist, a single raindrop rolls off his knuckle — hold it, let the audience lean in |
| 15 | THE PUNCH | **Fist-level side profile, ultra-slow-mo (1000fps feel), speed-ramp** | S1-f + S2 | the fist travels one inch — a shockwave ring of mist explodes off the raptor's chest, rain hangs suspended, the raptor is LAUNCHED across the ring through the lantern ropes; ramp to real-time on the landing, freeze on the Dragon's follow-through, film-burn to the RAWR LEGENDS end card |

**Angle audit ✓** 1 drone push / 2 low track behind / 3 dutch ECU / 4 crash-zoom out / 5 locked
symmetrical wide / 6 over-shoulder / 7 worm's-eye / 8 whip-pan / 9 rack focus / 10 orbiting arc /
11 handheld / 12 God's-eye / 13 puddle-reflection tilt-up / 14 locked macro insert / 15 fist-level
slow-mo profile. **15 shots, zero repeats.**

### Wardrobe continuity 👕
- Shots 1–8: full jumpsuit (**S1-e**)
- Shots 9–15: jumpsuit stripped to the waist, battle-damaged (**S1-f**) — the nunchaku reveal
  doubles as the "getting serious" costume turn, so escalation reads on screen.

---

## 🎵 MUSIC SYNC
- Track: `music/Onslaught1.mp3` (the series track — every episode)
- Higgsfield media_id `d48ff0d5-d756-4625-961e-7c8ed744bb2f`
- Map the beat grid in the editor first; clips 4, 8, 10, 12 land on hits.
- **Shot 14 is the exception: cut the music to near-silence** (low rumble only) for the
  one-inch hold, then shot 15's punch lands ON the track's biggest hit. Silence sells the drama.

## ⚙️ EXPORT
1920×1080 · 24 or 30fps · AI-disclosure ON · title: **RAWR LEGENDS Ep.1 — ENTER THE RAPTOR 🐉🦖**
