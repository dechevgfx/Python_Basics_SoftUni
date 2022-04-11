name = input()

i = 1
sum_grade = 0
bad_grades_counter = 0

while i <= 12 and bad_grades_counter != 2:
    temp_grade = float(input())
    if temp_grade >= 4:
        sum_grade += temp_grade
        i += 1
    else:
        bad_grades_counter += 1

if bad_grades_counter == 2:
    print(f"{name} has been excluded at {i} grade")
else :
    avg = sum_grade / 12
    print(f"{name} graduated. Average grade: {avg:.2f}")