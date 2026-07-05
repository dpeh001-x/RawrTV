# RAWR FIGHTS — Episode 1 via Claude Code + Higgsfield API

Generate all 8 clips for "Downtown Demolition" (T-Rex vs Spinosaurus) with **consistent dinosaur designs**, straight from your machine.

## Why this works (when the chat connector didn't)
Claude Code runs locally — it has full network access and your API key, so it can submit each clip, poll until it's done, and download the MP4s. The consistency comes from **Soul mode**: every clip is generated from the *same two reference images*, so your T-Rex and Spino look identical shot to shot.

---

## SETUP (5 minutes)

### 1. Get your Higgsfield API key **and secret**
Log in at **[cloud.higgsfield.ai](https://cloud.higgsfield.ai/)** → **[API Keys](https://cloud.higgsfield.ai/api-keys)** → create a key. The official Higgsfield API issues a **key id + secret pair** — you need **both halves**, not just the id. Copy the secret when it's shown (usually only once).

### 2. Endpoint/auth defaults (already set to the official API)
These defaults are verified against the official Higgsfield Cloud API — you only need to override them if you use a gateway (Segmind / WaveSpeed / 302.AI / VideoGenAPI):
- **HF_API_BASE** — `https://platform.higgsfield.ai` (the official API host; `cloud.higgsfield.ai` is just the web dashboard)
- **HF_SUBMIT_PATH** — `/v1/image2video/dop`
- **HF_AUTH_HEADER** — `Authorization` (some gateways use `Ocp-Apim-Subscription-Key`)
- **HF_AUTH_PREFIX** — `Key ` → the header becomes `Authorization: Key KEY_ID:KEY_SECRET` (gateways often use `Bearer ` instead)
- reference-image field — `input_images` (some gateways call it `reference_image_urls`; override with `HF_REF_FIELD`)

### 3. Make your 2 hero stills, and host them
Generate one clean full-body still of each dino in Higgsfield (prompts below), approve them, then **upload them somewhere public** so the API can fetch them by URL (an S3/Cloudflare R2 bucket, imgur, or any image host). Most video APIs need image **URLs**, not local files.

Hero still prompts:
- **T-REX:** `Full-body shot of a Tyrannosaurus rex with dark olive-green scaly hide, faded amber underbelly, three deep parallel scars across its left shoulder, dull burnt-orange eyes, heavy muscular build, standing on a neon-lit city street at night, rain, cinematic, photorealistic, 9:16, no text`
- **SPINO:** `Full-body shot of a Spinosaurus with blue-grey hide and dark charcoal dorsal striping, a tall red-and-black sail, long narrow crocodilian snout, pale cream underbelly, standing on a neon-lit city street at night, rain, cinematic, photorealistic, 9:16, no text`

### 4. Set env vars
```bash
# Official Higgsfield auth needs BOTH the key id and the secret:
export HIGGSFIELD_API_KEY="your-key-id"
export HIGGSFIELD_API_SECRET="your-key-secret"     # the script joins them as KEY_ID:KEY_SECRET
# (or provide the pair in one var: export HIGGSFIELD_API_KEY="keyid:keysecret")

export TREX_REF_URL="https://your-host/trex_ref.png"
export SPINO_REF_URL="https://your-host/spino_ref.png"
# only if you use a gateway whose docs differ from the official defaults:
# export HF_API_BASE="..."; export HF_SUBMIT_PATH="..."; export HF_AUTH_HEADER="..."; export HF_AUTH_PREFIX="Bearer "
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
- **You need Higgsfield credits on the account.** With a valid key but an empty balance the API returns `403 {"detail":"Not enough credits"}` and nothing generates. Top up at [cloud.higgsfield.ai](https://cloud.higgsfield.ai/) first (~250–350 credits per fully-loaded episode).
- 8 clips × a few retries on the ⭐ hero shots (V1/V4/V7/V8) — budget accordingly; the `dop-lite` model on the non-hero clips keeps it cheap.
- Start with `--dry-run` to confirm the payload, then `--only V1` to confirm your endpoint/auth works before spending on all 8.
- Keep your API key **and secret** in env vars only — never commit them.

### Verified API contract (official Higgsfield Cloud)
Confirmed live against the service, so the script's defaults already match:
```
POST https://platform.higgsfield.ai/v1/image2video/dop
Authorization: Key KEY_ID:KEY_SECRET
Content-Type: application/json

{"params": {
   "prompt": "<character-locked prompt>",
   "model":  "dop-turbo" | "dop-lite" | "dop-preview",
   "input_images": [{"type": "image_url", "image_url": "https://.../hero.png"}]
}}
```
`input_images` is required (this is an image-to-video model). The success-response
shape (job id + status URL) still needs confirming on the first funded run — the
script prints the raw response if it can't find them so you can adjust.

*RAWR FIGHTS · RESULTS ARE REAL ✓*
