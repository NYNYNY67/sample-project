import hydra
from loguru import logger
from omegaconf import DictConfig

from sample_project.resolvers import ensure_unique_output_dir, register_resolvers

register_resolvers()


@hydra.main(version_base=None, config_path="../conf", config_name="main")
def main(cfg: DictConfig) -> None:
    output_dir = ensure_unique_output_dir()
    logger.info(f"Output: {output_dir}")
    logger.info(f"config:\n{cfg}")


if __name__ == "__main__":
    main()
