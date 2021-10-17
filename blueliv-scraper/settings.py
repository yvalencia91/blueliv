from pyaml_env import parse_config
from dataclasses import dataclass
from typing import Dict


@dataclass
class Config:
    authentication: Dict
    target: Dict
    logger: Dict


def setup_config():
    cfg = parse_config("settings.yaml")
    return Config(**cfg)


config = setup_config()
