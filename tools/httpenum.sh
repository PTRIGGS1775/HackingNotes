#!/bin/bash

#Simple script to run your http enumeration step.
#Automatically outputs to httpenum_<IP>_<PORT>.txt

#Defines ip variable as the first argument
ip="$1"
#Sets the port default value:
port="${2:-80}"

#Check if IP was given. -z means "is null". -n means "is not null". This is saying, if there is a value for IP then check to see if it matches the correct format for IP addresses. elif ! [[ expresion ]] is negating the test condition of matching the regex with $ip.
if [ -z $ip ]; then
	echo "[*] Simple HTTP Enumeration Script"
	echo "[*] Usage: sudo $0 <ip address> <port optional>"
	exit 0
elif ! [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
	echo "[*] That's not a valid IP address"
	echo "[*] Usage: sudo $0 <ip address> <port optional>"
	exit 0
fi

#Start the visual wait command.
while true;do echo -n .;sleep 1;done &

#Run through enumeration steps.
#The echo -e command allows me to print a new line when sending the text.
echo -e "=== === === === === === NMAP === === === === === ===\n" > httpenum_$ip\_$port.txt
nmap -p $port --script=http-enum.nse $ip >> httpenum_$ip\_$port.txt
printf "NMAP complete, moving to NIKTO"

echo -e "\n\n  === === === === === === NIKTO === === === === === ===\n" >> httpenum_$ip\_$port.txt
nikto -host $ip -port $port >> httpenum_$ip\_$port.txt

#Complete the visual wait command and echo step.
kill $!; trap 'kill $!' SIGTERM
echo "NIKTO done, now on to GOBUSTER!"

#Enumerate with gobuster, already uses progress bar.
#Small if condition to enable usage of different ports.
echo -e "=== === === === === === GOBUSTER === === === === === ===\n" >> httpenum_$ip\_$port.txt
if [ -z $2 ]; then
	gobuster dir -u http://$ip/ -t 50 -w /usr/share/dirb/wordlists/common.txt -x php,sh,txt,py  >> httpenum_$ip\_$port.txt
else
	gobuster dir -u http://$ip:$port -t 50 -w /usr/share/dirb/wordlists/common.txt -x php,sh,txt,py  >> httpenum_$ip\_$port.txt
fi

printf "\n\n"
printf "Done your file is right below!"
printf "\n\n"
cat httpenum_$ip\_$port.txt
