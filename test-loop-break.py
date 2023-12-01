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
