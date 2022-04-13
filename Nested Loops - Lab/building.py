x = int(input())
y = int(input())
room_nums = ""

for f in range(x, 0, -1):
    for r in range(y):
        current_room_n = f * 10 + r
        if f == x:
            print(f"L{current_room_n} ", end="")
        elif f % 2 != 0:
            room_nums += f'A{current_room_n} '
        else:
            room_nums += f'O{current_room_n} '
    print(room_nums)
    room_nums = ''