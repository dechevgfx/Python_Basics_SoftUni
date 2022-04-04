pages = int(input())
pages_for_hour = int(input())
days = int(input())
total_hours = pages / pages_for_hour
needed_hours = total_hours / days

print(round(needed_hours))


