import random
from typing import Generator, Tuple


player: list = [
    "Alice",
    "Bob",
    "Ali",
    "Charlie",
    "Dylan",
    "Eve",
    "Lina",
    "Noah",
    "Maya",
    "Zayd"
    ]
action: list = [
    "move",
    "grab",
    "drink",
    "run",
    "jump",
    "climb",
    "swim",
    "sleep",
    "eat",
    "hide",
    "attack",
    "defend",
    "use",
    "release",
    "explore"
    ]


def gen_event() -> Generator[Tuple[str, str], None, None]:
    while True:
        pla = random.choice(player)
        act = random.choice(action)
        yield (pla, act)


def consume_event(events_list) -> Generator[Tuple[str, str], None, None]:
    while len(events_list) > 0:
        index = random.randint(0, len(events_list) - 1)
        removed = events_list.pop(index)
        yield removed


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    g = gen_event()
    for i in range(1000):
        pla, act = next(g)
        print(f"Event {i}: Player {pla} did action {act}")

    events_list = []
    g2 = gen_event()
    for i in range(10):
        events_list.append(next(g2))

    g3 = consume_event(events_list)
    print(f"Built list of 10 events: {events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")
