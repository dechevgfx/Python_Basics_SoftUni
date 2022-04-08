from math import ceil
movie = str(input())
episode_duration = float(input())
brake_duration = float(input())
time_for_rest = brake_duration / 4
timeForLunch = brake_duration / 8
total_time_reserved = timeForLunch + time_for_rest
freeTimeOfBrake = brake_duration - total_time_reserved

if episode_duration <= freeTimeOfBrake:
    diff = abs((episode_duration + total_time_reserved) - brake_duration)
    print(f"You have enough time to watch {movie} and left with {ceil(diff)} minutes free time.")
else:
    diff = abs(brake_duration - (episode_duration + total_time_reserved))
    print(f"You don't have enough time to watch {movie}, you need {ceil(diff)} more minutes.")