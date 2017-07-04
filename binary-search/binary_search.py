import random
import time

start_time = time.time()

def generate_random_number(amount):
	return random.sample(range(1,int(amount)+1), int(amount))

def binary_search(l, value, low = 0, high = -1):
    if not l: return -1
    if(high == -1): high = len(l)-1
    if low >= high:
        if l[low] == value: return low
        else: return -1
    mid = (low+high)//2
    if l[mid] > value: return binary_search(l, value, low, mid-1)
    elif l[mid] < value: return binary_search(l, value, mid+1, high)
    else: return mid

amount = input('How many much data do you want to search? : ')
data = generate_random_number(amount)
x = input('what value are you looking?')
if x in data:
    result = "DATA FOUND"
else: 
    result = "DATA NOT FOUND"
print data
print result
print time.time() - start_time, 'Seconds'
print 'Written By KELVIN - https://github.com/vousmeevoyez'
