# Active Recon

## NMAP Scans 
**Host Discovery**\
`nmap -sn 10.10.10.0/24`\
`sudo arp-scan -l`
**Initial Scans**\
`sudo nmap -sC -sV -oA {directory}/{directory}  10.10.10.242`\
**Fast Scans**\
`nmap -Pn -sV 10.10.28.104 -p- > scan1.txt`\

## One Liner scan scripts 
### Linux 
Scan 1 system for a range of ports using Netcat:\
`for i in {20..65535}; do nc -nzvw1 192.168.65.20 $i 2>&1 & done | grep -E 'succ|open$'`\
Scan 1 system for a range of ports using /DEV/TCP:\
`for p in {1..1023}; do(echo >/dev/tcp/10.0.0.104/$p) >/dev/null 2>&1 && echo "$p open"; done`\
Scan a range of IPs for specific ports using Netcat:\
`for i in {1..254}; do nc -nvzw1 192.168.65.$i 20-23 80 2>&1 & done | grep -E 'succ|open$'`\
Ping scan a range of IPs:\
`for i in {1..254}; do (ping -c 1 172.16.249.$i | grep "bytes from" &) ; done`\

### Windows 
`for /l %i in (1,1,254) do @ping -n 1 -w 100 172.16.249.%i | findstr "Reply"`\

# Individual Service Enumeration
## HTTP/S (80, 8080, 443)
First things first need to run my [httpenum script](https://github.com/PTRIGGS1775/HackingNotes/blob/main/tools/httpenum.sh):\
`sudo /home/kali/HackingNotes/tools/httpenum.sh <IP>`
