count_groups = int(input())
musala = 0
montblanc = 0
kilimajaro = 0
k2 = 0
everest = 0
total = 0
for i in range(count_groups):
    people = int(input())
    total += people

    if people <= 5:
        musala += people
    elif people >= 6 and people <= 12:
        montblanc += people
    elif people >= 13 and people <= 25:
        kilimajaro += people
    elif people >= 26 and people <= 40:
        k2 += people
    else:
        everest += people
musala_pr = musala / total * 100
montblanc_pr = montblanc / total * 100
kilimajaro_pr = kilimajaro / total * 100
k2_pr = k2 / total * 100
everest_pr = everest / total * 100

print(f'{musala_pr:.2f}%')
print(f'{montblanc_pr:.2f}%')
print(f'{kilimajaro_pr:.2f}%')
print(f'{k2_pr:.2f}%')
print(f'{everest_pr:.2f}%')