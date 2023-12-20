import datetime
import os
import sys


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


total = ""

#run for loop 48k times
for _ in range(48000):
    total += str(int(gen_rand_bool()))

#export total to file
with open(os.path.join(sys.path[0], "rand-bool-flip-loop_48k_export.txt"), "w") as file:
    file.write(total)

print("done")
sys.exit()