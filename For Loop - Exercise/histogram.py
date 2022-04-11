n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for numbers in range (n):
    x = int(input())
    if x < 200:
        p1 += 1
    elif x < 400:
        p2 += 1
    elif x < 600:
        p3 += 1
    elif x < 800:
        p4 += 1
    else:
        p5 += 1

p1tot = p1 / n * 100
p2tot = p2 / n * 100
p3tot = p3 / n * 100
p4tot = p4 / n * 100
p5tot = p5 / n * 100

print(f'{p1tot:.2f}%')
print(f'{p2tot:.2f}%')
print(f'{p3tot:.2f}%')
print(f'{p4tot:.2f}%')
print(f'{p5tot:.2f}%')