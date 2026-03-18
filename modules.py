import os
import math

cwd = os.getcwd()
print("Current working directory:", cwd)

num = int(input("Enter an integer: "))
log_val = math.log2(num)

print(f"Log base 2 of {num} is: {log_val}")
print("Floor:", math.floor(log_val))
print("Ceiling:", math.ceil(log_val))