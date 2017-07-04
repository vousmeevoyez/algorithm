import time
import random

start_time = time.time()

def generate_first_part():
	first_digit = random.randint(1,99)
	return first_digit

def generate_second_part():
	middle = 0 
	while middle == 0:
		middle1 = random.randint(0,9)
		middle2 = random.randint(0,9)
		middle3 = random.randint(0,9)
		middle = 100*middle1 + 10*middle2 + middle3
	return middle

def generate_third_part():
	return ''.join(map(str,random.sample(range(10),4)))

def generate_msisdn():
	fixed = '+628'
	first = generate_first_part()
	second = generate_second_part()
	third = generate_third_part()
	telco = classify_telco(first)
	return fixed + '{}-{}-{}'.format(first,second,third) + '- %s'%(telco)

def classify_telco(a):
	operator = ''
	if 11 <= a <= 13 or 21 <= a <= 23 or 52 <= a <= 54:
		operator = 'Telkomsel'
	elif 14 <= a <= 16 or 55 <= a <= 58:
		operator = 'Indosat'
	elif 17 <= a <= 19 or a == 59 or 77 <= a <= 79:
		operator = 'XL'
	elif a == 28:
		operator = 'Ceria'	
	elif 31 <= a <=38 :
		operator = 'Axis'		
	elif 81 <= a <= 88:
		operator = 'Smartfren'
	elif 96 <= a <= 99:
		operator = 'Three'
	else :
		operator = 'Sorry your msisdn cant be identified'

	return operator

amount = input('Please input how many msisdn you wanna generate? : ')

for i in range(amount):
	print generate_msisdn()

print time.time() - start_time, "seconds"
print "written by kelvin - github.com/vousmeevoyez"
