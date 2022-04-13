sums = float(input())
sums = int(sums * 100)
coin_counter = 0
coin_counter += sums // 200
sums %= 200
coin_counter += sums // 100
sums %= 100
coin_counter += sums // 50
sums %= 50
coin_counter += sums // 20
sums %= 20
coin_counter += sums // 10
sums %= 10
coin_counter += sums // 5
sums %= 5
coin_counter += sums // 2
sums %= 2
coin_counter += sums // 1
sums %= 1
print(coin_counter)

