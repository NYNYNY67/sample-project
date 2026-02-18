#!/usr/bin/env bash
set -e

# Initialize project dependencies and rename package references.
# Rename the project directory manually before running this script.
#
# Usage:
#   mv sample-project <your-project-name>
#   cd <your-project-name>
#   ./init_project.sh

PROJECT_NAME="$(basename "$(pwd)")"
# Convert hyphens to underscores for Python package name (e.g. my-project -> my_project)
PACKAGE_NAME="${PROJECT_NAME//-/_}"
OLD_PACKAGE="sample_project"

echo "Initializing project: $PROJECT_NAME (package: $PACKAGE_NAME)"

# Rename src package directory
if [ -d "src/$OLD_PACKAGE" ] && [ "$OLD_PACKAGE" != "$PACKAGE_NAME" ]; then
    mv "src/$OLD_PACKAGE" "src/$PACKAGE_NAME"
    echo "Renamed package: src/$OLD_PACKAGE -> src/$PACKAGE_NAME"
fi

# Replace old package name in source files
if [ "$OLD_PACKAGE" != "$PACKAGE_NAME" ]; then
    find run src tests .claude -type f \( -name '*.py' -o -name '*.md' -o -name '*.yaml' \) \
        -exec sed -i '' "s/${OLD_PACKAGE}/${PACKAGE_NAME}/g" {} +
    echo "Replaced '$OLD_PACKAGE' -> '$PACKAGE_NAME' in source files"
fi

# Create pyproject.toml with src layout
uv init --lib --no-readme

# Main dependencies (always resolved to latest)
uv add coolname gitpython hydra-core loguru omegaconf

# Dev dependencies
uv add --group dev ipykernel pytest ruff

# Remove this script (no longer needed after initialization)
rm -- "$0"
echo "Removed init_project.sh"

# Initialize git repository and create first commit
git init
git add -A
git commit -m "first commit"

echo ""
echo "Done. Run: uv run python run/main.py"
