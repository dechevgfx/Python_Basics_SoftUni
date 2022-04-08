from math import pi

type_of_the_fig = input()
result = 0
if type_of_the_fig == "square":
    side = float(input())
    result = side * side
elif type_of_the_fig == "rectangle":
    side_a = float(input())
    side_b = float(input())
    result = side_a * side_b
elif type_of_the_fig == "circle":
    radius = float(input())
    result = pi * (radius ** 2)
else:
    side = float(input())
    height = float(input())
    result = side * height / 2

print(f"{result:.3f}")
