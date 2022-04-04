chicken = 10.35
fish = 12.40
vegan = 8.15

chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())

price_chicken = chicken * chicken_menus
price_fish = fish * fish_menus
price_vegan = vegan * vegan_menus

price_of_total_menus = price_chicken + price_fish + price_vegan
price_of_dessert = price_of_total_menus * 0.20

total_price = price_of_total_menus + price_of_dessert + 2.50

print(total_price)