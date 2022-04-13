number = int(input())
comb = 0
for x1 in range(number + 1):
    for x2 in range(number + 1):
        for x3 in range(number + 1):
            if x1 + x2 + x3 == number:
                comb += 1
print(comb)

