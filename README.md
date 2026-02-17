# sample-project

## Setup

```bash
uv sync
```

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
tests/              Tests
outputs/            Hydra output directories
```
