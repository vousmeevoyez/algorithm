#################################
# AUTHOR : KELVIN               #
# TITLE : COCKTAILSORT          #
#https://github.com/vousmeevoyez#
#################################

import time
import random

start_time = time.time()

def generate_random_number(amount):
	num_list = random.sample(range(1,int(amount)+1),int(amount))
	return num_list

def cocktailSort(A):
    up = range(len(A)-1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if A[i] > A[i+1]:  
                    A[i], A[i+1] =  A[i+1], A[i]
                    swapped = True
            if not swapped:
                return

amount = input('How many number do you want to sort? : ')
data = generate_random_number(amount)
cocktailSort(data)
print data
print time.time() - start_time , "Seconds"
print "Written By KELVIN - https://github.com/vousmeevoyez"
