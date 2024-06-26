# Passive Recon
- Gather information to help inform password attcks and login information 
- Passive information gathering activities should be focused on identifying IP addresses, (sub)domains, finding external partners and services, the types of technologies used and any other useful information (including the names of employees working at the company, e-mail addresses, websites, customers, naming conventions, E-mail & VPN systems and sometimes even passwords). 

# SEMI-PASSIVE 
- Access the site like a regular user to determine what technology is used. 
- Go to the top left of kali and select frameworks to choose from OSINT frameworks you can use.

## Finding Email accounts
1. [hunter.io](https://hunter.io)
2. [phonebook.cz](https://phonebook.cz) Prints out usernames in URL that you can Curl and pull info.
3. [Clearbit extension](https://clearbit.com/) Better to download as an extension in Chrome. Lets you sort by role.
4. [ReconNG](https://github.com/lanmaster53/recon-ng/wiki/Getting-Started) | Powerful tool that requires some money to use API keys to harvest emails.
5. TheHarvester | Use emails to be able to target individuals in the company. | d=domain, b=data-source, l=limit-results 
    - `theHarvester -d cisco.com -b yahoo -l 100`

## Gathering Breached Credentials
You can use gathered credentials to create a word list to streamline password cracking. Additionally, you should be looking for patterns. You may be able to target individuals of a company and potentially reuse passwords from personal accounts on target system.

The following options below are just options, you should be thinking about the methodology.
1. [MaverickAdams Github](https://github.com/hmaverickadams) Download his tool called breach-parse.
2. [Dehashed](https://dehashed.com/login) Let's you search on various fields to see where else that information is used.
3. [GitLeaks](https://github.com/zricethezav/gitleaks) | Find leaks in github, you can also do a filename:users search on the github page.
4. [Sripted breach scraper website](scylla.sh) | Use this after looking at breached credentials.

## Finding subdomains passively
Separate from enumerating with something like gobuster there are sites and tools that you can find subdomains with minimal lag time. Note these tools are probably not as effective for HackTheBox or ProvingGrounds. However, these are likely good for bug bounties.
1. [CertificateSearch](https://crt.sh) provides a series of different levels based on certificate fingerprinting all from a web portal.
2. sublist3r searches various databases for subdomains from the CLI.
    - `sublist3r -d [domain.com] -t 100`
3. Install [**OWASP AMASS**](https://github.com/OWASP/Amass)

## Identifying Website Technology
1. [BuiltWith](https://builtwith.com) | Use this to see what technology runs behind the website.
2. [Wappalyzer](https://wappalyzer.com) | This is more of a semi-passive type of recon, but is used as an extension in your browser. 
3. [NetCraft](https://searchdns.netcraft.com) | Provides a site report including technology.
4. [HTTPSec](https://securityheaders.com) | Analyze HTTP response headers and provide basic analysis of security posture.

## Google Hacking
- For more help visit the [GoogleDorking-Database](https://www.exploit-db.com/google-hacking-database)
- Leverage standard boolean logic to narrow results. Use wildcards *.
1. site:  #Used to narrow the site and find subdomains by stripping wwww
2. filetype:  #used to specify any file. 
3. -filetype: #used to negate filetypes 
4. intitle:“index of” “parent directory”   #Used to find incorrectly configured pages 
5. intext: #Used to find information in the page like "password"
6. inurl: #Helps narrow down the list.
7. Don't forget to use 'Advanced Search'

## Social Media
1. [citizenevidence](https://citizenevidence.amnestyuse.org) | Provides metadata of videos 
2. [searchftps](https://searchftps.net) | lets you search FTP sites 
3. [peakyou](https://peakyou.com) | searches information about specific people 
4. [followerwonk](https://followerwonk.com) | More social media searches
5. [shodan](https://www.shodan.io/) | Crawls devices connected to the internet like websites, servers, and IoT. 
6. **sherlock** |  Python3 tool for searching peoples social media presence. `sherlock username`
7. [namecheck](https://www.namechk.com) | Helps you find taken usernames.
8. Platform Specific (in general most SM platforms have locked down so OSINT is limited):
    - Twitter:
        - Use 'from:' in the search bar to see all posts/responses
        - Use 'to:' to find people talking to the individual
        - 'since:' and 'until:' to filer timeline
        - 'geocode:{code},{distance in km} 'with copied geocodes from google
        - https://github.com/rmdir-rp/OSINT-twitter-tools
    - Facebook:
        - Videos only demonstrated basic search feature of facbook.
        - Tool: https://sowsearch.info
        - Tool: https://intelx.io/tools?tab=facebook
        - `ctrl + u` on a user page then find 'user id:'
    - Instagram:
        - Search for the person and resort to image OSINT
        - Tool: https://imginn.com/
        - For the profile ID, right click and click "View page source". Then search for "profilePage_"
    - Snapchat:
        - map.snapchat.com
    - Reddit:
        - More google fu. Don't forget to check a user's post and comment history.
    - Linkedin:
        - Just review their pages.

## Image OSINT
- Reverse Image Search
    - images.google.com to upload the image and find source.
    - tineye.com is a different tool, but same function.
- Viewing EXIF Data
    - jimpl.com. Drag and drop image.
- Command line
    - Basic usage: `exiftool <img>`
    - To save to a file: `exiftool <img> > file.txt`

## People OSINT (Hate this section title)
- For other countries try seeing if the websites have different TLDs.
- Find people with whitepages.com or truepeoplesearch.com, also look at voter records.
- IP Addresses: thatsthem.com
- Phone numbers: truecaller.com or calleridtest.com or infobel.com (international) | use google and try variations of the phone number or with emojis.

## Physical Location OSINT
- Google satellite view to identify information about your location.
- If you need to figure something like this out: https://somerandomstuff1.wordpress.com/2019/02/08/geoguessr-the-top-tips-tricks-and-techniques/
- [wiglenet](https://wigle.net) used to find wifi information around a map.

## Website OSINT
- [builtwith](https://builtwith.com) to find out information about what the website is running.
- [centralops](https://centralops.net) to find out information about who bought the website
- [urlscan](https://urlscan.io) to view the behavior and content of a website without viewing it directly.
- [crt.sh](https://crt.sh) to find other websites and subdomains a website might have.
- [hunchly](https://hunch.ly) A google chrome extension that really just lets you organized captured PAI.

