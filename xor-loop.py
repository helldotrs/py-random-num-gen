import datetime

TEST = True
STRENGTH = 16


def gen_rand_bool():
    flip_value = 0
    output     = 0
    
    for a in range(STRENGTH):
        if TEST:
            print("---range loop itr.---")
        while True: #xor loop
            time_value = datetime.datetime.now().microsecond % 10
            flip_value = 1 - flip_value

            if TEST:
                print("xor loop itr. var: output: " + str(output) + ". time_value: " + str(time_value) + ". flip_value: " + str(flip_value) + ". ")

            if not time_value: 
                output = output != flip_value
                break

    return output
    
if TEST:
    i = 0
for _ in range(10):
    if TEST:
        i += 1
        print(i)
    print(gen_rand_bool())



