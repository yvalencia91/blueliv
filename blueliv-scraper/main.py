from src.actions.action import scrap_forum, post_threats
from src.actions.no_credentials import NoCredentials
from src.authentication.get_token import login
from time import sleep
from src.lib.logger import setup_logger
from logging import getLogger
from settings import config

setup_logger(config)
log = getLogger(__name__)


def main():
    payload = scrap_forum(strategy=NoCredentials())
    login()
    post_threats(payload=payload)


if __name__ == "__main__":
    count = 0
    while count < 5:
        log.info(f"Main sequence started. Count = {count}")
        main()
        sleep(10)
        count += 1
