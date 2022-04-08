month = input()
stay = int(input())
price_studio = 0
price_apartment = 0

if 7 < stay <= 14:
    if month == "May":
        price_studio = 50 * stay * 0.95
        price_apartment = 65 * stay
    elif month == "October":
        price_studio = 50 * stay * 0.95
        price_apartment = 65 * stay
    elif month == "June":
        price_studio = 75.20 * stay
        price_apartment = 68.70 * stay
    elif month == "September":
        price_studio = 75.20 * stay
        price_apartment = 68.70 * stay
    elif month == "July":
        price_studio = 76 * stay
        price_apartment = 77 * stay
    elif month == "August":
        price_studio = 76 * stay
        price_apartment = 77 * stay
elif stay > 14:
    if month == "May":
        price_studio = 50 * 0.70 * stay
        price_apartment = 65 * stay * 0.90
    elif month == "October":
        price_studio = 50 * 0.70 * stay
        price_apartment = 65 * stay * 0.90
    elif month == "June":
        price_studio = 75.20 * stay * 0.80
        price_apartment = 68.70 * stay * 0.90
    elif month == "September":
        price_studio = 75.20 * stay * 0.80
        price_apartment = 68.70 * stay * 0.90
    elif month == "July":
        price_studio = 76 * stay
        price_apartment = 77 * stay * 0.90
    elif month == "August":
        price_studio = 76 * stay
        price_apartment = 77 * stay * 0.90
else:
    if month == "May":
        price_studio = 50 * stay
        price_apartment = 65 * stay
    elif month == "October":
        price_studio = 50 * stay
        price_apartment = 65 * stay
    elif month == "June":
        price_studio = 75.20 * stay
        price_apartment = 68.70 * stay
    elif month == "September":
        price_studio = 75.20 * stay
        price_apartment = 68.70 * stay
    elif month == "July":
        price_studio = 76 * stay
        price_apartment = 77 * stay
    elif month == "August":
        price_studio = 76 * stay
        price_apartment = 77 * stay

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
