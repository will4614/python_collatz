#!/usr/bin/python3
import time
import random

# https://github.com/will4614/python_collatz

# ask the user for an integer
userValue = int(input("Enter an integer: "))

# preserve the user's value
n = userValue
steps = 0

# loop until we hit 1
while 1 != n:

  if 0 == n % 2:
    # even
    n = n / 2
  else:
    # odd
    n = n * 3 + 1.0

  # update the user on our progress
  print("Current value: " + str(n))

  # count our steps
  steps += 1

  # pause for a quarter second
  # time.sleep(0.25);

  # pause for a random amount of time less than 1 second
  time.sleep(random.random());

# give the user the final result
print(f'Done! We reached 1 from {userValue} in {steps} steps!')