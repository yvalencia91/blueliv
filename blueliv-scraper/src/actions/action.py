from src.actions.interface import Scrapper
from typing import Dict
from settings import config
import json
import requests
from logging import getLogger

log = getLogger(__name__)


def scrap_forum(strategy: Scrapper) -> Dict:

    strategy.retrieve()
    strategy.parse()
    payload = strategy.extract()
    return payload


def post_threats(payload: Dict) -> None:
    schema = config.authentication["endpoint"]["schema"]
    host = config.authentication["endpoint"]["host"]
    path = config.authentication["endpoint"]["threat"]
    url = f"{schema}://{host}{path}"

    headers = config.authentication["headers"]
    headers["Authorization"] = f"Bearer {config.authentication['token']['access_token']}"

    for p in payload["threats"]:
        response = requests.request("POST", url, headers=headers, data=json.dumps(p))
        log.info(f"New threat added: {response.json()}")
