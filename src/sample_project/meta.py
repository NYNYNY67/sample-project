import json
from datetime import datetime, timezone
from pathlib import Path

from git import InvalidGitRepositoryError, Repo
from loguru import logger


def collect_meta() -> dict:
    """Collect execution metadata including timestamp and git info."""
    meta = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    try:
        repo = Repo(search_parent_directories=True)
        meta["git"] = {
            "branch": repo.active_branch.name,
            "commit": repo.head.commit.hexsha,
            "dirty": repo.is_dirty(),
        }
        if repo.is_dirty():
            logger.warning("Git working tree is dirty. Commit hash may not be reproducible.")
    except (InvalidGitRepositoryError, TypeError):
        meta["git"] = None
    return meta


def save_meta(output_dir: Path) -> Path:
    """Collect and save metadata to output_dir/meta.json."""
    meta = collect_meta()
    path = output_dir / "meta.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
    return path
