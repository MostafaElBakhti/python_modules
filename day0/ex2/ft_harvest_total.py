def ft_harvest_total() -> None:
    total = 0
    for i in range(3):
        weight = int(input(f"Day {i+1} harvest: "))
        total += weight
    print(f"Total harvest: {total}")


ft_harvest_total()
