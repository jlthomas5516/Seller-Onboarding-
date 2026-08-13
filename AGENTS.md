# AGENTS.md

## Cursor Cloud specific instructions

### What this repo is
A single, self-contained **static site** — an internal CipherHealth "AE Onboarding Hub".
There is **no build system, package manager, or backend**:

- `index.html` — the entire application (inline CSS + vanilla JS; no bundler). Interactive
  features live in the `<script>` block at the bottom: a proof filter, an ROI calculator, and
  scroll-spy side navigation.
- `docs/AI-Contract-Reconciliation-Project-Plan.md` — supporting markdown doc.

There are no dependencies to install, no lint config, and no automated test suite. The only
external runtime references are Google Fonts loaded from a CDN (require network; the page still
works and is fully readable without them).

### Running it (development)
Serve the repo root over HTTP and open `index.html`. Any static file server works; the simplest
with no install is Python's built-in server:

```bash
python3 -m http.server 8000   # then open http://localhost:8000/
```

Do **not** just `open` the file over `file://` if you want the fonts/CDN behavior to match; serving
over HTTP is closer to how it is hosted. Editing `index.html` is picked up on a plain browser
refresh — there is no hot reload and no build step to re-run.

### Verifying core functionality
This is a static page, so "testing" means exercising the JS in a browser. Headless Chrome
(`google-chrome`) is available. Note: launch it with `--headless=new --no-sandbox
--disable-gpu --disable-dev-shm-usage` and a fresh `--user-data-dir`; the DevTools port binds to
`127.0.0.1` (use `http://127.0.0.1:9222`, not `localhost`), and the `dbus`/`UPower` errors in the
logs are harmless. Sanity checks: the ROI calculator (`#m7`) recomputes "Estimated annual savings"
when the four inputs change, and the proof filter buttons (`.fbtn`) show/hide `#prooflist .proof`
items.

### Lint / test / build
None exist. There is nothing to build; do not add a toolchain unless explicitly asked.
