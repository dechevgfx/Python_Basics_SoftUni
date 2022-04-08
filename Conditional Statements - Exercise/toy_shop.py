holiday_price = float(input())
puzzels = float(input())
dolls = float(input())
teddy_bears = float(input())
minions = float(input())
trucks = float(input())

total_toys = puzzels + dolls + teddy_bears + minions + trucks
total_bill = puzzels * 2.60 + dolls * 3 + teddy_bears * 4.10 + minions * 8.20 + trucks * 2.00

if total_toys >= 50:
    total_bill = total_bill * 0.75

total_bill = total_bill * 0.9
difference = abs(total_bill - holiday_price)

if total_bill >= holiday_price:
    print(f"Yes! {difference:.2f} lv left.")

else:
    print(f"Not enough money! {difference:.2f} lv needed.")