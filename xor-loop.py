import datetime

test = True
strength = 16
def gen_rand_bool():
    flip_value = 0
    output     = 0
    
    for a in range(strength):
        if test:
            print("---range loop itr.---")
        while True: #xor loop
            time_value = datetime.datetime.now().microsecond % 10
            flip_value = 1 - flip_value

            if test:
                print("xor loop itr. var: output: " + str(output) + ". time_value: " + str(time_value) + ". flip_value: " + str(flip_value) + ". ")

            if not time_value: 
                output = output != flip_value
                break

    return output

for _ in range(10):
    print(gen_rand_bool())

print(gen_rand_binary())


