starting_int = int(input())
final_int = int(input())
magic_num = int(input())
comb = 0
condition = False
for i in range(starting_int, final_int + 1):
    for x in range(starting_int, final_int + 1):
        comb += 1
        if i + x == magic_num:
            condition = True
            print(f"Combination N:{comb} ({i} + {x} = {magic_num})")
            break
    if condition:
        break

if not condition:
    print(f"{comb} combinations - neither equals {magic_num}")