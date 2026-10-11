<div align="center">

# ⚡ AQARION-fastapi

**A minimal, production-ready FastAPI scaffold. Part of the AQARION research stack.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-3%20passed-brightgreen?style=for-the-badge)](https://github.com/quantarion369-arch/Aqarion-Fastapi/actions)
[![Ruff](https://img.shields.io/badge/lint-ruff-46aef7?style=for-the-badge&logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![Mypy](https://img.shields.io/badge/types-mypy-2a6db2?style=for-the-badge&logo=python&logoColor=white)](https://mypy-lang.org/)

[Quick Start](#-quick-start) · [Endpoints](#-endpoints) · [Tech Stack](#%EF%B8%8F-tech-stack) · [Project Layout](#-project-layout) · [Related Repos](#-related-repositories)

</div>

---

## 📖 Concept

This repository is the **service layer** for the AQARION research stack. It provides a working FastAPI application that can expose mathematical results, audit artifacts, and evidence-backed content as HTTP APIs. It is intentionally minimal — no database, no auth, no Docker — so it can serve as a clean template for new services or a foundation for the full AQARION API.

> **Status:** Scaffold. All 3 tests pass from a clean clone. CI workflows are present and will run on the next push.

---

## 🚀 Quick Start

**Prerequisites:** Python 3.11+ and `pip`.

```bash
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
```

The API will be available at http://127.0.0.1:8000.
Interactive docs (Swagger UI) are at http://127.0.0.1:8000/docs.

---

🔌 Endpoints

Method Path Description
GET / Hello message
GET /health Health check
GET /items/ List all items
POST /items/ Create a new item (body: {"id": 1, "name": "apple"})
GET /items/{id} Fetch a single item by ID

---

✨ Features

Feature Description
FastAPI Modern, high-performance async web framework
Pydantic v2 Data validation and settings management
Uvicorn Lightning-fast ASGI server with --reload support
Pytest + HTTPX Async integration tests against the ASGI app
Ruff Fast Python linter and formatter
Mypy Static type checking (strict mode)
GitHub Actions CI workflows for test and lint on every push
Dev Scripts scripts/format.sh, scripts/lint.sh, scripts/test.sh

---

🛠️ Tech Stack

Layer Technology
Language Python 3.11+
Framework FastAPI
ASGI Server Uvicorn (standard extras)
Data Models Pydantic v2 + pydantic-settings
Testing Pytest, pytest-asyncio, HTTPX
Linting / Formatting Ruff
Type Checking Mypy (strict)
CI GitHub Actions

---

📁 Project Layout

```
Aqarion-Fastapi/
├── .github/
│   └── workflows/
│       ├── lint.yml              # Ruff + Mypy on every push
│       └── test.yml              # Pytest on every push
├── docs/
│   └── index.md                  # Project documentation
├── docs_src/
│   └── tutorial/
│       └── first_steps.py        # Runnable tutorial example
├── myfastapi/                    # Main Python package
│   ├── __init__.py
│   ├── main.py                   # FastAPI app + root routes
│   └── routers/
│       ├── __init__.py
│       └── items.py              # /items CRUD endpoints
├── scripts/
│   ├── format.sh                 # ruff format + ruff check --fix
│   ├── lint.sh                   # ruff check + mypy
│   └── test.sh                   # pytest -q
├── tests/
│   ├── __init__.py
│   └── test_main.py              # 3 async integration tests
├── .gitignore
├── .python-version               # 3.12
├── LICENSE                       # MIT
├── README.md                     # This file
└── pyproject.toml                # Project metadata + dependencies
```

---

🧪 Running Tests

```bash
# Activate the virtual environment first
source .venv/bin/activate

# Run the test suite
pytest -q
```

Expected output: 3 passed.

To run lint and type checks:

```bash
./scripts/lint.sh
```

To auto-format:

```bash
./scripts/format.sh
```

---

🔗 Related Repositories

Repository Description
AQARION Umbrella research repository. Mathematics, Lean proofs, and audit artifacts.
Aqarion-Fastapi This repository. FastAPI service scaffold for the AQARION stack.

---

🗺️ Roadmap

☑ Project scaffold with FastAPI, Pydantic, Uvicorn
☑ Async tests with pytest + HTTPX
☑ Ruff and Mypy configuration
☑ GitHub Actions CI (lint + test)
☐ Add /version endpoint
☐ Add OpenAPI tags and descriptions for all routes
☐ Connect to AQARION audit artifacts as data source
☐ Dockerfile + docker-compose (optional)

---

🤝 Contributing

1. Fork the repository.
2. Create a feature branch: git checkout -b feature/my-feature.
3. Commit your changes: git commit -m 'Add my feature'.
4. Push to the branch: git push origin feature/my-feature.
5. Open a Pull Request.

Please ensure all tests pass (pytest -q) and lint is clean (./scripts/lint.sh) before opening a PR.

---

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

<div align="center">
<sub>Part of the <a href="https://github.com/quantarion369-arch/AQARION">AQARION</a> research stack.</sub>
</div>
```

---

What changed and why

Improvement Reason
Centered header + badges Immediate visual status: Python version, framework, license, tests, lint, types
Tagline + concept blockquote Answers "what is this?" in under 10 seconds
Quick Start with numbered steps Copy-paste ready; includes expected URL
Endpoints table FastAPI-specific; reviewers see the API surface at a glance
Features table More scannable than a bullet list
Tech Stack table Explicit versions and layers
ASCII file tree Standard for GitHub READMEs; shows structure without a separate file
Related Repos section Directly links to your AQARION umbrella repo as requested
Roadmap checkboxes Shows project maturity and next steps
Contributing + License Standard open-source completeness
