from math import floor
hour_exam = int(input())
min_exam = int(input())
hour_arrive = int(input())
min_arrive = int(input())
exam_in_minutes = hour_exam * 60 + min_exam
arrive_in_minutes = hour_arrive * 60 + min_arrive

if arrive_in_minutes > exam_in_minutes:
    print("Late")
    diff = arrive_in_minutes - exam_in_minutes
    if diff >= 60:
        h = diff // 60
        min = diff % 60
        if min < 10:
            print(f"{h}:0{min} hours after the start.")
        else:
            print(f"{h}:{min} hours after the start.")
    else:
        min = diff % 60
        print(f"{min} minutes after the start.")
elif exam_in_minutes - arrive_in_minutes <= 30:
    print("On time")
    diff = exam_in_minutes - arrive_in_minutes
    if diff != 0:
        min = diff % 60
        print(f"{min} minutes before the start.")
else:
    print("Early")
    diff = exam_in_minutes - arrive_in_minutes
    if diff >= 60:
        h = diff // 60
        min = diff % 60
        if min < 10:
            print(f"{h}:0{min} hours before the start.")
        else:
            print(f"{h}:{min} hours before the start.")
    else:
        min = diff % 60
        print(f"{min} minutes before the start.")
