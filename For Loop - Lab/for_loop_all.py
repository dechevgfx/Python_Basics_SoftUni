'''For-Loop LAB'''


''' 05. Character_sequence
first_name = input()
for ch in first_name:
	print(ch)'''

''' 03.Even powers of 2
number = int(input())
for num in range(number+1):
	if num % 2 == 0:
		print(2 ** num)'''

'''
count_nums = int(input())
left_sum = 0
right_sum = 0

for numbers in range(2 * count_nums):
    current_num = int(input())
    if numbers < count_nums:
        left_sum += current_num
    else:
        right_sum += current_num
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else :
    print(f"No, diff = {abs(left_sum - right_sum)}")
'''

'''
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
print(f'Min number: {min_number}')'''

''' 02.Numbers from 1 to N
num = int(input())
for numbers in range (1, num + 1, 3):
	print(numbers)'''

''' 01. Numbers from 1 to 100
for num in range (1, 101):
	print(num)'''

''' 04. Number N to 1
number = int(input())
for num in range (number, 1 - 1, -1):
	print(num)'''

'''
number = int(input())
even_sum = 0
odd_sum = 0
for num in range (number):
    current_num = int(input())
    if num % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num

if odd_sum == even_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    diff = abs(odd_sum - even_sum)
    print('No')
    print(f'Diff = {diff}')'''

'''
number = int(input())
total = 0
for i in range (number):
    current_num = int(input())
    total += current_num
print(total)'''

''' 06. Vowels sum
word = input()
sum = 0

for i in word:
    if i == 'a':
        sum += 1
    elif i == 'e':
        sum += 2
    elif i == 'i':
        sum += 3
    elif i == 'o':
        sum += 4
    elif i == 'u':
        sum += 5

print(sum)'''
