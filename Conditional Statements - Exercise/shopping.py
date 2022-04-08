budget = float(input())
VGA_count = int(input())
CPU_count = int(input())
RAM_count = int(input())

VGA_price = 250 * VGA_count
CPU_price = (VGA_price * 0.35) * CPU_count
RAM_price = (VGA_price * 0.10) * RAM_count

total_price = VGA_price + CPU_price + RAM_price

if VGA_count > CPU_count:
    total_price = total_price * 0.85

diff = abs(budget - total_price)

if budget >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")