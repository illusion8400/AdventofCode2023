

TIME = []
DISTANCE= []

EXTIME= []
EXDISTANCE= []

winners_count = []
count = 0
for time_allowed in TIME:
    max_distance = DISTANCE[(TIME.index(time_allowed))]
    winning_speeds = []
    for speed in range(1,time_allowed):
        turns_left = time_allowed - speed
        total_speed = speed * turns_left 
        if total_speed > max_distance:
            winning_speeds.append(speed)
            continue
        else: continue
    print(len(winning_speeds))
    winners_count.append(len(winning_speeds))
total = 1
for x in winners_count:
    total = total * x
print(total)
    
   
    
#     winning_speeds.append(count)
#     # print(len(winning_speeds))
#     # break

# print(f"Margin of error: {int(winning_speeds[0]) * int(winning_speeds[1])*int(winning_speeds)}")