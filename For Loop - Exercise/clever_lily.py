age = int(input())
washMachine = float(input())
priceOfToy = int(input())
toyCount = 0
currentMoney = 10
income = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        income += currentMoney
        currentMoney += 10
        income -= 1
    else:
        toyCount += 1
totalMoney = toyCount * priceOfToy + income
diff = abs(washMachine - totalMoney)

if totalMoney >= washMachine:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
