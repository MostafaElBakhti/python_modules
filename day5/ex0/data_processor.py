from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self.storage = []
        self.rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        pass


class NumericProcessor(DataProcessor):
    pass


class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass