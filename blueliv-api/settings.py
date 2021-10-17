from pyaml_env import parse_config
from dataclasses import dataclass
from typing import Dict

@dataclass
class Config:
    secret_key: str
    logger: Dict
    apm: Dict


def setup_config():
    cfg = parse_config("settings.yaml")
    return Config(**cfg)


config = setup_config()
