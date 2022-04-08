budget = float(input())
stat = int(input())
dress_price = float(input())

price_of_decor = budget * 0.10
costs = stat * dress_price
needed_money = costs + price_of_decor
if stat > 150:
    costs *= 0.9
needed_money = costs + price_of_decor
difference = abs(needed_money - budget)

if needed_money <= budget:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")