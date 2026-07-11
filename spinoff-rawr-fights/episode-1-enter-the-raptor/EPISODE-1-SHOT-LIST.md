# 🥋🦖 EPISODE 1 — "ENTER THE RAPTOR"
### RAWR FIGHTS: CINEMATIC · The Dragon vs. The Raptor · 16:9 · one track: Dead Meat

**Set:** rain-soaked Hong Kong rooftop fight arena, night, neon (pink/cyan), steam, puddles.
**Consistency lever:** every clip is image-to-video driven from the hero stills in `/stills`.
**Scale lock:** the Raptor is **slightly smaller than the Dragon** (~1.5 m vs ~1.7 m) — a real
duel of equals, never a monster towering over him. **Physics lock:** real weight, momentum,
recoil, and grounded gravity in every clip (see the bible's Physics + Scale rules).

---

## 🖼️ THE STILLS (generate these FIRST — done via Higgsfield MCP)

| Still | What it locks | Model | Job IDs (2 variants each) |
|---|---|---|---|
| S1 · The Dragon hero still | hero look: yellow jumpsuit, black stripes, bowl cut, claw-scratched chest | soul_2 | `7421845c-6279-424b-990c-47b57854f796`, `5884ed07-998b-4537-befc-0dc21ff2a2bd` |
| S2 · The Raptor hero still | creature look: dark-green hide, black tiger stripes, scars, amber eyes | nano_banana_pro | `87ca0059-3f85-48bd-9323-add149013030`, `f4003eac-21c2-40b2-ae8f-8fd8bf3ff229` |
| S3 · The Arena (empty set) | location: rooftop arena, neon dragon sign, lanterns | nano_banana_pro | `293ff1a6-7e57-49aa-a330-fc8fd0eabf52`, `803736f5-1ae9-4948-9e55-96a94966d4c4` |
| S4 · Key art / title card | grand-intro title drop: "ENTER THE RAPTOR" | nano_banana_pro | `752887f7-49d0-4181-91ec-361902e5f146`, `358a3dde-563f-4885-89d0-7f4aa417591c` |

### ✅ FINAL CUT — LOCKED BY CLIENT
| Slot | Winner | File |
|---|---|---|
| Dragon | **E** | `S1-dragon-e.png` |
| Raptor | **B** | `S2-raptor-b.png` |
| Arena | **A** | `S3-arena-a.png` |
| Key Art | **B (corrected)** | `S4-keyart-b2.png` — text fixed: top line now **RAWR FIGHTS**, **EPISODE 1 removed** (job `e156926e`, edited from the original B) |

All 8 variants are saved in `/stills`. **Winners picked:**
- **S1 → `S1-dragon-e.png`** (job `1d7acb72`, nano_banana_pro) — **true-likeness pass**: full jumpsuit, claw-scratched chest, coiled stance in the rain. THE hero reference for all clips.
  - `S1-dragon-f.png` (job `9d342be0`) — jumpsuit stripped to the waist, battle-damaged: the mid-/late-fight look (shots 10–23).
  - `S1-dragon-c/d.png` (soul_2 likeness pass) + `a/b` (first pass) — alternates/reference only.
- **S2 → `S2-raptor-b.png`** (job `f4003eac`) — snarling jaw, amber eye, neon steam. (`a` = clean side profile, use as secondary angle reference)
  - ⚠️ **Scale note:** S2 was generated as a solo portrait described "~6 ft" — fine as a *look* reference (no size cue in-frame), but every **two-shot** clip must prompt the locked relationship (**raptor slightly SHORTER than the Dragon**). If any two-shot renders the raptor towering, regenerate that clip; the still itself does not need redoing.
- **S3 → `S3-arena-a.png`** (job `293ff1a6`) — symmetrical raised ring, giant neon dragon, lanterns, skyline. (`b` = elevated alt angle, usable for shot 10's God's-eye)
- **S4 → `S4-keyart-b2.png`** (job `e156926e`) — the **corrected** title card: top line **RAWR FIGHTS**, no episode line. This is the title drop AND the YouTube thumbnail. (`S4-keyart-b.png` is the original, superseded — still said "RAWR LEGENDS / EPISODE 1".)

Reference the winner's **job_id** as the start-frame in every video generation below.

---

## 🎥 THE CLIPS — 23 shots, 23 UNIQUE ANGLES (the non-repeating rule)

Cut on the Dead Meat beat grid. Angles never repeat — that's the series signature.
Every clip holds the **scale lock** (raptor slightly smaller than the Dragon) and the
**physics lock** (real weight, momentum, recoil, grounded gravity).

**Fight logic — three false endings:**
1. Raptor wins the first half: Switchblade slashes, then the Pickpocket draws FIRST BLOOD.
2. The Dragon answers: bare-hand flurry → flying kick → the ONE-INCH PUNCH launches the
   raptor through the ropes. *Looks over.* It isn't.
3. The raptor rises and its GUILLOTINE finisher CONNECTS — the Dragon is down, flat on the
   concrete, music dead. Then: the iconic kip-up somersault, the nunchaku comes out, and a
   crazy complicated combo delivers a flurry of blows to the raptor's head until its skull
   ridge CRACKS — **KO. The nunchaku storm is the true finale.**

### 🦖 THE RAPTOR'S MOVESET (it's a fighter, not a victim)
| Move | What it is |
|---|---|
| **The Switchblade** | fancy slash flurry — spinning tail-pivot into chained sickle-claw slashes, showy and fast |
| **The Pickpocket** | the sneaky one — tail feints HIGH at the face, hidden foot-claw rakes LOW across the chest |
| **The Guillotine** | its finisher — leaps off the corner structure into a claws-first death-dive |

### ACT I — THE GRAND INTRODUCTION (~0:00–0:15, music: intro build)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 1 | The set awakens | **Slow drone push-in, high wide, descending** | S3-a | neon flickers on sign by sign, rain, steam rises, empty arena breathing |
| 2 | The Dragon's entrance | **Low tracking shot from behind, slow-mo** | S1-e | he walks through parting steam toward camera-away, knuckles crack, yellow suit glowing under neon. Back to lens — chest not shown |
| 3 | The Raptor's reveal | **Extreme close-up, dutch tilt** | S2-b | amber eye snaps open in darkness, pupil contracts, rain drips off snout, low growl |
| 4 | Title drop | **Crash-zoom out from lightning strike** | S4-b2 | key art slams in ON THE FIRST BIG HIT of Dead Meat (this is a motion-graphics beat, not a fresh generation) |

### ACT II — THE STANDOFF (~0:15–0:30)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 5 | Face-off | **Symmetrical wide profile, locked-off, both in frame** | S3-a + S1-e + S2-b | 20 feet apart, rain between them, neither moves, lanterns sway. Enforce scale: raptor reads shorter than the Dragon |
| 6 | The Dragon reads him | **Over-the-Raptor's-shoulder, shallow focus** | S1-e | slides into stance, beckons with fingers, iconic 'come here' gesture |
| 7 | The Raptor circles | **Ground-level worm's-eye, wide lens distortion** | S2-b | sickle claws pass inches from lens through puddle, tail whips |

### ACT III-A — THE RAPTOR'S ROUND (~0:30–0:40, music: full onslaught)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 8 | THE SWITCHBLADE | **Whip-pan following each slash** | S2 + S1-e | raptor's showy slash flurry: spinning tail-pivot into three chained sickle slashes, Dragon weaving backward on his heels, a lantern and a neon sign shredded, sparks and paper embers |
| 9 | THE PICKPOCKET — first blood | **Low lateral dolly slide at waist height, speed-ramped** | S2 + S1-e | the sneaky one: tail whips HIGH at his face — he blocks it — hidden foot-claw rakes LOW across his chest, three red lines through the yellow suit. He staggers back, touches the wound, looks at his hand. The raptor does a taunting little strut |
| 10 | The turn | **Rack focus: raptor's snapping jaws foreground → Dragon behind** | S1-f | jaws snarl in blurred foreground; focus snaps to the wounded Dragon stripping the torn jumpsuit to his waist, rolling his neck, sliding into stance and beckoning with two fingers. NOW it's personal |

### ACT III-B — THE DRAGON'S ANSWER → FALSE ENDING #1 (~0:40–0:52)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 11 | Bare-hand flurry | **Handheld shaky close, inside the fight** | S1-f + S2 | Jeet Kune Do straight-blast chain punches and trapping hands against snapping jaws, a backfist snaps the raptor's snout sideways, rain flying off every impact |
| 12 | THE FLYING KICK | **Top-down overhead (God's-eye)** | S3-b + both | Dragon launches — full flying side-kick connects square in the ribs, raptor skids across the wet ring through neon reflections, lanterns scatter |
| 13 | One inch | **Locked-off macro insert, extreme close-up** | S1-f | music ducks for a breath: his open palm settles ONE INCH from the staggered raptor's heaving chest scales, fingers slowly curl into a fist, a single raindrop rolls off his knuckle |
| 14 | THE ONE-INCH PUNCH | **Fist-level side profile, ultra-slow-mo (1000fps feel), speed-ramp** | S1-f + S2 | the fist travels one inch — a shockwave ring of mist explodes off the raptor's chest, rain hangs suspended, the raptor is LAUNCHED through the lantern ropes and lies still in the wreckage. *It looks over.* |

### ACT III-C — THE DEVASTATION → THE DRAGON GOES DOWN (~0:52–1:02)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 15 | It rises | **Reflection shot: action in a puddle, then tilt up** | S2 + S3-a | the Dragon turns his back to walk away — behind him the puddle reflection shows the raptor RISING out of the lantern wreckage; tilt up as it screams and springs onto the corner structure by the neon dragon sign |
| 16 | THE GUILLOTINE CONNECTS | **Dragon's POV — the dive comes AT CAMERA** | S2 | the raptor launches its claws-first death-dive straight at the lens, sickle claws leading, backlit by lightning — this time it HITS. Impact fills the frame, whiteout to black |
| 17 | Down | **Ground-level dutch: his face on the concrete in foreground, raptor blurred behind** | S1-f + S2 | the Dragon lies flat on the wet concrete, cheek against the ground, fresh cuts, rain falling on his face, eyes closed. In the blurred background the raptor struts a slow victory lap. **MUSIC DEAD — only rain and distant neon buzz** |

### ACT III-D — THE COMEBACK: KIP-UP + NUNCHAKU KO — THE TRUE FINALE (~1:02–1:20)
| # | Shot | UNIQUE ANGLE | Drive from | Prompt beats |
|---|---|---|---|---|
| 18 | THE KIP-UP | **Vertical crane boom-up, rising with him** | S1-f | his eyes SNAP open on the concrete — legs whip skyward and he somersaults up in the iconic no-hands kip-up, landing coiled in stance in one motion; the camera rises with his body. **Dead Meat slams back in the instant his feet plant** |
| 19 | The draw | **Vertical whip-tilt: belt → hands → eyes** | S1-f | whip-tilt up his body as the nunchaku drops from his belt into his palm, chain snapped taut between both fists at chest height, his eyes burning over the top of it, water shaking off the wood |
| 20 | THE CRAZY COMBO (wind-up) | **180° orbiting arc shot, speed-ramped** | S1-f | camera circles as the nunchaku blurs into the craziest combination: double figure-8s, behind-the-back pass, under-the-arm catch, neck wrap and re-draw, hand-to-hand switches — and he's WALKING TOWARD the raptor the entire time, rain spiraling off the chains |
| 21 | THE FLURRY | **Locked frontal medium, rhythmic strobe speed-ramps** | S1-f + S2 | blow after blow to the raptor's head — left, right, up under the jaw — every strike landing ON a beat of the track, the head snapping side to side, it can't bite through the blur, legs wobbling |
| 22 | THE CRACK | **Bullet-time frozen-moment 90° sweep** | S2 | the final overhead strike lands dead on the crown — time freezes mid-impact and the camera sweeps around it: a visible fracture splitting across the raptor's skull ridge, one pupil blown wide, rain suspended — then time releases and its legs buckle |
| 23 | KO + end card | **Slow push-in to hero freeze-frame, film-burn** | S1-f + S2 | the raptor face-plants into a puddle, OUT COLD, tongue lolling. The Dragon stands over it chest heaving, spins the nunchaku once, tucks it away, thumbs his nose with a flick. Freeze on that frame, film grain burns out → RAWR FIGHTS end card |

**Angle audit ✓** 1 drone push / 2 low track behind / 3 dutch ECU / 4 crash-zoom out / 5 locked
symmetrical wide / 6 over-shoulder / 7 worm's-eye / 8 whip-pan / 9 low lateral dolly slide /
10 rack focus / 11 handheld / 12 God's-eye / 13 locked macro insert / 14 fist-level slow-mo
profile / 15 puddle-reflection tilt-up / 16 POV dive-at-camera / 17 ground-level dutch
foreground-background / 18 crane boom-up / 19 vertical whip-tilt / 20 orbiting arc / 21 locked
frontal strobe-ramp / 22 bullet-time sweep / 23 slow push-in freeze. **23 shots, zero repeats.**

### Wardrobe + wound continuity 👕🩸
- Shots 1–9: full jumpsuit (**S1-e**), chest clean until shot 9.
- **Shot 9 CREATES the chest scratches** — the Pickpocket's rake is where the claw marks
  seen in the hero stills come from.
- Shots 10–23: jumpsuit stripped to the waist, scratched chest (**S1-f**); shot 17 adds
  fresh cuts from the Guillotine — he should look progressively wrecked by the finale.
- The nunchaku stays UNSEEN until shot 19. The kip-up → draw → storm is one continuous
  crescendo; don't tease the weapon earlier or the finale deflates. (Keep a waist sash on
  S1-f from shot 10 so shot 19's "drops from his belt" has somewhere to have come from.)

### ⚠️ OPEN ITEMS — resolve before generating (from the verification pass)
1. **Scratch continuity (biggest):** the locked hero still **S1-e already shows a claw-scratched
   chest**, but the plan says the chest is clean until the Pickpocket rakes it in shot 9 — so shots
   5, 6 and 8 (chest visible, pre-wound) would show the wound too early. **Recommended fix:** treat
   S1-e's marks as the Dragon's established look and make shot 9's "first blood" a *fresh, bright,
   bleeding* gash that reads distinctly against the older scars. (Alt: prompt shots 1–8 with the
   suit fully zipped / chest hidden — but that fights the locked still.)
2. **Angle near-repeat:** shot 20 (180° orbiting arc) and shot 22 (bullet-time 90° sweep) are both
   circling moves only one shot apart in the finale — the closest thing to a repeat in the episode.
   **Recommended fix:** make 22 a *low, tight micro-orbit locked on the skull* (or a straight snap-in
   freeze) so it doesn't echo 20's wide body-orbit.
3. **Physics vs. launches:** the "realistic physics" rule and the big launches (one-inch punch sends
   the raptor through the ropes; kick skids it across the ring) pull against each other at ~scale
   parity. **Recommended read:** "cinematic realism" — keep the launches but sell them with real
   weight (raptor tumbles/rolls with momentum, no floaty hang-time), not documentary realism.

---

## 🎵 MUSIC SYNC
- Track: `music/Dead_meat.mp3` (the series track — every episode)
- Higgsfield media_id `12c8ddb8-33cf-4b11-a7af-ea5454a300bb`
- Map the beat grid in the editor first; clips 4, 8, 12, 14 land on hits
  (shot 9's claw rake lands just OFF the beat — sneak attacks shouldn't be telegraphed by the music).
- Shot 13 (one-inch hold): quick half-second duck, then shot 14's punch lands on a big hit.
- **Shots 16–17 = FULL music dropout.** The Guillotine impact kills the track; over shot 17
  it's only rain and neon buzz. The silence makes the knockdown feel final.
- **Shot 18 (the kip-up) restarts Dead Meat the frame his feet plant** — the comeback and
  the track come back together. Shot 21's flurry lands strike-per-beat; shot 22's skull-crack
  is the track's single biggest hit; shot 23 rides the tail-out to the freeze.

## ⚙️ EXPORT
1920×1080 · 24 or 30fps · AI-disclosure ON · title: **RAWR FIGHTS Ep.1 — ENTER THE RAPTOR 🐉🦖**
