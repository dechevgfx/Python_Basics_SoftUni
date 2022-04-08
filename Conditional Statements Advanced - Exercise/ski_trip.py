
days = int(input())
typeOfHousing = (input())
feedback = input()
nights = int(days - 1)
price = 0
if days < 10:
    if typeOfHousing == "room for one person":
        price = 18.00 * nights
    elif typeOfHousing == "apartment":
        price = 25 * 0.70 * nights
    elif typeOfHousing == "president apartment":
        price = 35 * 0.90 * nights
elif 10 <= days <= 15:
    if typeOfHousing == "room for one person":
        price = 18.00 * nights
    elif typeOfHousing == "apartment":
        price = 25 * 0.65 * nights
    elif typeOfHousing == "president apartment":
        price = 35 * 0.85 * nights
else:
    if typeOfHousing == "room for one person":
        price = 18.00 * nights
    elif typeOfHousing == "apartment":
        price = 25 * 0.50 * nights
    elif typeOfHousing == "president apartment":
        price = 35 * 0.80 * nights
if feedback == "positive":
    price = price * 1.25
elif feedback == "negative":
    price = price * 0.90

print(f"{price:.2f}")