import time
import math

def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

num = 25100
delay = 2123
result = delayed_sqrt(num, delay)
print(f"Square root of {num} after {delay} miliseconds is {result}")