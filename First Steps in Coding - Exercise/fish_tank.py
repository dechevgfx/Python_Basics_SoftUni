long = int(input())
wide = int(input())
height = int(input())
percent_used_space = float(input())

size_cm3 = long * wide * height
size_liters = size_cm3 / 1000
used_space = percent_used_space / 100
needed_liters = size_liters * (1 - used_space)

print(needed_liters)