# Active Recon

## NMAP Scans 
**Host Discovery**\
`nmap -sn 10.10.10.0/24`\
`sudo arp-scan -l`

**Initial Scans**\
`sudo nmap -sC -sV -oA {directory}/{directory}  10.10.10.242`

**Fast Scans**\
`nmap -Pn -sV 10.10.28.104 -p- > scan1.txt`

## One Liner scan scripts 
### Linux 
Scan 1 system for a range of ports using Netcat:\
`for i in {20..65535}; do nc -nzvw1 192.168.65.20 $i 2>&1 & done | grep -E 'succ|open$'`

Scan 1 system for a range of ports using /DEV/TCP:\
`for p in {1..1023}; do(echo >/dev/tcp/10.0.0.104/$p) >/dev/null 2>&1 && echo "$p open"; done`

Scan a range of IPs for specific ports using Netcat:\
`for i in {1..254}; do nc -nvzw1 192.168.65.$i 20-23 80 2>&1 & done | grep -E 'succ|open$'`

Ping scan a range of IPs:\
`for i in {1..254}; do (ping -c 1 172.16.249.$i | grep "bytes from" &) ; done`

### Windows 
`for /l %i in (1,1,254) do @ping -n 1 -w 100 172.16.249.%i | findstr "Reply"`

# Individual Service Enumeration
## HTTP/S (80, 8080, 443)
### Method
> First things first need to run my [httpenum script](https://github.com/PTRIGGS1775/HackingNotes/blob/main/tools/httpenum.sh):
> - I set this as an alias so all I need to do is type `httpenum` into my CLI and it will run.
> 
> This script runs the NMAP scripting engine for HTTP, Nikto, and goBuster. You can do these things individually with:
> - Nmap:
> `sudo nmap -p 80 --script=http-enum.nse <IP>`
> - goBuster (see below)
> - Nikto:
> `nikto -host <IP>`
>
> Second thing is to review the webpage itself. Method:
> 1. Review page and subdomains
> 2. Review source code
> 3. Use burpsuite to see what kind of responses you see.

### goBuster Scans
Also be aware that you can use different wordlists as well as look up different hosts with the VHOSTs option in gobuster, this allows you to find things suchs as secrets.htb.local from just having htb.local also known as subdomains.
- Basic\
`sudo gobuster dir -u http://IP  -t 50 -w /usr/share/dirb/wordlists/common.txt  -o busted.txt -x php,sh,txt,py`
- Intense\ 
`sudo gobuster dir -u http://IP  -t 50 -w /usr/share/dirb/wordlists/big.txt  -o intensebusted.txt -x php,sh,txt,py`
- Seclists\ 
`sudo gobuster dir -u http://IP  -t 50 -w /usr/share/seclists/Discovery/Web-Content/CGIs.txt -s '200,204,301,302,307,403,500' -e`

## SMB (139, 445)
### Method
> TCM recommends searching metasploit to review smb scanning information
> My method would be to run some automatic commands first and then do the process of manual entry. 
> Automatic commands are enum4linux and nmap. I've put these into a script like my httpenum script for convenience: [smbenum](https://github.com/PTRIGGS1775/HackingNotes/blob/main/tools/smbenum.sh) and created the alias smbenum.

### SMBClient 
Logging in without info\
`smbclient --no-pass -L //<IP>`

If you omit the pwd, it will be prompted. With --pw-nt-hash, the pwd provided is the NT hash.\
`smbclient -U '<username>[%passwd]' -L [--pw-nt-hash] //<IP>`

### SMBMap 
Null User\
`smbmap -H <IP> -P <PORT>`

Credentials\
`smbmap -u "<username>" -p "<password>" -H <IP> -P <PORT>`

Pass-the-Hash\
`smbmap -u "<username>" -p "NT:LM" -H <IP> -P <PORT>`

### CrackMapExec 
Null User\
`crackmapexec smb <IP> -u ' ' -p ' ' --shares`

Credentials\
`crackmapexec smb <IP> -u '<username>' -p '<password>' --shares`

Pass-the-Hash\
`crackmapexec smb <IP> -u '<username>' -H '<HASH>' --shares`
