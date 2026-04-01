---
name: python-project-structure
description: Define and apply a clear Python repository layout for new projects or legacy refactors. Use when creating project scaffolding, standardizing directories, or reorganizing an existing Python codebase.
---

# Python Project Structure

Use this structure as the default baseline.

```text
.
├── <package_name>/
│   ├── __init__.py
│   └── ...
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── smoke/
│   ├── fixtures/
│   └── support/
├── scripts/
├── docs/
├── artifacts/
├── .dockerignore
├── .envrc
├── .gitignore
├── .python-version
├── Dockerfile
└── pyproject.toml
```

Folders can be omitted if not needed, but the top-level structure should be followed when applicable. For example, if no Dockerfiles are needed, the `Dockerfile` and `.dockerignore` can be omitted. If no documentation is needed, the `docs/` directory can be omitted.

## Conventions

- Keep every `__init__.py` file empty.
- Use `poetry` for dependency management.
- Pin Python in `.python-version` (default `3.13.0` unless project constraints require another version).
- Use `direnv` with `.envrc` for local environment setup.
- If multiple container variants are needed, add a `docker/` directory and place Dockerfiles there.
- Treat `.venv/` as local-only and never commit it.

## `.envrc` Template

```bash
VIRTUAL_ENV=.venv
python_version="$(cat .python-version)"
layout pyenv "$python_version"
layout python

if [ ! -x "$VIRTUAL_ENV/bin/poetry" ]; then
  pip install poetry
  pip install keyrings-google-artifactregistry-auth==1.1.2
fi

dotenv_if_exists .env
```

## Refactor Checklist

When standardizing a legacy project:

1. Create missing top-level directories (`tests/`, `scripts/`, `docs/`, `artifacts/`).
2. Move runtime package code under `<package_name>/`.
3. Split tests into `unit/`, `integration/`, and `smoke/`.
4. Add or normalize `.python-version`, `pyproject.toml`, and `.envrc`.
5. Verify `__init__.py` files are empty.
