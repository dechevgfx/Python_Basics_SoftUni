score = int(input())
bonus = 0.0
if score <= 100:
    bonus = 5
elif score < 1000:
    bonus = score * 0.20
else:
    bonus = score * 0.1

if score % 2 == 0:
    bonus += 1
elif score % 10 == 5:
    bonus += 2


print(bonus)
print(score + bonus)
