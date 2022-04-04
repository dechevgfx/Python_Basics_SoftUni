nylon = 1.50
paint = 14.50
thinner_liquid = 5.00

nylon_quantity = int(input())
paint_quantity = int(input())
thinner_quantity = int(input())
working_hours = int(input())

nylon_price = nylon * (nylon_quantity + 2)
paint_price = paint * (paint_quantity * 1.1)
thinner_price = thinner_liquid * thinner_quantity

total_price = nylon_price + paint_price + thinner_price + 0.40
working_price = (total_price * 0.30) * working_hours

total = total_price + working_price

print(total)