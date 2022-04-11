import sys

number = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
for position in range(1, number + 1):
    n = float(input())
    if position % 2 == 0:
        even_sum += n
        if n > even_max:
            even_max = n
        if n < even_min:
            even_min = n
    else:
        odd_sum += n
        if n > odd_max:
            odd_max = n
        if n < odd_min:
            odd_min = n
print(f'OddSum={odd_sum:.2f},')
if odd_min == sys.maxsize:
    print("OddMin=No,")
else:
    print(f'OddMin={odd_min:.2f},')
if odd_max == -sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax={odd_max:.2f},')
print(f'EvenSum={even_sum:.2f},')
if even_min == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f'EvenMin={even_min:.2f},')
if even_max == -sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax={even_max:.2f}')