#!/bin/bash

#Simple script to run your smb enumeration step.
#Automatically outputs to smbenum_<IP>.txt

#Defines ip variable as the first argument
ip="$1"

#Check if IP was given. -z means "is null". -n means "is not null". This is saying, if there is a value for IP then check to see if it matches the correct format for IP addresses. elif ! [[ expresion ]] is negating the test condition of matching the regex with $ip.
if [ -z $ip ]; then
	echo "[*] Simple SMB Enumeration Script"
	echo "[*] Usage: sudo $0 <ip address>"
	exit 0
elif ! [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
	echo "[*] That's not a valid IP address"
	echo "[*] Usage: sudo $0 <ip address>"
	exit 0
fi

printf "Starting with NMAP"

#Start the visual wait command.
while true;do echo -n .;sleep 1;done &

#Run through enumeration steps.
#The echo -e command allows me to print a new line when sending the text.
echo -e "=== === === === === === NMAP === === === === === ===\n" > smbenum_$ip.txt
nmap -p 139,445 --script=smb-vuln* $ip >> smbenum_$ip.txt
printf "NMAP complete, moving to enum4linux\n"

echo -e "\n\n  === === === === === === ENUM4LINUX === === === === === ===\n" >> smbenum_$ip.txt
enum4linux -a $ip >> smbenum_$ip.txt 

#Complete the visual wait command and echo step.
kill $!; trap 'kill $!' SIGTERM

#The enum4linux creates random printings of ^[[##m so I deleted anything that matches that string before the file is CATed out.
#Created regex with: https://regexr.com/

sed 's/\^\[\[([0-9]|([0-9][0-9]))m//g' smbenum_$ip.txt

printf "\n\n"
printf "Done your file is right below!"
printf "\n\n"
sleep 3
cat smbenum_$ip.txt
