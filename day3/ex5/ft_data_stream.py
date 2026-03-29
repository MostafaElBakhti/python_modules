import typing
import random


player: list = ["Alice", "Bob", "Ali"]
action: list = ["move", "grab", "drink"]

def gen_event() :
    while True:
        pla = random.choice(player)
        act = random.choice(action)
        yield (pla,act)

g = gen_event()
for i in range(1000):
    pla,act = next(g)
    print(f"Event {i}: Player {pla} did action {act}")
events_list = []
g2 = gen_event()
for i in range(10):
    events_list.append(next(g2))

def consume_event(events_list):
    while len(events_list) > 0:
        index = random.randint(0, len(events_list) - 1)
        removed = events_list.pop(index)
        yield removed

g3 = consume_event
print(f"Built list of 10 events: {events_list}")

for event in consume_event(events_list):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {events_list}")





