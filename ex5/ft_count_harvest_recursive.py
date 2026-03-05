def helper(day, Total) -> None:
    if (day > Total):
        print("Harvest time!")
        return
    print(f"Day {day}")
    helper(day + 1, Total)


def ft_count_harvest_recursive() -> None:
    Days = int(input("Days until harvest: "))
    helper(1, Days)


ft_count_harvest_recursive()
