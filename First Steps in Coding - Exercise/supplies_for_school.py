pens = 5.80
markers = 7.20
detergent = 1.20

count_of_pens = int(input())
count_of_markers = int(input())
count_of_detergent = int(input())
discount_percent = int(input()) / 100

price_of_pens = pens * count_of_pens
price_of_markers = markers * count_of_markers
price_of_detergent = detergent * count_of_detergent

total_price_of_supplies_before_discount = (price_of_pens + price_of_markers + price_of_detergent)
total_price = total_price_of_supplies_before_discount - (total_price_of_supplies_before_discount * discount_percent)

print(total_price)

