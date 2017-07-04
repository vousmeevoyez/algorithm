###################################
# AUTHOR :KELVIN_	     	  #
# https://github.com/vousmeevoyez #
# BRUTE FORCE STRING MATCHING     #
###################################
import random, string
import time

start_time = time.time()

def generate_random_string(length):
	return ''.join(random.choice(string.lowercase) for i in range(length))

def brute_force_match(word, text):

	m = len(word)
	n = len(text)

	counter = 0
	
	for i in range(0, n-m+1):
		found = True
		for j in range(0, m):
			if word[j] != text[i+j]:
				found = False
				break
		if found :
			counter += 1
		
	if counter == 0:
		print "no match"

	else:
		print "the word appears : " , counter , "times!"

amount = input('Please input how much string that you want to generate? : ')
string = generate_random_string(amount)
print string
word = raw_input('Please input text that you want to search')

brute_force_match(word, string)
print time.time() - start_time, "seconds"
print "Written By Kelvin - https://github.com/vousmeevoyez"
