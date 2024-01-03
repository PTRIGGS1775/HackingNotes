#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2: #Includes the filename as one of the args
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4

else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
