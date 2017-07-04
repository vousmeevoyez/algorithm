################################## 
# AUTHOR : KELVIN		 #
# TITLE : BUBBLE SORT            # 
# https://github.com/vousmeevoyez#
##################################

import time
import random

start_time = time.time()

def generate_random_number(amount):
	return random.sample(range(1,int(amount)+1),int(amount))

def bubblesort(seq):
    changed = True
    while changed:
        changed = False
        for i in xrange(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return seq

amount = input('How many number do you want to sort? ')
data = generate_random_number(amount)
print bubblesort(data)
print time.time() - start_time, "Seconds"
print "WRITTEN BY KELVIN - https://github.com/vousmeevoyez"
