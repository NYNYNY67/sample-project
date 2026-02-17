import os
from pathlib import Path

from coolname import generate_slug
from hydra.core.hydra_config import HydraConfig
from omegaconf import OmegaConf


def register_resolvers():
    OmegaConf.register_new_resolver(
        "short_id", lambda: generate_slug(2), use_cache=True, replace=True
    )


def ensure_unique_output_dir() -> Path:
    """Rename Hydra's output_dir with a fresh slug if it already exists."""
    output_dir = Path(HydraConfig.get().runtime.output_dir)
    if not output_dir.exists():
        return output_dir

    parent = output_dir.parent
    existing = {p.name for p in parent.iterdir() if p.is_dir()}
    for _ in range(100):
        new_name = generate_slug(2)
        if new_name not in existing:
            break
    else:
        raise RuntimeError(
            f"Failed to generate a unique slug after 100 attempts in {parent}"
        )

    new_dir = parent / new_name
    os.rename(output_dir, new_dir)
    return new_dir
