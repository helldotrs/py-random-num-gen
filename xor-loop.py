import datetime

strength = 16
def gen_rand_binary():
  binary = 0
  for a in range(strength):
    while True:
      current_time = datetime.datetime.now()
      binary = 1 - binary #xor

      #FIXME:
      current_time = datetime.datetime.now()
      microseconds_rightmost_digit = current_time.microsecond % 10
      if microseconds_rightmost_digit == 0:
          print("Breaking the loop.")
          break # and output binary?
