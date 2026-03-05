def ft_water_remind() -> None:
    Days = int(input("Days since last watering: "))

    if Days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


ft_water_remind()
