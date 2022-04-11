import sys

number = int(input())
sum_of_el = 0
max_el = -sys.maxsize
for num in range(number):
    n = int(input())
    sum_of_el += n
    if n > max_el:
        max_el = n
if max_el == sum_of_el - max_el:
    print("Yes")
    print(f'Sum = {max_el}')
else:
    diff = abs(max_el - (sum_of_el - max_el))
    print("No")
    print(f'Diff = {diff}')