# Robot Framework + Pytest + CI (DevOps Test Automation Portfolio)

A small, practical portfolio repo that proves you can:
- write **Python tests with pytest** (unit + API integration)
- write **Robot Framework** API tests (RequestsLibrary)
- run everything in **CI (GitHub Actions)** with a green badge
- generate Robot reports (`log.html`, `report.html`) and upload them as CI artifacts

## Architecture (simple)
- A tiny **FastAPI** service runs locally (or in CI) on `http://127.0.0.1:8000`
- **pytest** runs:
  - unit tests against pure Python functions
  - live API tests against the running service
- **Robot Framework** runs API tests against the same service
- **GitHub Actions** starts the service, runs tests, uploads Robot reports

## Quick start (local)
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# run the API
make run
```

In another terminal:
```bash
make test
make robot
```

Robot reports will be in:
- `robot-reports/log.html`
- `robot-reports/report.html`

## Run everything like CI (local)
```bash
make ci-local
```

## Endpoints
- `GET /health` -> `{"status":"ok"}`
- `GET /calc/add?a=1&b=2` -> `{"a":1,"b":2,"sum":3}`
- `POST /items` -> creates an item and returns it with an id and computed tax

## Proof for recruiters (what to look at)
- `.github/workflows/ci.yml` (CI pipeline)
- `tests/` (pytest tests, including live API tests)
- `robot_tests/` (Robot Framework API tests)
- `Makefile` (simple dev workflow)

## Test Reports (Robot Framework)

Robot Framework generates HTML reports on every CI run and publishes them as GitHub Actions artifacts.

**How to access:**
1. Go to the **Actions** tab in this repository
2. Open the latest **CI** workflow run (green ✅)
3. Scroll to **Artifacts**
4. Download **robot-reports** and open:
   - `report.html`
   - `log.html`

This provides a reproducible, CI-generated proof of test execution (not just screenshots).
---

### Notes
- This repo is intentionally small and fast.
- Next upgrade (if you want): containerize + deploy to kind and run the same tests against the K8s Service.
