import time
import random

# epoch time: relative to January 1, 00:00 AM, 1970, UTC
right_now = time.time()
a_little_later = time.time()
a_little_later - right_now

# time tuple
now = time.localtime()
print(now)
now[6]
now.tm_wday

# formatting time
time.strftime("%m/%d/%Y", now)
time.strftime("%d/%m/%Y", now)
time.strftime("%d-%m-%Y", now)
time.strftime("%A %B %d, %Y", now)

tomorrow_str = "04/30/2025"
tomorrow = time.strptime(tomorrow_str, "%m/%d/%Y")
print(tomorrow)

bday = "06/13/2008"
bday_time = time.strptime(bday, "%m/%d/%Y")
bday_time.tm_wday

# time out with sleep()
time.sleep(1)
for num in range(10):
    print(num)
    time.sleep(1)

# checking code running time
start = time.process_time()
for _ in range(1_000_000):
    result = random.randint(1, 1000) ** 3
stop = time.process_time()

stop - start
