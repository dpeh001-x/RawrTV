#!/usr/bin/env python3
"""
RAWR FIGHTS — Episode 1 generator (Higgsfield API)
Generates all 8 clips for "Downtown Demolition" (T-Rex vs Spinosaurus),
using reference images (Soul mode) so the dinosaur designs stay CONSISTENT.

Run inside Claude Code:  python generate_episode1.py
It will: submit each clip -> poll until done -> download V1..V8.mp4 into ./output/

Handy flags (no API calls / no cost until you drop --dry-run):
  python generate_episode1.py --dry-run        # print the exact payloads, spend nothing
  python generate_episode1.py --only V1        # generate a single clip (README's "test V1 first")
  python generate_episode1.py --only V1,V4,V7  # generate a subset
  python generate_episode1.py --list           # list clip ids + one-line summaries
"""

import os, time, json, sys, pathlib, urllib.request, argparse

# ============================================================
# CONFIG  —  ⚠️ VERIFY THESE AGAINST YOUR LIVE HIGGSFIELD DOCS
# The exact base URL / paths / model names / auth header differ depending on
# whether you use the OFFICIAL Higgsfield Cloud API or a gateway (Segmind,
# WaveSpeed, 302.AI, VideoGenAPI). Open your dashboard's API docs and confirm
# the values below. Everything else in this script is provider-agnostic.
# ============================================================
API_BASE      = os.environ.get("HF_API_BASE", "https://platform.higgsfield.ai")  # confirmed official API host
SUBMIT_PATH   = os.environ.get("HF_SUBMIT_PATH", "/v1/image2video/dop")           # confirmed DoP image-to-video route
AUTH_HEADER   = os.environ.get("HF_AUTH_HEADER", "Authorization")                # gateways may use 'Ocp-Apim-Subscription-Key'
AUTH_PREFIX   = os.environ.get("HF_AUTH_PREFIX", "Key ")                          # official = 'Key ' + 'KEY_ID:KEY_SECRET' (gateways often use 'Bearer ')
MODEL_HERO    = os.environ.get("HF_MODEL_HERO", "dop-turbo")  # DoP model for the ⭐ hero shots (enum: dop-lite|dop-preview|dop-turbo)
MODEL_STD     = os.environ.get("HF_MODEL_STD",  "dop-lite")   # cheaper DoP model for the rest
REF_FIELD     = os.environ.get("HF_REF_FIELD", "input_images")  # official field name (some gateways use 'reference_image_urls')
CLIP_SECONDS  = int(os.environ.get("HF_SECONDS", "5"))

# Official Higgsfield auth is  Authorization: Key KEY_ID:KEY_SECRET  — it needs
# BOTH halves. Provide them either as HIGGSFIELD_API_KEY="keyid:keysecret", or
# split across HIGGSFIELD_API_KEY + HIGGSFIELD_API_SECRET and we join them here.
API_KEY       = os.environ.get("HIGGSFIELD_API_KEY")
API_SECRET    = os.environ.get("HIGGSFIELD_API_SECRET") or os.environ.get("HF_API_SECRET")
if API_KEY and API_SECRET and ":" not in API_KEY:
    API_KEY = f"{API_KEY}:{API_SECRET}"

# Your two approved hero-still URLs (see README — these MUST be public URLs).
TREX_REF  = os.environ.get("TREX_REF_URL",  "")   # e.g. https://.../trex_ref.png
SPINO_REF = os.environ.get("SPINO_REF_URL", "")

# Fixed seeds per dino = extra consistency across clips.
TREX_SEED, SPINO_SEED = 70111, 70222

OUT = pathlib.Path("output"); OUT.mkdir(exist_ok=True)

# ============================================================
# CHARACTER-LOCKED PROMPTS  (identical design tokens every clip)
# ============================================================
TREX  = ("a Tyrannosaurus rex with dark olive-green scaly hide, a faded amber "
         "underbelly, three deep parallel scars across its left shoulder, dull "
         "burnt-orange eyes, heavy muscular build, weathered cracked skin texture")
SPINO = ("a Spinosaurus with blue-grey hide and dark charcoal dorsal striping, a "
         "tall red-and-black sail, a long narrow crocodilian snout, a pale cream "
         "underbelly, lean athletic build")
SCENE = ("night, rain-soaked neon-lit downtown city, kaiju scale towering over "
         "skyscrapers, cars and buses in frame for scale, cinematic blockbuster "
         "lighting, photorealistic, vertical 9:16, no text")

CLIPS = [
    dict(id="V1", hero=True,  refs=[TREX_REF],            seed=TREX_SEED,
         prompt=f"{TREX} erupts up through a city street, cars and asphalt flung aside, spotlights and pyro flares, low hero angle, rain and steam. {SCENE}"),
    dict(id="V2", hero=False, refs=[SPINO_REF],           seed=SPINO_SEED,
         prompt=f"{SPINO} smashes head-first through a glass skyscraper, shards raining down, sail lit by neon and pyro, low hero angle. {SCENE}"),
    dict(id="V3", hero=False, refs=[TREX_REF, SPINO_REF], seed=TREX_SEED,
         prompt=f"{TREX} and {SPINO} face off across a flooded neon street, rain pouring, headlights and steam, tense standoff, low wide angle. {SCENE}"),
    dict(id="V4", hero=True,  refs=[TREX_REF, SPINO_REF], seed=TREX_SEED,
         prompt=f"{TREX} charges and slams {SPINO} through an office building, glass and concrete exploding outward, dust cloud, dynamic handheld. {SCENE}"),
    dict(id="V5", hero=False, refs=[SPINO_REF, TREX_REF], seed=SPINO_SEED,
         prompt=f"{SPINO} swings its long tail and knocks a row of cars and a bus into {TREX}, debris flying, neon reflections, motion blur. {SCENE}"),
    dict(id="V6", hero=False, refs=[SPINO_REF, TREX_REF], seed=SPINO_SEED,
         prompt=f"{SPINO} pins {TREX} against a skyscraper with its clawed forelimbs, snapping its long jaws, sparks and shattering windows, dramatic low angle. {SCENE}"),
    dict(id="V7", hero=True,  refs=[TREX_REF, SPINO_REF], seed=TREX_SEED,
         prompt=f"{TREX} drives {SPINO} backward through a giant neon billboard, sparks and electrical arcs bursting, rain, epic scale. {SCENE}"),
    dict(id="V8", hero=True,  refs=[TREX_REF, SPINO_REF], seed=TREX_SEED,
         prompt=f"slow-motion: {TREX} clamps its jaws onto the neck of {SPINO} and slams it onto the street, pavement cratering, dust blast, dramatic slow-mo. {SCENE}"),
]

# ============================================================
# API HELPERS  (thin wrappers; adjust payload keys to match your docs)
# ============================================================
def _headers():
    return {"Content-Type": "application/json",
            AUTH_HEADER: f"{AUTH_PREFIX}{API_KEY}"}

def _post(path, body):
    req = urllib.request.Request(API_BASE + path,
                                 data=json.dumps(body).encode(),
                                 headers=_headers(), method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

def _get(url):
    req = urllib.request.Request(url, headers=_headers(), method="GET")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

def build_body(clip):
    """Assemble the submit payload for a clip (pure — no network I/O, no cost).

    Verified schema for the official Higgsfield DoP image2video endpoint:
        {"params": {"prompt": str,
                    "model": "dop-lite"|"dop-preview"|"dop-turbo",
                    "input_images": [{"type": "image_url", "image_url": <url>}, ...]}}
    input_images is REQUIRED — this is an image-to-video model, so every clip
    needs at least one reference still. Unknown extra params are ignored by the
    API, so consistency is carried by the reference images (Soul mode), not seed.
    """
    refs = [u for u in clip["refs"] if u]           # drop empties
    params = {
        "prompt": clip["prompt"],
        "model": MODEL_HERO if clip["hero"] else MODEL_STD,
        REF_FIELD: [{"type": "image_url", "image_url": u} for u in refs],
    }
    if clip.get("seed") is not None:
        params["seed"] = clip["seed"]   # accepted-or-ignored; harmless if unsupported
    return {"params": params}

def submit(clip):
    resp = _post(SUBMIT_PATH, build_body(clip))
    # NOTE: the SUCCESS response shape (job id + status/poll url) was not yet
    # observable — the test account has no credits, so no job has completed.
    # These getters are best-effort; confirm the keys on the first funded run
    # (print `resp` if id/poll come back None) and adjust here if needed.
    rid = resp.get("id") or resp.get("request_id") or resp.get("job_id")
    poll = (resp.get("polling_url") or resp.get("status_url")
            or (f"{API_BASE}/v1/job-sets/{rid}" if rid else None))
    return rid, poll

def poll(url, every=6, timeout=900):
    t0 = time.time()
    while time.time() - t0 < timeout:
        d = _get(url)
        st = (d.get("status") or "").upper()
        if st in ("COMPLETED", "SUCCEEDED", "DONE"):
            out = d.get("output", {})
            urls = out.get("media_url") or out.get("media_urls") or [out.get("url")]
            return urls[0]
        if st in ("ERROR", "FAILED"):
            raise RuntimeError(f"generation failed: {json.dumps(d)[:400]}")
        print(f"    …{st or 'PENDING'} ({int(time.time()-t0)}s)")
        time.sleep(every)
    raise TimeoutError("timed out waiting for clip")

def download(url, path):
    urllib.request.urlretrieve(url, path)

# ============================================================
# DRY RUN  (validate payloads/prompts without any API call or cost)
# ============================================================
def dry_run(clips):
    print("🧪 DRY RUN — no API calls, no cost. Previewing payloads:\n")
    preview = []
    for clip in clips:
        body = build_body(clip)
        params = body["params"]
        n_refs = len(params.get(REF_FIELD, []))
        print(f"▶ {clip['id']}  model={params['model']:<10} seed={params.get('seed')}  refs={n_refs}")
        print(f"    prompt: {clip['prompt'][:110]}…")
        preview.append({"id": clip["id"], "endpoint": API_BASE + SUBMIT_PATH, "body": body})
    (OUT / "dry_run_preview.json").write_text(json.dumps(preview, indent=2))
    print(f"\n📝 Full payloads written to {OUT/'dry_run_preview.json'}")
    print(f"   Endpoint    : {API_BASE + SUBMIT_PATH}")
    print(f"   Auth header : {AUTH_HEADER}: {AUTH_PREFIX}<key>")
    print(f"   Ref field   : {REF_FIELD}")
    print(f"   API key set : {'yes' if API_KEY else 'NO — export HIGGSFIELD_API_KEY'}")
    if API_KEY and AUTH_PREFIX.strip() == "Key" and ":" not in API_KEY:
        print("\n⚠️  Your key has no ':' — official Higgsfield auth needs KEY_ID:KEY_SECRET.")
        print("    Add the secret: export HIGGSFIELD_API_SECRET=... (or set HIGGSFIELD_API_KEY='id:secret').")
    if not (TREX_REF and SPINO_REF):
        print("\n⚠️  TREX_REF_URL / SPINO_REF_URL not set — clips will lose Soul-mode consistency.")
    print("\nWhen this looks right, drop --dry-run to actually generate.")

# ============================================================
# MAIN
# ============================================================
def run(clips):
    if not API_KEY:
        sys.exit("❌ Set HIGGSFIELD_API_KEY (see README). Or preview safely with: --dry-run")
    if AUTH_PREFIX.strip() == "Key" and ":" not in (API_KEY or ""):
        sys.exit("❌ Official Higgsfield auth needs KEY_ID:KEY_SECRET — set HIGGSFIELD_API_SECRET too (see README).")
    # image2video REQUIRES a source image per clip; without refs there is nothing to animate.
    if not (TREX_REF and SPINO_REF):
        sys.exit("❌ TREX_REF_URL / SPINO_REF_URL are required — image2video needs a reference still per clip.\n"
                 "   Host your two hero stills publicly and export their URLs (see README). Preview with --dry-run.")

    manifest = []
    for clip in clips:
        print(f"▶ {clip['id']} — submitting…")
        try:
            if not build_body(clip)["params"][REF_FIELD]:
                raise RuntimeError("no reference image URL available for this clip")
            rid, poll_url = submit(clip)
            print(f"    id={rid}")
            media = poll(poll_url)
            dest = OUT / f"{clip['id']}.mp4"
            download(media, dest)
            print(f"  ✅ saved {dest}\n")
            manifest.append({"id": clip["id"], "file": str(dest), "url": media})
        except Exception as e:
            print(f"  ❌ {clip['id']} failed: {e}\n")
            manifest.append({"id": clip["id"], "error": str(e)})
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2))
    ok = sum(1 for m in manifest if "file" in m)
    print(f"Done. {ok}/{len(clips)} clips in ./output/  → now assemble in CapCut.")

def select(only):
    if not only:
        return CLIPS
    wanted = {s.strip().upper() for s in only.split(",") if s.strip()}
    valid = {c["id"].upper() for c in CLIPS}
    unknown = wanted - valid
    if unknown:
        sys.exit(f"❌ Unknown clip id(s): {', '.join(sorted(unknown))}. Valid: {', '.join(c['id'] for c in CLIPS)}")
    return [c for c in CLIPS if c["id"].upper() in wanted]

def main():
    ap = argparse.ArgumentParser(description="Generate RAWR FIGHTS Episode 1 clips via the Higgsfield API.")
    ap.add_argument("--dry-run", action="store_true", help="Preview payloads/prompts without calling the API (no cost).")
    ap.add_argument("--only", metavar="IDS", help="Comma-separated clip ids to run, e.g. V1 or V1,V4,V7.")
    ap.add_argument("--list", action="store_true", help="List clip ids and one-line summaries, then exit.")
    args = ap.parse_args()

    if args.list:
        for c in CLIPS:
            tag = "⭐hero" if c["hero"] else "  std"
            print(f"{c['id']}  {tag}  {c['prompt'][:80]}…")
        return

    clips = select(args.only)
    if args.dry_run:
        dry_run(clips)
    else:
        run(clips)

if __name__ == "__main__":
    main()
