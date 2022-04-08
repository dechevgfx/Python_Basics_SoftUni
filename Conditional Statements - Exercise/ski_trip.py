days = int(input())
type_of_housing = (input())
feedback = input()
nights = int(days - 1)
price = 0
if days < 10:
    if type_of_housing == "room for one person":
        price = 18.00 * nights
    elif type_of_housing == "apartment":
        price = 25 * 0.70 * nights
    elif type_of_housing == "president apartment":
        price = 35 * 0.90 * nights
elif 10 <= days <= 15:
    if type_of_housing == "room for one person":
        price = 18.00 * nights
    elif type_of_housing == "apartment":
        price = 25 * 0.65 * nights
    elif type_of_housing == "president apartment":
        price = 35 * 0.85 * nights
else:
    if type_of_housing == "room for one person":
        price = 18.00 * nights
    elif type_of_housing == "apartment":
        price = 25 * 0.50 * nights
    elif type_of_housing == "president apartment":
        price = 35 * 0.80 * nights
if feedback == "positive":
    price = price * 1.25
elif feedback == "negative":
    price = price * 0.90

print(f"{price:.2f}")