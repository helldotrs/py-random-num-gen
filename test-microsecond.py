from datetime import datetime

for a in range(10):
    current_time = datetime.now()
    microseconds_rightmost_digit = current_time.microsecond % 10

    print("run " + str(a)                    +" results:")
    print("current_time:"                    + str(current_time))
    print("current_time.microsecond:"        + str(current_time.microsecond))
    print("microseconds_rightmost_digit:"    + str(microseconds_rightmost_digit))
    
