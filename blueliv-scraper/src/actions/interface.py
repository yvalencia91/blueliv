from abc import ABC, abstractmethod
from typing import Dict


class Scrapper(ABC):

    def __init__(self):
        self.response = None
        self.threats = None

    @abstractmethod
    def retrieve(self):
        pass

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def extract(self) -> Dict:
        pass