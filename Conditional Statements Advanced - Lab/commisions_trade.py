
city = input()
sales = float(input())
isValid = 0 <= sales <= 500
isValid1 = 500 < sales <= 1000
isValid2 = 1000 < sales <= 10000
isValid3 = sales > 10000
finalSum = 0

if isValid:
    if city == "Sofia":
        print(f'{(0.05 * sales):.2f}')
    elif city == "Varna":
        print(f'{(0.045 * sales):.2f}')
    elif city == "Plovdiv":
        print(f'{(0.055 * sales):.2f}')
    else: print("error")
elif isValid1:
    if city == "Sofia":
        print(f'{(0.07 * sales):.2f}')
    elif city == "Varna":
        print(f'{(0.075 * sales):.2f}')
    elif city == "Plovdiv":
        print(f'{(0.08 * sales):.2f}')
    else: print("error")
elif isValid2:
    if city == "Sofia":
        print(f'{(0.08 * sales):.2f}')
    elif city == "Varna" :
        print(f'{(0.1 * sales):.2f}')
    elif city == "Plovdiv" :
        print(f'{(0.12 * sales):.2f}')
    else :
        print("error")
elif isValid3:
    if city == "Sofia" :
        print(f'{(0.12 * sales):.2f}')
    elif city == "Varna" :
        print(f'{(0.13 * sales):.2f}')
    elif city == "Plovdiv" :
        print(f'{(0.145 * sales):.2f}')
    else :
        print("error")
else:
    print("error")
