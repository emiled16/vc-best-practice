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
| CLI | `typer` |
| Path Management | `pathlib` |
| Console printing | `rich` |
| Releases | `release-please` |

If a project already uses another toolchain, follow the project convention first.

## Code Style

- Prefer functions and modules over classes unless stateful behavior or explicit interfaces require classes.
- Keep modules as lightweight and focused as possible. Avoid mixing unrelated responsibilities in one file.
- Split definitions by concern instead of colocating everything with the caller.
  For example, keep FastAPI request/response models in a dedicated `models/` package rather than in the endpoint module.
  Prefer one module per model when practical, such as `models/users.py`.
- Apply the same rule to persistence code.
  Prefer one ORM/table schema module per table or aggregate instead of a single large file containing every schema.
- Move small general-purpose reusable helpers into a shared `utils/` package or module instead of leaving them embedded in feature modules.
- Use dependency injection for external dependencies and cross-cutting services when it improves testability, configurability, or separation of concerns.
  Typical examples include database sessions, repositories, API clients, auth context, and configuration.
  Avoid introducing dependency injection when direct construction is simpler and the dependency is local, stable, and not worth the extra indirection.
- Keep every `__init__.py` file empty.
- Prefer absolute imports.
- Use type hints throughout, with modern syntax (`list[str]`, `X | None`).
- Optimize for readability and maintainability over cleverness.
- Do not overengineer. Prefer the simplest design that satisfies the current requirements and add abstraction only when there is a clear need.
- Keep changes scoped to the user request.
- Use complete import paths.
- Use try/except blocks only when it is necessary.
- Add minimal doc string at the function level to explain the function's purpose, if the function is not self-explanatory.

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
- [ ] Modules stay lightweight and organized by responsibility
- [ ] Dependency injection is used where it adds clear value
- [ ] Tests cover behavior and pass
- [ ] `ruff` passes
- [ ] Commits are atomic and use Conventional Commits
