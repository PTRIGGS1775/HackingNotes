Just a <sup>quick</sup> *test* of **Markdown**

# Passive Recon
- Gather information to help inform password attcks and login information 
- Passive information gathering activities should be focused on identifying IP addresses, (sub)domains, finding external partners and services, the types of technologies used and any other useful information (including the names of employees working at the company, e-mail addresses, websites, customers, naming conventions, E-mail & VPN systems and sometimes even passwords). 

## Finding Email accounts
1. [hunter.io](https://hunter.io)\
2. [phonebook.cz](https://phonebook.cz) Prints out usernames in URL that you can Curl and pull info.\
3. [Clearbit extension](https://clearbit.com/) Better to download as an extension in Chrome. Lets you sort by role.\
4. [ReconNG](https://github.com/lanmaster53/recon-ng/wiki/Getting-Started) | Powerful tool that requires some money to use API keys to harvest emails.\
5. TheHarvester | Use emails to be able to target individuals in the company. | d=domain, b=data-source, l=limit-results 
    - `theHarvester -d cisco.com -b yahoo -l 100`\

## Gathering Breached Credentials
You can use gathered credentials to create a word list to streamline password cracking. Additionally, you should be looking for patterns. You may be able to target individuals of a company and potentially reuse passwords from personal accounts on target system.\
The following options below are just options, you should be thinking about the methodology.\
1. [MaverickAdams Github](https://github.com/hmaverickadams) Download his tool called breach-parse.\
2. [Dehashed](https://dehashed.com/login) Let's you search on various fields to see where else that information is used.
3. [GitLeaks](https://github.com/zricethezav/gitleaks) | Find leaks in github, you can also do a filename:users search on the github page.

## Finding subdomains passively
Separate from enumerating with something like gobuster there are sites and tools that you can find subdomains with minimal lag time. Note these tools are probably not as effective for HackTheBox or ProvingGrounds. However, these are likely good for bug bounties.\
1. [CertificateSearch](https://crt.sh) provides a series of different levels based on certificate fingerprinting all from a web portal.\
2. sublist3r searches various databases for subdomains from the CLI\
    - `sublist3r -d [domain.com] -t 100`\
3. Install [**OWASP AMASS**](https://github.com/OWASP/Amass)

## Identifying Website Technology
1. [BuiltWith](https://builtwith.com) | Use this to see what technology runs behind the website.
2. [Wappalyzer](https://wappalyzer.com) | This is more of a semi-passive type of recon, but is used as an extension in your browser. 
3. [NetCraft](https://searchdns.netcraft.com) | Provides a site report including technology.
4. [HTTPSec](https://securityheaders.com) | Analyze HTTP response headers and provide basic analysis of security posture.

## Google Hacking

