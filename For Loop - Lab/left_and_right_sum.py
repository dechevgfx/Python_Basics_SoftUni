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
