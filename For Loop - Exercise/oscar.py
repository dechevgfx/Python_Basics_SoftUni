name_act = input()
points = float(input())
jury_count = int(input())
nominee = False
for current_grade in range(jury_count):
    name = input()
    temp_point = float(input())
    points += len(name) * temp_point / 2
    if points > 1250:
        print(f'Congratulations, {name_act} got a nominee for leading role with {points:.1f}!')
        nominee = True
        break

if not nominee:
    needed_points = 1250.5 - points
    print(f'Sorry, {name_act} you need {needed_points:.1f} more!')