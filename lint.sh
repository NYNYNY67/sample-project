#!/bin/bash
set -e

echo "Running ruff checks..."
uv run ruff check --fix run src tests

echo "Running ruff format..."
uv run ruff format run src tests

echo "Running import formatting..."
uv run ruff check --extend-select I --fix run src tests

echo "All lint checks completed successfully!"
