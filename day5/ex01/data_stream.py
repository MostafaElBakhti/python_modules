from typing import Any, List, Sequence
from abc import ABC, abstractmethod
import typing

class DataProcessor(ABC):
    def __init__(self):
        self.storage: list[tuple[int, str]] = []
        self.rank = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise Exception("No data to output")
        return self.storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: int | float | Sequence[int | float]) -> None:
            if not self.validate(data):
                raise Exception("Improper numeric data")

            if isinstance(data, (int, float)):
                self.storage.append((self.rank, str(data)))
                self.rank += 1
            else:
                for item in data:
                    self.storage.append((self.rank, str(item)))
                    self.rank += 1


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("mproper text data")

        if isinstance(data, str):
            self.storage.append((self.rank, data))
            self.rank += 1
        else:
            for item in data:
                self.storage.append((self.rank, item))
                self.rank += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items()
                )
                for item in data
            )

        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        if isinstance(data, dict):
            self.storage.append((self.rank, str(data)))
            self.rank += 1
        else:
            for item in data:
                self.storage.append((self.rank, str(item)))
                self.rank += 1

class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        
    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element in stream: {element}")
    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        

ds = DataStream()

num_proc = NumericProcessor()
text_proc = TextProcessor()
log_proc = LogProcessor()

ds.register_processor(num_proc)
ds.register_processor(text_proc)
ds.register_processor(log_proc)


stream = [
    "Hello",
    42,
    {"log_level": "INFO", "log_message": "Test"},
    [1,2,"oops"]
]

ds.process_stream(stream)