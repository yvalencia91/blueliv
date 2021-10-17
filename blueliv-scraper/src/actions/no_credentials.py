from src.actions.interface import Scrapper
from settings import config
from bs4 import BeautifulSoup
from src.utils.utils import format_date
import requests

from logging import getLogger

log = getLogger(__name__)

class NoCredentials(Scrapper):

    def retrieve(self):
        log.info("Setting up url and headers")
        url = config.target["url"]
        headers = config.target["headers"]

        self.response = requests.request("GET", url, headers=headers)

        if self.response.status_code != 200:
            log.error("Something went wrong while getting the HTML")

        log.info("Retrieve complete")

    def parse(self):

        log.info("Parsing raw HTML")
        soup = BeautifulSoup(self.response.text, 'lxml')

        log.info("Looking for topics...")
        self.threats = soup.find_all("tr", class_="topicrow")

    def extract(self):

        all_threats = []
        log.info("Creating payload format...")
        for t in self.threats:
            new_threat = t.find_all("a", href=True)

            topic = new_threat[0].text
            author = new_threat[2].text
            post_date = t.find("span", class_="nowrap").text

            threat = {
                "author": author,
                "topic": topic,
                "post_date": format_date(post_date=post_date)
            }

            all_threats.append(threat)

        return {"threats": all_threats}