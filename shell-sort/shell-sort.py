  #==================================#
  # AUTHOR : KELVIN                  #
  # TITLE : GNOME SORT               #
  # https://github.com/vousmeevoyez  #
  #==================================#
import time
import random

start_time = time.time()
def generate_random_number(amount):
	num_list = random.sample(range(1,int(amount)+1), int(amount))
	return num_list

def shellsort(num):
    inc = len(num) // 2
    while inc:
        for i, el in enumerate(num):
            while i >= inc and num[i - inc] > el:
                num[i] = num[i - inc]
                i -= inc
            num[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)

amount = input('Please input how many number you want to sort : ')
data = generate_random_number(amount)
shellsort(data)
print data
print time.time() - start_time,"Seconds"
print 'Code written by KELVIN - https://github.com/vousmeevoyez'
