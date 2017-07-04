###################################
# AUTHOR : KELVIN 	     	  #
# CHINESE REMAINDER DIVISION 	  #
# https://github.com/vousmeevoyez #
###################################
import time

start_time = time.time()

def chinese_remainder(n, a):

    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
a = []
n = []
stopper = False

while stopper == False :
	input_a = input('Please input a (dividend): ')
	input_n = input('Please input n (divisor): ')
	print "%d mod %d" % (input_a, input_n)
	status = raw_input('do you want to continue y/n : ')
	if status != 'y' :
		stopper = True

	a.append(input_a)
	n.append(input_n)

print chinese_remainder(n,a)
print time.time() - start_time, "Seconds"
print "Written By KELVIN - https://github.com/vousmeevoyez"
