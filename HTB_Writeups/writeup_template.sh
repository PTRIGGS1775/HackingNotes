#/bin/bash
#
#This script was written to save time when doing HTB writeups. 
#Basically you're just copying the URL and the IP once you spawn your machine to get the initial portion of your work done for you.

boxurl="$1"
ip="$2"

#Check to see that the script was run with the appropriate arguments.
if [ -z $boxurl ] | [ -z $ip ]; then
	echo "[*] Correct Usage: $0 https://app.hackthebox.com/machines/{box name} IP.IP.IP.IP"
	exit 0
elif ! [[ $boxurl =~ (https://app.hackthebox.com/machines/*) ]]; then
       	echo "[*] Correct Usage: $0 https://app.hackthebox.com/machines/{box name} IP.IP.IP.IP"
	echo "[*] If htb has changed their url for boxes you will need to re-write the script"	
elif ! [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
	echo "[*] That's not a valid IP address"
	echo "[*] Corect Usage: $0 https://app.hackthebox.com/machines/{box name} IP.IP.IP.IP"
	exit 0
fi

#This took a while to figure out, but to set the variable BOXNAME as the output of a linux command I need to make sure that its nested within $(command) a money sign and brackets. 
#I also need to make sure there are no spaces between variable equal-sign or command. 
#Otherwise if I have someing like variable= $(command) the script will execute the command while saving it to a variable.

boxname=$(cut -d '/' -f 5- <<< $boxurl)
todaydate=$(date '+%Y-%m-%d')

#Make the writeup directories
mkdir $boxname
mkdir $boxname/images

#I don't know a faster way to redirect input per line to a file so I added each echo sent to the Readme.md file ona separate line.
echo "# $boxname" > $boxname/Readme.md
echo "" >> $boxname/Readme.md
echo "<h1 align="center">" >> $boxname/Readme.md
echo "    <br>" >> $boxname/Readme.md
echo "    <a href="$boxurl"><img src="images/img.png" alt="$boxname"></a>"  >> $boxname/Readme.md
echo "    <br>" >> $boxname/Readme.md
echo "</h1>" >> $boxname/Readme.md
echo "" >> $boxname/Readme.md
echo "***" >> $boxname/Readme.md
echo "" >> $boxname/Readme.md
echo "__Machine IP__:" >> $boxname/Readme.md
echo "\`\`\`bash" >> $boxname/Readme.md
echo "$ip" >> $boxname/Readme.md
echo "\`\`\`" >> $boxname/Readme.md
echo "__Date__: $todaydate" >> $boxname/Readme.md
echo "" >> $boxname/Readme.md
echo "***" >> $boxname/Readme.md
echo "" >> $boxname/Readme.md
echo "# Nmap" >> $boxname/Readme.md
echo "" >> $boxname/Readme.md
echo "![](images/nmap.png)" >> $boxname/Readme.md
echo "\`\`\`bash" >> $boxname/Readme.md
echo "sudo nmap -sC -sV $ip > $boxname/nmap_$ip" >> $boxname/Readme.md
echo "\`\`\`" >> $boxname/Readme.md

printf "\n\n\n"
printf "============================================================================================================="
printf "\n\n"
printf "[*] The script has completed. You know have a $boxname directory with an images subdirectory.[*] You need to save your screenshot of the box as 'img.png' and the screenshot of your nmap scan as 'nmap.png' for all this hard work to be displayed.\n"
read -p "Would you like to run your nmap script? (sudo nmap -sC -sV $ip > $boxname/nmap_$ip)? " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
	#Start the visual wait command.
	while true;do echo -n .;sleep 1;done &
	sudo nmap -sC -sV $ip > $boxname/nmap_$ip
	#Complete the visual wait command and echo step.
	kill $!; trap 'kill $!' SIGTERM
fi

#This will only work without a prompt within my current environment.
#This will create issues if I do a git pull, I'll need to reset my git variables.
git add . 
git commit -m "Created directory for HTB $boxname"
git push

printf "\n\n\n"
printf "============================================================================================================="
printf "\n\n"
print "Your NMAP scan is complete and all files have been added to your github"

