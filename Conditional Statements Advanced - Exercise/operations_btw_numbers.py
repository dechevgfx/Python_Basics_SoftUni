N1 = int(input())
N2 = int(input())
op = input()
result = 0

if op == "+":
    result = N1 + N2
    if result % 2 == 0:
        print(f"{N1} {op} {N2} = {result} - even")
    else:
        print(f"{N1} {op} {N2} = {result} - odd")
elif op ==  "-":
    result = N1 - N2
    if result % 2 == 0:
        print(f"{N1} {op} {N2} = {result} - even")
    else:
        print(f"{N1} {op} {N2} = {result} - odd")
elif op == "*":
    result = N1 * N2
    if result % 2 == 0:
        print(f"{N1} {op} {N2} = {result} - even")
    else:
        print(f"{N1} {op} {N2} = {result} - odd")
if op == "/":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 / N2
        print(f"{N1} {op} {N2} = {result:.2f}")
if op == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    else:
        result = N1 % N2
        print(f"{N1} {op} {N2} = {result}")
