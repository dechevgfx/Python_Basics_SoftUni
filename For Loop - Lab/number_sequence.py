import sys

number = int(input())
min_number = sys.maxsize
max_number = -sys.maxsize
for i in range (number):
    current_num: int = int(input())
    if current_num > max_number:
        max_number = current_num
    if current_num < min_number:
        min_number = current_num
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')