import datetime

TEST = False
STRENGTH = 16


def gen_rand_bool(test = False):
    flip_value = 0
    output     = 0
    
    for _ in range(STRENGTH):
        if test:
            print("-range loop itr-")
        while True: #flip loop
            time_value = datetime.datetime.now().microsecond % 10
            flip_value = 1 - flip_value

            if test:
                print("-flip loop itr- value are; output: " + str(output) + ". time_value: " + str(time_value) + ". flip_value: " + str(flip_value) + ". ")

            if not time_value: 
                output = output != flip_value
                break

    return output

if TEST:
    for i in range(10):
        print(i)
        print(gen_rand_bool(test = True))
    print("---end of test---")


