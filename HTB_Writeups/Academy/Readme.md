# Academy

<h1 align=center>
    <br>
    <a href=https://app.hackthebox.com/machines/Academy><img src=images/img.png alt=Academy></a>
    <br>
</h1>

***

__Machine IP__:
```bash
10.129.50.111
```
__Date__: 2024-01-22

***

# Nmap

![](images/nmap.png)
```bash
sudo nmap -sC -sV 10.129.50.111 > Academy/nmap_10.129.50.111
```
The first NMAP scan gave us SSH open and HTTP open.

## SSH
Looking at **OpenSSH 8.2p1 Exploit** on google turns up zero results. But we'll store this as a possible route for later.

## HTTP
### Initial Review
- For HTTP to work we'll need to add academy.htb to our /etc/hosts file.
- After adding the file I ran my httpenum script and while that ran i reviewed what the website looked like.
![](images/webpage.png)
- Interesting and meta page here. View source isn't pulling anything unique, but you can register a fake account to login. This brings you to a page that looks like HTB, but none of the links appear to redirect anywhere.
- Scan results for `httpenum` returned very little. Only a possible admin.php directory and that the server is Apache/2.4.41.
- Reviewing that version of apache led me to [this](https://blog.qualys.com/vulnerabilities-threat-research/2021/10/27/apache-http-server-path-traversal-remote-code-execution-cve-2021-41773-cve-2021-42013) possible exploit, but my attempts to replicate in burpsuite were unsuccessful, likely because there is not an available cgi-bin directory.

### Burpsuite
- Initial use of burpsuite didn't return any meaninful results on repeater, and intruder didn't take for a small brute force on usernames 'admin' and root'. Or so I thought...
- Lets look at the register feature
# You need to add the methodology of checking other PHP directories especially if its only login or register.



