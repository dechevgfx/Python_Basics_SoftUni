destination = input()
savings = 0
while destination != 'End':
    budget = float(input())
    while savings < budget:
        money = float(input())
        savings += money
        if savings >= budget:
            print(f"Going to {destination}!")
            break
    savings = 0
    destination = input()
