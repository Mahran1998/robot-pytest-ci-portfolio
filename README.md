[![CI](https://github.com/Mahran1998/robot-pytest-ci-portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/Mahran1998/robot-pytest-ci-portfolio/actions/workflows/ci.yml)

 small test automation portfolio project: **FastAPI** test target + **pytest** (unit + integration) + **Robot Framework** API tests, executed in **GitHub Actions CI** with downloadable HTML reports.

 **CI workflow (proof):** https://github.com/Mahran1998/robot-pytest-ci-portfolio/actions/workflows/ci.yml

## Project Highlights
- **FastAPI** demo service used as a test target (`/health`, `/calc/add`, `/items`)
- **pytest** suite: unit tests + live API integration tests (runs against the running service)
- **Robot Framework** API suite using **RequestsLibrary** (HTML `report.html` / `log.html`)
- **GitHub Actions CI** runs on every push/PR and uploads Robot reports as **artifacts**
- Local dev workflow via **Makefile** (`make ci-local`) for one-command reproduction


## Skills Demonstrated
- API testing (pytest + Robot Framework RequestsLibrary)
- Test types: unit + integration (live API tests)
- CI automation (GitHub Actions)
- Reproducible CLI workflow (Makefile: `make ci-local`)
- Debugging real test/CI issues (imports, expected HTTP errors, rounding)


## Architecture (simple)
- A **FastAPI** service runs locally (or in CI) on `http://127.0.0.1:8000`
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

## Key Files
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

---

