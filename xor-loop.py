import datetime

strength = 16
def gen_rand_binary():
    rand_value = 0
    output     = 0
    
    for a in range(strength):
        while True: #xor loop
            time_value = datetime.datetime.now().microsecond % 10
            rand_value = 1 - rand_value
          
            if not time_value: 
                output = output - rand_value
                break

        return output

print(gen_rand_binary())
print(gen_rand_binary())
print(gen_rand_binary())
print(gen_rand_binary())
print(gen_rand_binary())
print(gen_rand_binary())
print(gen_rand_binary())
print(gen_rand_binary())


