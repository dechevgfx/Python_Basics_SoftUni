balance = 0

while True:
    comm = input()

    if comm == 'NoMoreMoney':
        break
    elif float(comm) < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {float(comm):.2f}')
    balance += float(comm)

print(f'Total: {balance:.2f}')
