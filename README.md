<div align="center">

# ⚡ AQARION-Fastapi

A minimal FastAPI service scaffold for exact partition computation, numerical asymptotic comparison, and the AQARION research stack.

[![Tests](https://github.com/quantarion369-arch/Aqarion-Fastapi/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/quantarion369-arch/Aqarion-Fastapi/actions/workflows/test.yml)
[![Lint and Types](https://github.com/quantarion369-arch/Aqarion-Fastapi/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/quantarion369-arch/Aqarion-Fastapi/actions/workflows/lint.yml)
[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Quick Start](#quick-start) · [Endpoints](#endpoints) · [Verification](#verification) · [Project Layout](#project-layout) · [Research Boundaries](#research-boundaries)

</div>

---

## Overview

AQARION-Fastapi is a service layer for selected computations in the AQARION research stack.

It provides:

- Core service endpoints: a root response, health check, and in-memory item operations.
- Exact integer partitions: computation of the partition number (p(n)).
- Asymptotic comparison: the leading Hardy–Ramanujan approximation and input-specific relative error.
- Automated tests, Ruff linting, and mypy type checks.

```text
HTTP request
     |
     v
FastAPI application
     |
     +-- Core service --------> Root / health / in-memory items
     |
     +-- Partition router ----> Exact integer partition computation
     |
     +-- Asymptotic router ----> Exact value + approximation + error
```

This is a research/API scaffold, not a complete production deployment.
It has no database, authentication layer, or Docker deployment configuration.

Application outputs are not independent mathematical proofs, formal verification
certificates, or publication approvals.

## Quick Start

Prerequisites: Python 3.11+ and pip. GitHub Actions currently checks the project on Python 3.12.

```bash
git clone [https://github.com/quantarion369-arch/Aqarion-Fastapi.git](https://github.com/quantarion369-arch/Aqarion-Fastapi.git)
cd Aqarion-Fastapi

python3 -m venv .venv
source .venv/bin/activate

pip install -e '.[dev]'

uvicorn myfastapi.main:app --reload
```

On Windows, activate the environment with:

```powershell
.venvScriptsActivate.ps1
```

Development URLs:

| Resource | URL |
|---|---|
| API | http://127.0.0.1:8000 |
| Interactive documentation | http://127.0.0.1:8000/docs |
| OpenAPI schema | http://127.0.0.1:8000/openapi.json |

The reload-enabled server is for development.

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/` | Hello message |
| GET | `/health` | Health check |
| GET | `/items/` | List in-memory items |
| POST | `/items/` | Create an item |
| GET | `/items/{item_id}` | Fetch an item by ID |
| GET | `/partition/{n}` | Return the exact partition number |
| GET | `/asymptotic/{n}` | Compare the exact partition value with the leading approximation |

Example item request body:

```json
{
  "id": 1,
  "name": "apple"
}
```

### Exact integer partitions

`GET /partition/{n}` accepts integer inputs from `0` through `1000`, inclusive.

Negative integers and integers above the supported limit receive HTTP 400 responses.

Example:

```bash
curl http://127.0.0.1:8000/partition/10
```

Response:

```json
{
  "n": 10,
  "p_n": 42
}
```

Upper-boundary response:

```bash
curl http://127.0.0.1:8000/partition/1000
```

```json
{
  "n": 1000,
  "p_n": 24061467864032622473692149727991
}
```

The implementation uses an iterative, incrementally cached version of Euler's
pentagonal-number recurrence. Cached values are stored as Python integers,
and cache extension is protected by a lock.

The cache belongs to the running Python process. It is not persistent storage.

Two distinct files serve different roles:

| File | Role |
|---|---|
| `myfastapi/partition.py` | Computes exact partition values |
| `myfastapi/routers/partition.py` | Defines the HTTP endpoint and its input boundary |

### Hardy–Ramanujan comparison

`GET /asymptotic/{n}` accepts integer inputs from `1` through `1000`, inclusive.

The implemented leading approximation is:

[
p(n) approx
\frac{exp!left(pisqrt{2n/3}
ight)}
     {4sqrt{3},n}.
]

Example:

```bash
curl http://127.0.0.1:8000/asymptotic/100
```

Response fields:

| Field | Meaning |
|---|---|
| `n` | Requested positive integer |
| `exact` | Exact partition value |
| `approximation` | Floating-point leading-order approximation |
| `relative_error` | Absolute approximation error divided by the exact value |

The reported error describes the requested input. Passing selected test cases
does not establish a universal error bound or monotonic error reduction for
every input.

## Verification

### Recorded verification checkpoint

On October 12, 2026, both GitHub workflows completed successfully for revision:

```text
a7e76b804ccfa6f478cfd332083b64b7474e9893
```

| Check | Recorded result | Evidence |
|---|---|---|
| GitHub tests | Success | [Test run 38203890104](https://github.com/quantarion369-arch/Aqarion-Fastapi/actions/runs/38203890104) |
| GitHub Ruff and mypy workflow | Success | [Lint run 38203890122](https://github.com/quantarion369-arch/Aqarion-Fastapi/actions/runs/38203890122) |
| Local Termux suite | 11 tests passed | Recorded local execution |
| Local research-script syntax check | Passed | Recorded local execution |
| Local whitespace check | Passed | Recorded local execution |

This is a revision-specific checkpoint, not a guarantee about future changes.
The badges at the top link to the workflow history for the main branch.

### Run checks locally

After installing development dependencies and activating the environment:

```bash
pytest -q
ruff check .
mypy myfastapi --ignore-missing-imports
git diff --check
```

The commands above include the test, lint, and type-check commands used by the
current GitHub workflows, plus a local whitespace check.

Check the research script's syntax separately:

```bash
python -m py_compile research/pb-core-006/pb006_extrapolate.py
```

Available helper scripts:

```bash
./scripts/test.sh
./scripts/lint.sh
./scripts/format.sh
```

The formatting script changes files; review its output before committing.

### Test coverage

The recorded local suite passed 11 tests across these four modules:

| Module | Purpose |
|---|---|
| `tests/test_main.py` | Core service and item operations |
| `tests/test_partition.py` | Existing partition endpoint tests |
| `tests/test_asymptotic.py` | Asymptotic response and selected error comparisons |
| `tests/test_partition_boundary.py` | Fresh-process upper-boundary computation and API boundary behavior |

The boundary tests check:

- Exact computation of `partition(1000)` in a fresh Python subprocess.
- A successful response from `/partition/1000`.
- Rejection of `/partition/1001` with HTTP 400 and the expected detail.

The fresh-process check avoids relying on a cache warmed by earlier tests.

### Termux-specific mypy workaround

In the tested Termux Python 3.13 environment, mypy 2.4.0's native parser failed
to load its `ast_serialize` extension:

```text
ImportError: dlopen failed: cannot locate symbol "PyExc_TypeError"
```

The local type check passed using:

```bash
.venv/bin/python -m mypy --no-native-parser myfastapi
```

This selects the fallback parser; it does not suppress application type errors.

The GitHub Python 3.12 lint workflow passed without this workaround.
Do not add the flag to the hosted workflow solely because the local Termux
environment required it.

## Project Layout

```text
Aqarion-Fastapi/
├── .github/
│   └── workflows/
│       ├── lint.yml
│       └── test.yml
├── docs/
│   └── index.md
├── docs_src/
│   └── tutorial/
│       └── first_steps.py
├── myfastapi/
│   ├── __init__.py
│   ├── main.py
│   ├── partition.py
│   ├── asymptotic.py
│   └── routers/
│       ├── __init__.py
│       ├── items.py
│       ├── partition.py
│       └── asymptotic.py
├── research/
│   └── pb-core-006/
│       └── pb006_extrapolate.py
├── scripts/
│   ├── format.sh
│   ├── lint.sh
│   └── test.sh
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_partition.py
│   ├── test_asymptotic.py
│   └── test_partition_boundary.py
├── .gitignore
├── .python-version
├── LICENSE
├── README.md
└── pyproject.toml
```

This is a navigational overview, not an exhaustive repository inventory.

## Technology

| Layer | Technology |
|---|---|
| Language | Python |
| API framework | FastAPI |
| ASGI server | Uvicorn |
| Data models | Pydantic |
| Testing | Pytest, pytest-asyncio, HTTPX |
| Linting and formatting | Ruff |
| Static type checking | Mypy |
| Continuous integration | GitHub Actions |
| Exact partition computation | Integer arithmetic and cached recurrence |
| Asymptotic endpoint | Python `math` computations |
| Research extrapolation script | mpmath |

Dependency declarations and version requirements are maintained in
[`pyproject.toml`](pyproject.toml).

## Research Boundaries

Keep these categories distinct:

| Category | What it establishes |
|---|---|
| Exact computation | An exact result for the implemented calculation and specified input |
| Numerical approximation | An approximate value produced by the implemented formula |
| Empirical test | Observed behavior for the cases actually tested |
| Formal proof | A theorem established under explicit assumptions through an appropriate proof record |

The API's asymptotic comparison and the research extrapolation script do not,
by themselves, certify an asymptotic theorem.

Research derivations, proof obligations, counterexamples, formal verification,
and audit conclusions belong in their authoritative research records.
Passing CI does not promote a mathematical claim beyond its supporting evidence.

## Related Repository

[AQARION](https://github.com/quantarion369-arch/AQARION) is the umbrella research
repository for the broader mathematics, proof, and audit work.

This repository provides the API/service boundary for selected computations.

## Roadmap

Completed:

- [x] FastAPI service scaffold.
- [x] Async integration tests.
- [x] Ruff and mypy checks.
- [x] Separate GitHub test and lint workflows.
- [x] Exact integer partition endpoint.
- [x] Leading Hardy–Ramanujan comparison endpoint.
- [x] Iterative partition computation and upper-boundary regression tests.
- [x] Successful hosted test and lint checkpoint for revision `a7e76b8`.

Potential future work—not implemented or promised by this list:

- [ ] Add a `/version` endpoint.
- [ ] Improve OpenAPI tags and route descriptions.
- [ ] Integrate selected audit artifacts with explicit provenance.
- [ ] Add optional container deployment configuration.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make a focused change with appropriate tests.
4. Run tests, lint, and type checks.
5. Review the diff and open a pull request.

```bash
git checkout -b feature/my-feature

pytest -q
ruff check .
mypy myfastapi --ignore-missing-imports
git diff --check
```

Include verification results and identify the revision tested.

Keep mathematical claims precise: distinguish exact computation,
approximation, empirical observation, and proof. Do not describe passing
software checks as mathematical certification.

## License

Licensed under the MIT License. See [`LICENSE`](LICENSE).

---

<div align="center">

<sub>Part of the <a href="https://github.com/quantarion369-arch/AQARION">AQARION</a> research stack.</sub>

</div>
