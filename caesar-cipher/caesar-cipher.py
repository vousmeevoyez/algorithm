###################################
# AUTHOR : KELVIN 	          #
# TITLE : CAESAR CIPHER	     	  #
# https://github.com/vousmeevoyez #
###################################
import time

start_time = time.time()
def caesarcipher(s, k, decode = False):
	if decode: k = 26 - k
	return "".join([chr((ord(i) - 65 + k) % 26 + 65)
	for i in s.upper()
		if ord(i) >= 65 and ord(i) <= 90 ])
msg = raw_input('Please input string text')
print msg
enc = caesarcipher(msg, 11)
print "Encrypt -> %s" % enc
print caesarcipher(enc, 11, decode = True)
print time.time() - start_time, "Seconds"
print "Written by KELVIN - https://github.com/vousmeevoyez"
