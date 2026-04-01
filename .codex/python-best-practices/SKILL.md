---
name: python-best-practices
description: Apply practical Python engineering standards across implementation, refactoring, and review work. Use when writing Python, reviewing Python changes, or improving Python code quality.
---

# Python Best Practices

Use these rules as defaults unless the repository already enforces a different standard.

## Preferred Toolchain

| Concern | Tool |
|---|---|
| Dependency management | `poetry` |
| Python version | `pyenv` + `.python-version` |
| Env vars | `direnv` + `.envrc` + `.env` |
| Linting / formatting | `ruff` |
| Testing | `pytest` |
| Coverage | `pytest-cov` |
| Mocking | `pytest-mock` |
| Async tests | `pytest-asyncio` |
| API | `fastapi` |
| ORM | `sqlalchemy` |
| Migrations | `alembic` |
| Releases | `release-please` |

If a project already uses another toolchain, follow the project convention first.

## Code Style

- Prefer functions and modules over classes unless stateful behavior or explicit interfaces require classes.
- Keep every `__init__.py` file empty.
- Prefer absolute imports.
- Use type hints throughout, with modern syntax (`list[str]`, `X | None`).
- Optimize for readability and maintainability over cleverness.
- Keep changes scoped to the user request.

## Testing

- Treat tests as correctness checks; do not weaken tests to force a pass.
- Consider implementation complete only when behavior is correct and relevant tests pass.
- Prefer a test layout like:

```text
tests/
unit/
integration/
```

## Git & Commits

- Keep commits atomic and reviewable.
- Use [Conventional Commits](https://www.conventionalcommits.org/):

```text
feat(scope): short imperative summary

Optional concise body explaining why.
```

- Do not force-push `main`.
- If blocked, surface the blocker explicitly instead of shipping risky workarounds.

## Quick Checklist

- [ ] Project conventions checked before applying defaults
- [ ] Every `__init__.py` file is empty
- [ ] Imports are clear and consistent
- [ ] Type hints use modern Python syntax
- [ ] Design favors simple functions/modules
- [ ] Tests cover behavior and pass
- [ ] `ruff` passes
- [ ] Commits are atomic and use Conventional Commits
