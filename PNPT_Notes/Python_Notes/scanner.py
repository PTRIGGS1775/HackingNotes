#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
#Could also could look to use regex to ensure the ip address is valid
if len(sys.argv) == 2: #Includes the filename as one of the args
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4

else:
    print('Invalid amount of arguments.')
    print('Syntax: python3 scanner.py <ip>')
    sys.exit()  #Added this line to allow the program to exit without throwing a traceback error.

#Add a banner
print('-' * 40) #The simplification for adding the lines is a real nice touch.
print('Scanning target: ' + target)
print('Time started: ' + str(datetime.now()))
print('-' * 40)

try:
    for port in range(1,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #Error indicator in python for connection. If open returns 0 if closed returns 1.
        if result == 0:
            print(f'Port {port} is open')
        s.close()

except KeyboardInterrupt:
    print('\nExiting program.')
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved.')
    sys.exit()

except socket.error:
    print('Could not connect')
    sys.exit()

except NameError:
    print('\nRead the error above')
    sys.exit()
