<div align="center">⚡ AQARION-Fastapi

A minimal, production-ready FastAPI scaffold. Part of the AQARION research stack.

""Python" (https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)" (https://www.python.org/)
""FastAPI" (https://img.shields.io/badge/FastAPI-0.115%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)" (https://fastapi.tiangolo.com/)
""License: MIT" (https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)" (https://opensource.org/licenses/MIT)
""Tests" (https://img.shields.io/badge/test--functions-8-blue?style=for-the-badge)" (https://github.com/quantarion369-arch/Aqarion-Fastapi/actions)
""Ruff" (https://img.shields.io/badge/lint-ruff-46aef7?style=for-the-badge&logo=ruff&logoColor=white)" (https://github.com/astral-sh/ruff)
""Mypy" (https://img.shields.io/badge/types-mypy-2a6db2?style=for-the-badge&logo=python&logoColor=white)" (https://mypy-lang.org/)

"Quick Start" (#-quick-start) · "Endpoints" (#-endpoints) · "Tech Stack" (#%EF%B8%8F-tech-stack) · "Project Layout" (#-project-layout) · "Related Repos" (#-related-repositories)

</div>---

📖 Concept

This repository is the service layer for the AQARION research stack. It provides a working FastAPI application that can expose mathematical results, audit artifacts, and evidence-backed content as HTTP APIs. It is intentionally minimal — no database, no authentication layer, no Docker — so it can serve as a clean template for new services or a foundation for the full AQARION API.

The application now includes three functional areas:

- Core service: root response, health check, and in-memory item endpoints.
- Exact integer partitions: computes (p(n)), the number of integer partitions of (n), using Euler's pentagonal-number recurrence.
- Asymptotic comparison: compares the exact partition value with the leading Hardy–Ramanujan approximation and reports the relative error for the requested input.

«Status: Research/API scaffold. Eight test functions are present across three test modules. Their presence does not establish that the current suite passes from a clean clone; run the commands below and check the GitHub Actions results for the commit you intend to use. Production readiness is not asserted by the scaffold alone.»

Mathematical computations exposed through this API are application outputs, not independent proofs, formal verification certificates, or publication approvals. Research claims and their supporting evidence should remain in their appropriate authoritative research records.

---

🚀 Quick Start

Prerequisites: Python 3.11+ and "pip".

# 1. Clone the repository
git clone https://github.com/quantarion369-arch/Aqarion-Fastapi.git
cd Aqarion-Fastapi

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# 3. Install with development dependencies
pip install -e '.[dev]'

# 4. Run the development server
uvicorn myfastapi.main:app --reload

The API will be available at http://127.0.0.1:8000.

Interactive docs (Swagger UI) are at http://127.0.0.1:8000/docs. The generated OpenAPI schema is at http://127.0.0.1:8000/openapi.json.

---

🔌 Endpoints

Method| Path| Description
GET| "/"| Hello message
GET| "/health"| Health check
GET| "/items/"| List all in-memory items
POST| "/items/"| Create an item (body: "{"id": 1, "name": "apple"}")
GET| "/items/{item_id}"| Fetch a single item by ID
GET| "/partition/{n}"| Return the exact integer partition number (p(n))
GET| "/asymptotic/{n}"| Compare (p(n)) with its leading Hardy–Ramanujan approximation

Integer partition endpoint

"GET /partition/{n}" returns a JSON object with the requested integer "n" and its exact partition number "p_n".

The route accepts (0 \leq n \leq 1000). Negative values and values above the supported limit are rejected with an HTTP 400 response.

Example:

curl http://127.0.0.1:8000/partition/10

Expected mathematical result:

{
  "n": 10,
  "p_n": 42
}

The computation uses Euler's pentagonal-number recurrence with memoization. The endpoint returns an exact integer result within its configured input range.

Hardy–Ramanujan asymptotic endpoint

"GET /asymptotic/{n}" compares the exact partition value against the leading-order Hardy–Ramanujan approximation.

The route accepts (1 \leq n \leq 1000). It returns these fields:

Field| Meaning
"n"| Requested positive integer
"exact"| Exact partition value (p(n))
"approximation"| Floating-point leading-order approximation
"relative_error"| Absolute difference between approximation and exact value, divided by the exact value

The implemented leading term is

[
p(n) \approx
\frac{\exp!\left(\pi\sqrt{2n/3}\right)}
{4\sqrt{3},n}.
]

Example:

curl http://127.0.0.1:8000/asymptotic/100

The response contains the exact partition value alongside the approximation and its relative error.

Interpretation boundary: This is an asymptotic approximation, not an exact formula for (p(n)). The returned relative error describes the particular requested input. A small number of passing test cases does not establish a universal error bound, a convergence theorem, or monotonic error reduction for every (n).

---

✨ Features

Feature| Description
FastAPI| Modern, high-performance ASGI web framework
Pydantic v2| Request/response data validation and model definitions
Uvicorn| ASGI server with development reload support
In-memory item API| Basic item creation, listing, and retrieval
Exact partition computation| Euler's pentagonal-number recurrence for (p(n)), with memoization
Asymptotic comparison| Leading Hardy–Ramanujan approximation with input-specific relative error
Pytest + HTTPX| Async integration tests against the ASGI application
Ruff| Python linting and formatting
Mypy| Static type checking configuration
GitHub Actions| Separate workflow files for tests and lint/type checks
Development scripts| "scripts/format.sh", "scripts/lint.sh", and "scripts/test.sh"

---

🛠️ Tech Stack

Layer| Technology
Language| Python 3.11+
Framework| FastAPI
ASGI Server| Uvicorn (standard extras)
Data Models| Pydantic v2 + pydantic-settings
Testing| Pytest, pytest-asyncio, HTTPX
Linting / Formatting| Ruff
Type Checking| Mypy
CI| GitHub Actions
Partition computation| Python integers, recurrence, memoization
Asymptotic computation| Python "math" module

---

📁 Project Layout

Aqarion-Fastapi/
├── .github/
│   └── workflows/
│       ├── lint.yml                  # Ruff + Mypy workflow
│       └── test.yml                  # Pytest workflow
├── docs/
│   └── index.md                      # Project documentation
├── docs_src/
│   └── tutorial/
│       └── first_steps.py            # Runnable tutorial example
├── myfastapi/
│   ├── __init__.py
│   ├── main.py                       # FastAPI app + router registration
│   ├── partition.py                  # Exact integer partition function p(n)
│   ├── asymptotic.py                 # Hardy–Ramanujan approximation + error
│   └── routers/
│       ├── __init__.py
│       ├── items.py                  # /items endpoints
│       ├── partition.py              # /partition/{n} endpoint
│       └── asymptotic.py             # /asymptotic/{n} endpoint
├── scripts/
│   ├── format.sh                     # Ruff formatting and autofix
│   ├── lint.sh                       # Ruff lint + Mypy
│   └── test.sh                       # pytest -q
├── tests/
│   ├── __init__.py
│   ├── test_main.py                  # Core service and item tests
│   ├── test_partition.py             # Partition endpoint tests
│   └── test_asymptotic.py            # Asymptotic endpoint tests
├── .gitignore
├── .python-version                   # Python version selection
├── LICENSE                           # MIT
├── README.md                         # This file
└── pyproject.toml                    # Project metadata + dependencies

The layout above identifies the main application, router, test, and workflow files relevant to the documented API. It is not intended to enumerate every repository file.

---

🧪 Running Tests

Install the development dependencies using the Quick Start instructions, then activate the virtual environment.

# Activate the virtual environment first
source .venv/bin/activate

# Run the complete test suite
pytest -q

The repository currently contains eight test functions across these modules:

- "tests/test_main.py"
- "tests/test_partition.py"
- "tests/test_asymptotic.py"

The exact number of passing tests and the final test result must come from running the suite. Do not treat the presence of test functions as evidence that the current checkout passes.

To run lint and type checks:

./scripts/lint.sh

To auto-format:

./scripts/format.sh

To run the test script directly:

./scripts/test.sh

CI verification: Check the test and lint workflow results for the exact commit being reviewed. Workflow files existing in the repository does not, by itself, prove that either workflow has passed.

---

🔗 Related Repositories

Repository| Description
"AQARION" (https://github.com/quantarion369-arch/AQARION)| Umbrella research repository for mathematics, Lean proofs, and audit artifacts
"Aqarion-Fastapi" (https://github.com/quantarion369-arch/Aqarion-Fastapi)| This repository. FastAPI service scaffold for the AQARION stack

The API repository is the service boundary for selected computations. Research derivations, proof obligations, formal verification, counterexamples, and audit conclusions should remain in their existing authoritative records and be referenced here only when a concrete API integration requires them.

---

🗺️ Roadmap

☑ Project scaffold with FastAPI, Pydantic, and Uvicorn
☑ Async tests with pytest + HTTPX
☑ Ruff and Mypy configuration
☑ GitHub Actions workflows for lint and tests
☑ Exact integer partition computation endpoint
☑ Hardy–Ramanujan leading-order comparison endpoint
☐ Verify the current test and lint workflows on the intended commit
☐ Add "/version" endpoint
☐ Add OpenAPI tags and descriptions for all routes
☐ Connect to AQARION audit artifacts as a data source, with explicit provenance
☐ Dockerfile + docker-compose (optional)

---

🤝 Contributing

1. Fork the repository.
2. Create a feature branch: "git checkout -b feature/my-feature".
3. Commit your changes: "git commit -m 'Add my feature'".
4. Push to the branch: "git push origin feature/my-feature".
5. Open a Pull Request.

Before opening a PR, run the test suite:

pytest -q

Run lint and type checks:

./scripts/lint.sh

Include the relevant test results when describing a change. Mathematical claims should distinguish exact computation, numerical approximation, empirical observation, and formally established proof.

---

📄 License

This project is licensed under the MIT License. See the "LICENSE" file for details.

<div align="center">
<sub>Part of the <a href="https://github.com/quantarion369-arch/AQARION">AQARION</a> research stack.</sub>
</div>
