prev_reading = int(input())  
curr_reading = int(input())  
if curr_reading >= prev_reading:
    volume = curr_reading - prev_reading
else:
    volume = (10000 - prev_reading) + curr_reading

if volume <= 300:
    cost = 21.00  
if volume>300 and volume <= 600:
    cost = 21.00 + (volume - 300) * 0.06
if volume > 600 and volume <= 800:
    cost = 21.00 + 300 * 0.06 + (volume - 600) * 0.04
if volume > 800:
    cost = 4.00 + 300 * 0.06 + 200 * 0.04 + (volume - 800) * 0.025
average_price = cost / volume



print(f"{volume:.2f}")
print(f"{cost:.2f}")
print(f"{average_price:.2f}")
