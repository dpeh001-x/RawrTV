# RAWR FIGHTS — Episode 1 via Claude Code + Higgsfield API

Generate all 8 clips for "Downtown Demolition" (T-Rex vs Spinosaurus) with **consistent dinosaur designs**, straight from your machine.

## Why this works (when the chat connector didn't)
Claude Code runs locally — it has full network access and your API key, so it can submit each clip, poll until it's done, and download the MP4s. The consistency comes from **Soul mode**: every clip is generated from the *same two reference images*, so your T-Rex and Spino look identical shot to shot.

---

## SETUP (5 minutes)

### 1. Get your Higgsfield API key
Log in to Higgsfield → find the **API / Developer** section (Higgsfield Cloud, or your gateway dashboard) → create an API key.

### 2. ⚠️ Confirm 4 values from your API docs
The exact endpoint differs between the official Higgsfield Cloud API and gateways (Segmind / WaveSpeed / 302.AI / VideoGenAPI). Open your dashboard's API docs and check these, then set any that differ as env vars:
- **HF_API_BASE** — base URL (e.g. `https://cloud.higgsfield.ai`)
- **HF_SUBMIT_PATH** — the image-to-video submit path (e.g. `/v1/image2video`)
- **HF_AUTH_HEADER** — usually `Authorization`; some gateways use `Ocp-Apim-Subscription-Key`
- **HF_AUTH_PREFIX** — usually `Bearer ` (with the space); some use empty `""`

Also confirm the **model names** (`HF_MODEL_HERO`, `HF_MODEL_STD`) and the reference-image field name — this script uses `reference_image_urls`; some APIs call it `input_images`. If yours differs, tell Claude Code "change reference_image_urls to <name>" and it'll edit the script.

### 3. Make your 2 hero stills, and host them
Generate one clean full-body still of each dino in Higgsfield (prompts below), approve them, then **upload them somewhere public** so the API can fetch them by URL (an S3/Cloudflare R2 bucket, imgur, or any image host). Most video APIs need image **URLs**, not local files.

Hero still prompts:
- **T-REX:** `Full-body shot of a Tyrannosaurus rex with dark olive-green scaly hide, faded amber underbelly, three deep parallel scars across its left shoulder, dull burnt-orange eyes, heavy muscular build, standing on a neon-lit city street at night, rain, cinematic, photorealistic, 9:16, no text`
- **SPINO:** `Full-body shot of a Spinosaurus with blue-grey hide and dark charcoal dorsal striping, a tall red-and-black sail, long narrow crocodilian snout, pale cream underbelly, standing on a neon-lit city street at night, rain, cinematic, photorealistic, 9:16, no text`

### 4. Set env vars
```bash
export HIGGSFIELD_API_KEY="sk-..."
export TREX_REF_URL="https://your-host/trex_ref.png"
export SPINO_REF_URL="https://your-host/spino_ref.png"
# only if your docs differ from defaults:
# export HF_API_BASE="..."; export HF_SUBMIT_PATH="..."; export HF_AUTH_HEADER="..."; export HF_AUTH_PREFIX=""
```

---

## RUN
```bash
python generate_episode1.py
```
It generates V1–V8, polls each to completion, and saves them to `./output/` plus a `manifest.json`. Then take those into your **CapCut build sheet** (overlays, health bars, VO all ready).

### Preview & single-clip flags (spend nothing until you're ready)
```bash
python generate_episode1.py --dry-run        # print the exact payloads/prompts — NO API call, NO cost
python generate_episode1.py --dry-run --only V1   # preview just one clip
python generate_episode1.py --only V1        # generate a single clip (recommended first run)
python generate_episode1.py --only V1,V4,V7  # generate a subset
python generate_episode1.py --list           # list all clip ids + summaries
```
`--dry-run` writes the full payloads to `output/dry_run_preview.json` and prints the endpoint,
auth header, ref-field name, and whether your key/refs are set — so you can confirm your provider
config is correct **before** spending any credits.

### Let Claude Code drive it
Easiest path: open this folder in Claude Code and say:
> "Read the README, help me set my env vars, then run generate_episode1.py. If the API returns an error about a field name or endpoint, fix the script to match Higgsfield's response and retry."

That way Claude Code adapts the payload/response keys to your exact API on the fly — which is the one thing that varies by provider.

---

## COST / SAFETY
- 8 clips × a few retries on the ⭐ hero shots (V1/V4/V7/V8) — budget accordingly; `lite` model on the non-hero clips keeps it cheap.
- Start with `--dry-run` to confirm the payload, then `--only V1` to confirm your endpoint/auth works before spending on all 8.
- Keep your API key in env vars only — never commit it.

*RAWR FIGHTS · RESULTS ARE REAL ✓*
