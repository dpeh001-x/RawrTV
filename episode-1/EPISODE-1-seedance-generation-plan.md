# RAWR FIGHTS — Episode 1 "Downtown Demolition" · Seedance Generation Plan

Living plan for generating the 8 vertical clips via the **Higgsfield MCP connector**
(Seedance 2.0 image-to-video). This file is the source of truth so work can resume
across sessions — if the connector drops, reconnect it in a fresh session and follow
this sheet exactly.

---

## Account & budget
- **Workspace:** private Pro workspace `ac717e56-898e-4e2c-a36b-7913d3d8a803` (owner)
- **Plan:** Pro
- **Credits:** started at **574**; ~**27 spent** (reference stills + V1 test) → **~547 remaining**

## Locked creative rules (apply to EVERY clip)
- **No humans.** Absolutely no people/crowds anywhere in frame.
- **Scale:** street-level city scale (kaiju was tried and dropped).
- **Dino size ratio (must be correct):** the **Spinosaurus is the longer & taller
  animal** (its tall sail raises it above the T-Rex); the **Tyrannosaurus rex is
  shorter but noticeably bulkier / more heavily muscled**.
- **Look:** night, heavy rain, neon-lit downtown, wet reflective asphalt, photorealistic,
  hyper-detailed, cinematic blockbuster lighting, vertical 9:16.
- **Story beat:** T-Rex vs Spinosaurus brawl; T-Rex wins the finale (V8).

## Generation settings (per clip)
| Setting | Value |
|---|---|
| Model | **Seedance 2.0** (`seedance_2_0`) |
| Aspect ratio | 9:16 |
| Duration | 5s |
| Resolution / mode | 720p / std (~22.5 cr each) |
| Native audio | **off** (VO/SFX added in CapCut) |
| Genre hint | epic / action |
| Consistency | pass the two approved stills as **image_references** |

## Approved reference stills (v2 — Nano Banana Pro, 2K)
| Dino | Job ID | URL |
|---|---|---|
| T-Rex | `2a6c7b99-c302-4b57-9b28-f5dd4e234408` | https://d8j0ntlcm91z4.cloudfront.net/user_3G4EKe8Vr9E2YlQd0Ypng9D9FlM/hf_20260705_075839_2a6c7b99-c302-4b57-9b28-f5dd4e234408.png |
| Spino | `44d098c1-e9aa-41a3-bae5-a56a79f23f06` | https://d8j0ntlcm91z4.cloudfront.net/user_3G4EKe8Vr9E2YlQd0Ypng9D9FlM/hf_20260705_075841_44d098c1-e9aa-41a3-bae5-a56a79f23f06.png |

**Character tokens (keep identical every clip):**
- **T-REX:** dark olive-green scaly hide, faded amber underbelly, three deep parallel red
  scars across its left shoulder, dull burnt-orange eyes, stocky heavily-muscled bulky
  build, deep powerful jaws, weathered cracked wet skin.
- **SPINO:** blue-grey hide with dark charcoal dorsal striping, a tall red-and-black sail,
  a long narrow crocodilian snout, a pale cream underbelly, a long lean athletic build.

---

## Clip list & status
| # | Shot | Refs | Status |
|---|---|---|---|
| V1 | T-Rex reveal, rears & roars, low hero angle | T-Rex | ✅ DONE |
| V2 | Spino smashes through a glass skyscraper | Spino | ⬜ to generate |
| V3 | Standoff across a flooded neon street | Both | ⬜ to generate |
| V4 | T-Rex charges & slams Spino through an office tower | Both | ⬜ to generate |
| V5 | Spino tail-sweeps cars/bus into T-Rex | Both | ⬜ to generate |
| V6 | Spino pins T-Rex against a skyscraper | Both | ⬜ to generate |
| V7 | T-Rex drives Spino through a neon billboard | Both | ⬜ to generate |
| V8 | Finale slow-mo: T-Rex clamps Spino's neck, slams it down | Both | ⬜ to generate |

**V1 output (approved):**
https://d8j0ntlcm91z4.cloudfront.net/user_3G4EKe8Vr9E2YlQd0Ypng9D9FlM/hf_20260705_080540_7785db68-3542-4dc4-8b12-358597f270b0.mp4

---

## Prompts (copy verbatim)

### V1 — T-Rex reveal ✅ (already generated)
> Cinematic blockbuster shot. A colossal Tyrannosaurus rex with dark olive-green scaly hide, faded amber underbelly, three deep parallel red scars across its left shoulder, dull burnt-orange eyes, heavy muscular build and weathered cracked wet skin, rears up and roars with jaws wide over a rain-soaked neon-lit downtown city at night. Extreme low hero angle, tiny cars and buses far below on the flooded street for scale, searchlights and pyro flares, sheets of rain and steam, glistening wet scales, dramatic blockbuster lighting, photorealistic, hyper-detailed, vertical 9:16. Absolutely no people, no humans, no crowds anywhere in frame.

### V2 — Spino reveal · refs: Spino
> Cinematic blockbuster shot. A Spinosaurus with blue-grey hide, dark charcoal dorsal striping, a tall red-and-black sail, long narrow crocodilian snout and pale cream underbelly, smashes head-first through a glass skyscraper facade on a rain-soaked neon-lit downtown street at night, glass shards raining down, sail lit by neon and pyro flares, low hero angle, wet reflective asphalt, photorealistic, hyper-detailed, vertical 9:16. Absolutely no people, no humans.

### V3 — Standoff · refs: T-Rex + Spino
> Cinematic wide shot. A Tyrannosaurus rex (dark olive-green hide, amber underbelly, three red scars on its left shoulder, stocky heavily-muscled build) and a Spinosaurus (blue-grey hide, tall red-and-black sail, long crocodilian snout) face off across a flooded neon street in heavy rain, headlights and steam between them, tense standoff. The Spinosaurus is clearly longer and taller with its sail raised above the T-rex, while the T-rex is shorter but noticeably bulkier and more heavily muscled. Night, neon downtown, photorealistic, vertical 9:16. No people, no humans.

### V4 — T-Rex bodyslam · refs: T-Rex + Spino
> Cinematic handheld action. The stocky bulky Tyrannosaurus rex charges and slams the taller long-sailed Spinosaurus through an office building, glass and concrete exploding outward, dust cloud, rain, neon light. The Spinosaurus is the longer/taller animal, the T-rex shorter but heavier and more muscular. Night downtown, photorealistic, hyper-detailed, vertical 9:16. No people, no humans.

### V5 — Spino tail sweep · refs: T-Rex + Spino
> Cinematic action, motion blur. The long-tailed Spinosaurus swings its tail and knocks a row of cars and a bus into the Tyrannosaurus rex, debris flying, neon reflections on wet asphalt, rain. Spinosaurus longer and taller with its sail; T-rex shorter but bulkier. Night downtown, photorealistic, vertical 9:16. No people, no humans.

### V6 — Spino pins T-Rex · refs: T-Rex + Spino
> Dramatic low angle. The taller Spinosaurus pins the bulkier Tyrannosaurus rex against a skyscraper with its clawed forelimbs, snapping its long crocodilian jaws, sparks and shattering windows, rain and neon. Spinosaurus is the larger, taller animal; T-rex shorter but more heavily muscled. Night downtown, photorealistic, vertical 9:16. No people, no humans.

### V7 — T-Rex drives Spino back · refs: T-Rex + Spino
> Cinematic epic shot. The Tyrannosaurus rex drives the Spinosaurus backward through a giant neon billboard, sparks and electrical arcs bursting, rain, steam. Spinosaurus longer and taller with its red-and-black sail; T-rex shorter but bulkier and stronger. Night downtown, photorealistic, hyper-detailed, vertical 9:16. No people, no humans.

### V8 — Finale (slow-mo) · refs: T-Rex + Spino
> Slow-motion cinematic finish. The bulky Tyrannosaurus rex clamps its powerful jaws onto the neck of the taller long-sailed Spinosaurus and slams it down onto the street, pavement cratering, dust blast, rain, neon glow. Spinosaurus is the longer/taller animal, T-rex shorter but heavier and dominant. Night downtown, photorealistic, hyper-detailed, vertical 9:16. No people, no humans.

---

## Resume checklist (new session)
1. Confirm Higgsfield connector is attached (its `mcp__Higgsfield__*` tools are available).
2. Check balance.
3. Generate **V2** first, review frames (on-model Spino? no humans?), then run **V3–V8**.
4. Download each MP4, then assemble in CapCut per `CAPCUT-BUILD-SHEET-downtown-demolition.md`.
5. Optionally upscale favorite clips with the dedicated upscaler (cheap) instead of
   generating everything at 1080p.
