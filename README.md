# sample-project

A project template for Python + Hydra experiments.

## Getting Started (New Project)

1. Clone this template with your project name:

```bash
git clone https://github.com/NYNYNY67/sample-project.git your-project-name
cd your-project-name
```

2. Run the initialization script:

```bash
./init_project.sh
```

This script will:

- Rename `src/sample_project/` to match your project name (hyphens are converted to underscores, e.g. `my-project` -> `my_project`)
- Update all `sample_project` references in `run/`, `src/`, `tests/`, `.claude/` (`.py`, `.md`, `.yaml` files)
- Generate `pyproject.toml` via `uv init --lib`
- Install dependencies (`coolname`, `gitpython`, `hydra-core`, `loguru`, `omegaconf`) and dev dependencies (`ipykernel`, `pytest`, `ruff`)
- Remove `init_project.sh` itself (one-time use)
- Initialize a git repository and create the first commit

## Setup (Existing Project)

```bash
uv sync
```

## Jupyter Kernel

Register the uv-managed virtual environment as a Jupyter kernel:

```bash
uv run python -m ipykernel install --user --name <your-project-name>
```

The kernel will appear in VS Code and JupyterLab. Notebooks are stored in the `notebook/` directory.

## Run

```bash
# Basic
uv run python run/main.py

# Override config
uv run python run/main.py param=value nested.param=value

# Specify run ID
uv run python run/main.py run_id=myrun

# Pipeline with shared run ID
RUN_ID=$(python -c "from coolname import generate_slug; print(generate_slug(2))")
uv run python run/fetch.py run_id=$RUN_ID
uv run python run/preprocess.py run_id=$RUN_ID
uv run python run/train.py run_id=$RUN_ID
```

## Lint

```bash
./lint.sh
```

## Test

```bash
uv run pytest tests/
```

## Project Structure

```
conf/               Hydra configs (yaml)
run/                Entry point scripts
src/sample_project/ Source package (auto-installed by uv sync)
notebook/           Jupyter notebooks
tests/              Tests
outputs/            Hydra output directories
```
