day = input()
price_one = 12
price_two = 14
price_three = 16
if day in ("Monday", "Tuesday", "Friday"):
    print(price_one)
elif day in ("Wednesday", "Thursday"):
    print(price_two)
elif day in ("Saturday", "Sunday"):
    print(price_three)
