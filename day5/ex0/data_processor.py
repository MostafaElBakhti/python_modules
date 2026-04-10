from abc import ABC, abstractmethod
from typing import Any, cast, Sequence


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
            raise Exception("Improper text data")

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
            self.storage.append((self.rank, ": ".join(data.values())))
            self.rank += 1
        else:
            for item in data:
                self.storage.append((self.rank, ": ".join(item.values())))
                self.rank += 1


if __name__ == "__main__":
    text = TextProcessor()
    int_input = 42
    list_input = ["Hello", "Nexus", "World"]

    int_res = text.validate(int_input)


    nemuric = NumericProcessor()
    nemuric_int = nemuric.validate(42)
    text_input = "hello"
    text_input2 = "foo"
    nemuric_text = nemuric.validate(text_input)

    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '{int_input}': {nemuric_int}")
    print(f"Trying to validate input '{text_input}': {nemuric_text}")
    print(
        f"Test invalid ingestion of string "
        f"'{text_input2}' without prior validation:"
    )
    try:
        nemuric.ingest(cast(Any, text_input2))
    except Exception as error:
        print(f"Got exception: {error}")
    myList = [1, 2, 3, 4, 5]
    nemuric.ingest(myList)
    print(f"Processing data: {myList}")
    for i in range(3):
        rank, value = nemuric.output()
        print(f"Numeric value {rank}: {value}")

    print("\n\nTesting Text Processor...")
    print(f"Trying to validate input '{int_input}': {int_res}")
    print(f"Processing data: {list_input}")
    text.ingest(list_input)

    rank, value = text.output()
    print("Extracting 1 value...")
    print(f"Text value {rank}: {value}")

    log = LogProcessor()
    log_input = log.validate(text_input)
    print("\nTesting Log Processor...")
    print(f"Trying to validate input '{text_input}': {log_input}")

    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    log.ingest(log_data)
    print(f"Extracting {len(log_data)} values...")
    for i in range(len(log_data)):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")
    testtt = TextProcessor()
    testtt.validate(42)
