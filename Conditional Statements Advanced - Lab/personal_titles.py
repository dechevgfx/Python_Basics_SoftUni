age = float(input())
sex = str(input())

if sex == "f":
    if age < 16:
        print("Miss")
    else:
        print("Ms.")
elif sex == "m":
    if age < 16:
        print("Master")
    else:
        print("Mr.")
