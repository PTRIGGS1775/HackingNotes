# Linux Commands 

### Housekeeping
Update kali linux
`sudo apt update && apt upgrade`  
When installing new tools recommend installing them into the opt directory  
`cd /opt`  
Find anything on your machine:

`find / -name “what you want to find” 2>&1 | grep -v "Permission denied"`

Find any tool or binary on a linux machine

`locate {binary}` 
Copy output to clipboard: 
`{command} | xclip -selection -clipboard`

### Network Commands
List all networks  
`ip a`  
List wireless commands  
`iwconfig`  
List networked neighbors in the mac table  
`ip n`
List routing information  
`ip r`  
List open ports  
`netstat -tulpn`  

### Services
Start or stop any service  
`sudo service [service] start/stop`  
Start or stop any service at bootup  
`sudo systemctl enable/disable [service]`
Start a web service for reasons...  
`sudo service apache2 start`  
Start a web service without apache   
`python3 -m http.server [port]`  





