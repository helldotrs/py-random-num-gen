import datetime
import time

while True:
    current_time = datetime.datetime.now()
    microseconds_rightmost_digit = current_time.microsecond % 10

    print(f"Microseconds rightmost digit: {microseconds_rightmost_digit}")

    if microseconds_rightmost_digit == 0:
        print("Breaking the loop.")
        break

    # Optionally, add a small delay to avoid excessive CPU usage
    time.sleep(0.1)
"""
output:
$ python3 test-loop-break.py
Microseconds rightmost digit: 9
Microseconds rightmost digit: 1
Microseconds rightmost digit: 6
Microseconds rightmost digit: 5
Microseconds rightmost digit: 2
Microseconds rightmost digit: 2
Microseconds rightmost digit: 4
Microseconds rightmost digit: 3
Microseconds rightmost digit: 4
Microseconds rightmost digit: 6
Microseconds rightmost digit: 0
Breaking the loop.
"""
