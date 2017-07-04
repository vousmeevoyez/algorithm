#################################
# AUTHOR : KELVIN               #
# TITLE : QUICKSORT             #
# https://github.com/vousmeevoyez#
#################################

import time
import random

start_time = time.time()

def generate_random_number(amount):
	num_list = random.sample(range(1,int(amount)+1),int(amount))
	return num_list

def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

amount = input('How many number do you want to sort? : ')
data = generate_random_number(amount)
print quickSort(data)
print time.time() - start_time , "Seconds"
print "Written By KELVIN - https://github.com/vousmeevoyez"
