fruit = input()
day = input()
count = float(input())
total = 0

is_valid = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"
is_valid1 = day == "Saturday" or day == "Sunday"

if is_valid :
    if fruit == "banana":
        total = count * 2.50
        print(f'{total:.2f}')
    elif fruit == "apple":
        total = count * 1.20
        print(f'{total:.2f}')
    elif fruit == "orange":
        total = count * 0.85
        print(f'{total:.2f}')
    elif fruit == "grapefruit":
        total = count * 1.45
        print(f'{total:.2f}')
    elif fruit == "kiwi":
        total = count * 2.70
        print(f'{total:.2f}')
    elif fruit == "pineapple":
        total = count * 5.50
        print(f'{total:.2f}')
    elif fruit == "grapes":
        total = count * 3.85
        print(f'{total:.2f}')
    else:
        print("error")
elif is_valid1:
    if fruit == "banana":
        total = count * 2.70
        print(f'{total:.2f}')
    elif fruit == "apple":
        total = count * 1.25
        print(f'{total:.2f}')
    elif fruit == "orange":
        total = count * 0.90
        print(f'{total:.2f}')
    elif fruit == "grapefruit":
        total = count * 1.60
        print(f'{total:.2f}')
    elif fruit == "kiwi":
        total = count * 3
        print(f'{total:.2f}')
    elif fruit == "pineapple":
        total = count * 5.60
        print(f'{total:.2f}')
    elif fruit == "grapes":
        total = count * 4.20
        print(f'{total:.2f}')
    else:
        print("error")
else:
    print("error")
