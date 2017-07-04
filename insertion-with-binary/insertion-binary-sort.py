############################################
# AUTHOR : KELVIN                          #
# TITLE: INSERTION SORT WITH BINARY SEARCH #
# https://github.com/vousmeevoyez          #
############################################

import time
import random

start_time = time.time()

def generate_random_number(amount):
	return random.sample(range(1,int(amount)+1), int(amount))

def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        # invariant: ``seq[:i]`` is sorted        
        # find the least `low' such that ``seq[low]`` is not less then `key'.
        #   Binary search in sorted sequence ``seq[low:up]``:
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1              
            else:
                up = middle
        # insert key at position ``low``
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]

amount = input('How much number do you want to sort? : ')
data = generate_random_number(amount)
insertion_sort_bin(data)
print data
print time.time() - start_time, "Seconds"
print "WRITTEN BY KELVIN - https://github.com/vousmeevoyez"
