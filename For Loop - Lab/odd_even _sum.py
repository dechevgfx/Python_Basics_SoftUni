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
    print(f'Diff = {diff}')