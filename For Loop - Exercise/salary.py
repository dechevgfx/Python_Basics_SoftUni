open_tabs = int(input())
current_salary = int(input())
is_have_salary = True

for i in range(1, open_tabs + 1):
    current_tabs = (input())
    if current_tabs == "Facebook":
        current_salary -= 150
    if current_tabs == "Instagram":
        current_salary -= 100
    if current_tabs == "Reddit":
        current_salary -= 50
if current_salary <= 0:
    is_have_salary = False
    print(f'You have lost your salary.')
if is_have_salary:
    print(int(current_salary))
