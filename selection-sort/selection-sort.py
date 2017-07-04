##################################
# AUTHOR : KELVIN		 #
# TITLE : SELECTION SORT         #
# https://github.com/vousmeevoyez#
##################################

import random
import time

start_time = time.time()

def generate_random_number(amount):
	return random.sample(range(1,int(amount)+1),int(amount))

def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i,len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst

amount = input('How many number do you want to generate? : ')
data = generate_random_number(amount)
result = selection_sort(data)
print result
print time.time() - start_time, "Seconds"
print "Written By KELVIN - https://github.com/vousmeevoyez"
