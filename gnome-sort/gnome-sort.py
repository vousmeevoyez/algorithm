 #==================================#
 # AUTHOR : KELVIN                  #
 # TITLE : GNOME SORT               #
# https://github.com/vousmeevoyez   #
 #==================================#
import time
import random

start_time = time.time()

def generate_random_number(amount):
	num_list = random.sample(range(1,int(amount)+1),int(amount))
	return num_list
	
def gnomesort(array):
	i, j, size = 1,2, len(array)
	while i < size :
		if array[i-1] <= array[i]:
			i,j = j, j+1
		else:
			array[i-1],array[i] = array[i],array[i-1]
			i -= 1
			if i == 0:
				i,j = j, j+1
		#end while
	return array

amount = input('Please insert the amount of number you want to sort ')
array = generate_random_number(amount)
print gnomesort(array)
print time.time() - start_time, "seconds"
print "Code written by KELVIN - https://github.com/vousmeevoyez"
