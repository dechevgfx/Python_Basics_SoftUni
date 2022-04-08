record = float(input())
distance_meters = float(input())
time_in_sec_for_one_m = float(input())
delay = distance_meters // 15 * 12.5
timeIvan = distance_meters * time_in_sec_for_one_m + delay
if timeIvan < record:
    print(f"Yes, he succeeded! The new world record is {timeIvan:.2f} seconds.")
else:
    diff = abs(timeIvan - record)
    print(f'No, he failed! He was {diff:.2f} seconds slower.')
