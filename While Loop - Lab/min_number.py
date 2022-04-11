import sys

min_num = sys.maxsize

while True:
    num = input()
    if num == "Stop":
        break
    elif int(num) < min_num:
        min_num = int(num)

print(min_num)