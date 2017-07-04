##################################
# AUTHOR : KELVIN 	         #
# TITLE : CYCLE SORT	         #
# https://github.com/vousmeevoyez#
##################################
import time
import random

start_time = time.time()

def generate_random_number(amount):
	num_list = random.sample(range(1,int(amount)+1),int(amount))
	return num_list

def cyclesort(vector):
    "Sort a vector in place and return the number of writes."
    writes = 0
 
    # Loop through the vector to find cycles to rotate.
    for cycleStart, item in enumerate(vector):
 
        # Find where to put the item.
        pos = cycleStart
        for item2 in vector[cycleStart + 1:]:
            if item2 < item:
                pos += 1
 
        # If the item is already there, this is not a cycle.
        if pos == cycleStart:
            continue
 
        # Otherwise, put the item there or right after any duplicates.
        while item == vector[pos]:
            pos += 1
        vector[pos], item = item, vector[pos]
        writes += 1
 
        # Rotate the rest of the cycle.
        while pos != cycleStart:
 
            # Find where to put the item.
            pos = cycleStart
            for item2 in vector[cycleStart + 1:]:
                if item2 < item:
                    pos += 1
 
            # Put the item there or right after any duplicates.
            while item == vector[pos]:
                pos += 1
            vector[pos], item = item, vector[pos]
            writes += 1
 
    return writes
amount = input('How many number do you want to sort')
x = generate_random_number(amount)
xcopy = x[::]
writes = cyclesort(xcopy)
if xcopy != sorted(x):
	print "Wrong Order!"
else :
	print ('%r\nIs correctly sorted using cycleSort to''\n%r\nUsing %i writes.' % (x, xcopy, writes))

print time.time() - start_time, "Seconds"
print "Written By Kelvin - https://github.com/vousmeevoyez"
