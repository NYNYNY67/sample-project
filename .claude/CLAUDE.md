# CLAUDE.md - Project Development Guide

## Project Structure

```
project/
├── conf/           # Hydra config files (yaml)
│   ├── *.yaml      # Main config files
│   └── */          # Sub-config directories (config groups)
├── run/            # Entry point scripts
│   └── *.py        # Scripts using hydra.main()
├── src/            # Source code (PyPA src layout)
│   └── sample_project/
│       ├── __init__.py
│       └── *.py
├── notebook/       # Jupyter notebooks
├── tests/          # Test code
│   ├── __init__.py
│   └── test_*.py
├── tmp/            # Temporary files (.gitignore)
├── outputs/        # Hydra output directory (.gitignore)
├── pyproject.toml  # Project settings & dependency management
└── lint.sh         # Lint script
```

## Technology Choices

- **uv**: Faster than pip/poetry, simpler lockfile management
- **Hydra**: Powerful YAML config composition & override, well-suited for experiment management
- **loguru**: Zero-config structured logging, more concise than stdlib logging
- **coolname**: Human-readable slugs, easier to share verbally or on Slack than UUIDs
- **ruff**: Unified linter/formatter in a single fast tool

## Lint & Test

```bash
# Lint (ruff check + format + import sorting)
./lint.sh

# All tests
uv run pytest tests/

# Specific test
uv run pytest tests/test_xxx.py -v
```

## Import Convention

Uses src layout. `uv sync` installs the package in editable mode.

```python
from sample_project.resolvers import register_resolvers
```

## Configuration Management (Hydra)

- Do not set Python-side defaults for Hydra-managed parameters (for reproducibility)
- Treat config as immutable — never modify `cfg` at runtime
- Follow the naming convention: `run/foo.py` -> `conf/foo.yaml`
- Every config must include `task.name` and `task.description`
- `run_id` is auto-generated as a coolname slug (`${short_id:}` resolver)
- Use Compose API in tests (`initialize` + `compose`), not `@hydra.main`
- Call `register_resolvers()` before `compose()` when using custom resolvers

## Examples

```bash
# Basic run
uv run python run/main.py

# Override config values
uv run python run/main.py param=value nested.param=value

# Run with a specific run_id
uv run python run/main.py run_id=myrun
```
