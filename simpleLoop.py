#!/usr/bin/python3
import time

userValue = int(input("Enter an integer: "))

n = userValue
steps = 0
while n != 1:
  if 0 == n % 2:
    n = n /2
  else:
    n = n * 3 + 1
  print("Current value: " + str(n))
  steps += 1
  time.sleep(0.25);

print(f'Done! We reached 1 in {steps} steps!')