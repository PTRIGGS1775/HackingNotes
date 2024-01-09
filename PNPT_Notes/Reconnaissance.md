Just a <sup>quick</sup> *test* of **Markdown**

# Passive Recon
- Physical: Location and Employee Information
- Web/Host: Target Validation, Finding Subdomains, Fingerprinting, Data Breaches

## OSINT
**This section is about looking for social information about the company**

### Finding Email accounts
[hunter.io](https://hunter.io)\
[phonebook.cz](https://phonebook.cz) Prints out usernames in URL that you can Curl and pull info.\
[Clearbit extension](https://clearbit.com/) Better to download as an extension in Chrome. Lets you sort by role.\

### Gathering Breached Credentials
You can use gathered credentials to create a word list to streamline password cracking. Additionally, you should be looking for patterns. You may be able to target individuals of a company and potentially reuse passwords from personal accounts on target system.\
The following options below are just options, you should be thinking about the methodology.\
[MaverickAdams Github](https://github.com/hmaverickadams) Download his tool called breach-parse.\
[Dehashed](https://dehashed.com/login) Let's you search on various fields to see where else that information is used.\

### Finding subdomains passively
Separate from enumerating with something like gobuster there are sites and tools that you can find subdomains with minimal lag time. Note these tools are probably not as effective for HackTheBox or ProvingGrounds.\
[CertificateSearch](https://crt.sh) provides a series of different levels based on certificate fingerprinting all from a web portal.\
sublist3r searches various databases for subdomains from the CLI\
`sublist3r -d [domain.com]`
