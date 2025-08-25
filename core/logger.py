import sys
import logging
from typing import Dict, List, Optional, Literal

from core.config import env_config

_LEVEL_BY_ENV: Dict[Literal["production", "staging", "local"], int] = {
    "production": logging.INFO,
    "staging": logging.INFO,
    "local": logging.DEBUG,
}

def setup_logging() -> None:
    root = logging.getLogger()
    if root.handlers:
        return

    env = env_config.LOG_LEVEL if hasattr(env_config, "LOG_LEVEL") else "production"
    level = _LEVEL_BY_ENV.get(env, logging.INFO)

    formatter = logging.Formatter(
        fmt="[%(asctime)s - %(name)s - %(levelname)s] %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )

    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)

    root.setLevel(level)
    root.addHandler(handler)