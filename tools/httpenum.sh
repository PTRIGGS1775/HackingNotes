#!/bin/bash

#Simple script to run your http enumeration step.
#Automatically outputs to httpenum_<IP>.txt

#Check if IP was given
if [ -z "$1" ]; then
	echo "[*] Simple HTTP Enumeration Script"
	echo "[*] Usage: sudo $0 <ip address>"
	exit 0
fi

#Start the visual wait command.
while true;do echo -n .;sleep 1;done &

#Run through enumeration steps.
echo "====================NMAP====================" > httpenum_$1.txt
nmap -p 80 --script=http-enum.nse $1 >> httpenum_$1.txt

#Complete the visual wait command and echo step.
kill $!; trap 'kill $!' SIGTERM
echo "NMAP done, now on to GOBUSTER!"

#Enumerate with gobuster, already uses progress bar.
printf "\n\n"
echo "==================GOBUSTER==================" >> httpenum_$1.txt
gobuster dir -u http://$1/ -t 50 -w /usr/share/dirb/wordlists/common.txt -x php,sh,txt,py  >> httpenum_$1.txt
echo "Done your file is right below!"
cat httpenum_$1.txt
