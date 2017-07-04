##################################
# AUTHOR : KELVIN                #
# https://github.com/vousmeevoyez#
# TITLE : INSERTION SORT         #
##################################

import time
import random

start_time = time.time()

def generate_random_number(amount):
	return random.sample(range(1,int(amount)+1), int(amount))

def insertionsort(l):
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

amount = input('How many number do you want to sort : ')
data = generate_random_number(amount)
insertionsort(data)
print data
print time.time() - start_time, "Seconds"
print "Written By KELVIN - https://github.com/vousmeevoyez"
