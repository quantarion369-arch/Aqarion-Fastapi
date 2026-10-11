# Aqarion-Fastapi

A FastAPI project scaffold. Part of the AQARION research stack.

## Quickstart

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -e '.[dev]'
uvicorn myfastapi.main:app --reload
```

## Endpoints

- `GET /`        — hello message
- `GET /health`  — health check
- `GET /items/`  — list items
- `POST /items/` — create item
- `GET /items/{id}` — fetch item

## Development

```bash
./scripts/format.sh
./scripts/lint.sh
./scripts/test.sh
```

## Layout

```
myfastapi/       package
docs/            documentation
docs_src/        runnable doc examples
tests/           pytest suite
scripts/         dev scripts
.github/         CI workflows
```

## License

MIT
