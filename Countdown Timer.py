# Countdown Timer

import time

my_time = int(input("What amount of time you woud like to set: "))
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)



print("Times up")