#######################################
# AUTHOR : KELVIN		      #
# COMB SORT			      #
# github.com/vousmeevoyez	      #
#######################################

import time
import random

start_time = time.time()

def generate_random_number(amount):
	return random.sample(range(1,int(amount)+1),int(amount))

def combsort(input):

    gap = len(input)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        swaps = False
        for i in range(len(input) - gap):
            j = i+gap
            if input[i] > input[j]:
                input[i], input[j] = input[j], input[i]
                swaps = True
 
amount = input('Please input how much number do you want to generate? : ')
number_list = generate_random_number(amount)
print number_list
combsort(number_list)
print number_list
print time.time() - start_time, "seconds"
print "written by kelvin - github.com/vousmeevoyez"
