type_ticket = input()
rows = int(input())
col = int(input())

price_per_ticket = 0
capacity = rows * col

if type_ticket == "Premiere":
    price_per_ticket = 12
elif type_ticket == "Normal":
    price_per_ticket = 7.50
else:
    price_per_ticket = 5
total = price_per_ticket * capacity
print(f"{total:.2f} leva")