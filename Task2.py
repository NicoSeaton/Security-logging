import re #imports regular expressions to be used later
from collections import Counter #imports counter functionality to  be used later

word = "Failed password" #creates a string that I need to keep track of to look for attempts 
logf = open('auth.log', 'r').read().split('\n') #creates a variable which is an open file path
occurence = [] #creates a list called occurence which can keep track of many variables at once

for entry in logf: #creates the variable entry and something to keep track of in my open file
   if word in entry: #for those entries if they contain my specified string from earlier
       ipData = re.findall(r'[0-9]+(?:\.[0-9]+){3}', entry) #look for an Ip within the entry
       for ip in ipData: #For every IP that we find in those entries
          occurence.append(ip) #Updates the list with the new IP that we find
          Addresses = Counter(occurence) #Creates a list that tracks the number of times each IP we find was found

with open('Blacklist.txt', 'w') as Write: #Create a new text file and write to it
   for Addresses, count in Addresses.items(): #Taking into account the list of IPs we made earlier and their number of occurences
      if count >= 30: #If the occurences were more than 30
         print("IPs with more than 30 failed attempts:", Addresses) #print those Ips with more than 30 failed attempts to this program
         Write.write('Blacklisted IP: {}\n'.format(Addresses)) #Also write them out in the text file we created so we can blacklist them

print("malicious IPs listed in the blacklist file") #Writes this line so we know it has successfully blacklisted the IPs
