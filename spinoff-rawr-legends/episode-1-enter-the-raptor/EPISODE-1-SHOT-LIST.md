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

## 🎥 THE CLIPS — 17 shots, 17 UNIQUE ANGLES (the non-repeating rule)

Cut on the Onslaught1 beat grid. Angles never repeat — that's the series signature.

**Fight logic:** the Raptor wins the first half. Its sneaky claw attack draws FIRST BLOOD —
that wound is what makes the Dragon pull the nunchaku. Escalation:
**raptor slashes → first blood → nunchaku combos → flying kick → raptor's finisher attempt → one-inch punch counter.**

### 🦖 THE RAPTOR'S MOVESET (it's a fighter, not a victim)
| Move | What it is |
|---|---|
| **The Switchblade** | fancy slash flurry — spinning tail-pivot into chained sickle-claw slashes, showy and fast |
| **The Pickpocket** | the sneaky one — tail feints HIGH at the face, hidden foot-claw rakes LOW across the chest |
| **The Guillotine** | its finisher — leaps off the corner structure into a claws-first death-dive |

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

### ACT III-A — THE RAPTOR'S ROUND (~0:30–0:40, music: full onslaught)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 8 | THE SWITCHBLADE | **Whip-pan following each slash** | S2 + S1-e | raptor's showy slash flurry: spinning tail-pivot into three chained sickle slashes, Dragon weaving backward on his heels, a lantern and a neon sign shredded, sparks and paper embers |
| 9 | THE PICKPOCKET — first blood | **Low lateral dolly slide at waist height, speed-ramped** | S2 + S1-e | the sneaky one: tail whips HIGH at his face — he blocks it — hidden foot-claw rakes LOW across his chest, three red lines through the yellow suit. He staggers back, touches the wound, looks at his hand. The raptor does a taunting little strut |
| 10 | Nunchaku reveal | **Rack focus: raptor's snapping jaws foreground → Dragon behind** | S1-f | jaws snarl in blurred foreground; focus snaps to the wounded Dragon stripping the torn jumpsuit to his waist and pulling nunchaku from his belt, one slow warm-up spin, eyes locked. NOW it's personal |

### ACT III-B — THE DRAGON'S ANSWER (~0:40–0:50)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 11 | THE CRAZY COMBO | **180° orbiting arc shot, speed-ramped** | S1-f | camera circles him as the nunchaku blurs: double figure-8s, behind-the-back pass, under-the-arm catch, neck wrap and re-draw — rain whipping off the chains in spirals, neon streaks smearing |
| 12 | Combo connects | **Handheld shaky close, inside the fight** | S1-f + S2 | end of the combo cracks across the raptor's jaw mid-lunge, spit and rain flying, raptor staggers sideways |
| 13 | THE FLYING KICK | **Top-down overhead (God's-eye)** | S3-b + both | Dragon launches — full flying side-kick connects square in the ribs, raptor skids across the wet ring through neon reflections, lanterns scatter |

### ACT III-C — THE RAPTOR'S FINISHER vs THE ONE-INCH PUNCH (~0:50–1:05)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 14 | The climb | **Reflection shot: action in a puddle, then tilt up** | S2 + S3-a | the raptor rises, shakes off rain, screams — then springs onto the corner structure above the ring, coiling low against the neon dragon sign. It's setting something up |
| 15 | THE GUILLOTINE | **Dragon's POV — the dive comes AT CAMERA** | S2 | the raptor launches into its claws-first death-dive straight at the lens, sickle claws leading, backlit by lightning — at the last frame the view slips sideways: the dive MISSES, the raptor crashes through the lantern ropes, dazed |
| 16 | One inch | **Locked-off macro insert, extreme close-up** | S1-f | DEAD SILENCE beat: his open palm settles ONE INCH from the dazed raptor's heaving chest scales, fingers slowly curl into a fist, a single raindrop rolls off his knuckle — hold it, let the audience lean in |
| 17 | THE PUNCH | **Fist-level side profile, ultra-slow-mo (1000fps feel), speed-ramp** | S1-f + S2 | the fist travels one inch — a shockwave ring of mist explodes off the raptor's chest, rain hangs suspended, the raptor is LAUNCHED across the ring through the lantern ropes; ramp to real-time on the landing, freeze on the Dragon's follow-through, film-burn to the RAWR LEGENDS end card |

**Angle audit ✓** 1 drone push / 2 low track behind / 3 dutch ECU / 4 crash-zoom out / 5 locked
symmetrical wide / 6 over-shoulder / 7 worm's-eye / 8 whip-pan / 9 low lateral dolly slide /
10 rack focus / 11 orbiting arc / 12 handheld / 13 God's-eye / 14 puddle-reflection tilt-up /
15 POV dive-at-camera / 16 locked macro insert / 17 fist-level slow-mo profile. **17 shots, zero repeats.**

### Wardrobe + wound continuity 👕🩸
- Shots 1–9: full jumpsuit (**S1-e**), chest clean until shot 9.
- **Shot 9 CREATES the chest scratches** — the Pickpocket's rake is where the claw marks
  seen in the hero stills come from.
- Shots 10–17: jumpsuit stripped to the waist, scratched chest (**S1-f**) — the costume turn
  is motivated by the wound, so the escalation reads on screen.

---

## 🎵 MUSIC SYNC
- Track: `music/Onslaught1.mp3` (the series track — every episode)
- Higgsfield media_id `d48ff0d5-d756-4625-961e-7c8ed744bb2f`
- Map the beat grid in the editor first; clips 4, 8, 11, 13, 15 land on hits
  (shot 9's claw rake lands just OFF the beat — sneak attacks shouldn't be telegraphed by the music).
- **Shot 16 is the exception: cut the music to near-silence** (low rumble only) for the
  one-inch hold, then shot 17's punch lands ON the track's biggest hit. Silence sells the drama.

## ⚙️ EXPORT
1920×1080 · 24 or 30fps · AI-disclosure ON · title: **RAWR LEGENDS Ep.1 — ENTER THE RAPTOR 🐉🦖**
