deposit = float(input())
term = int(input())
interest_rate = float(input())

interest = deposit * (interest_rate / 100)
rate_for_one_month = interest / 12
total_sum = deposit + term * rate_for_one_month

print(total_sum)