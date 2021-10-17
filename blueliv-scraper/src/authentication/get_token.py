import requests
import json
from settings import config


def login() -> None:
    schema = config.authentication["endpoint"]["schema"]
    host = config.authentication["endpoint"]["host"]
    path = config.authentication["endpoint"]["login"]
    url = f"{schema}://{host}{path}"
    payload = json.dumps(config.authentication["basic"])

    headers = config.authentication["headers"]

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = response.json()

    config.authentication["token"]["access_token"] = response_json["access_token"]
    config.authentication["token"]["refresh_token"] = response_json["refresh_token"]

