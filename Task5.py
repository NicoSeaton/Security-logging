#5. Compare the results from the Webserver’s log and those from the SSH
#logs and create a new text file with a new entry describing the
#correlation of both events.

import re #Imports regular expressions to be used later

authFile = open('auth.log', 'r').read().split('\n') #creates a variable which is an open file
accessFile = open('access.log', 'r').read().split('\n') #creates another variablde which is an open file
authList = [] #creates a lsit to be used later
accessList = [] #creates another list to be used later

for entry1 in authFile: #Creates a variable for looking for entries
          authIps = re.findall(r'[0-9]+(?:\.[0-9]+){3}', entry1) #look for IPS within the file and call it authIPS
          for ip1 in authIps: #for each IP we find
                      authList.append(ip1) #Update our list to contain all the IPS

for entry2 in accessFile: #Creates a variable for looking for entries
          accessIps = re.findall(r'[0-9]+(?:\.[0-9]+){3}', entry2) #look for IPS within the file and call it accessIPS
          for ip2 in accessIps: #for each IP we find
                      accessList.append(ip2) #Update our list to contain all the IPS


suspectIP = list(set(authList).intersection(accessList))#Creates a set of of those lists from earlier
#where ever the lsits contained the same information it corss references them and writes that information down
with open('auth.log', 'r') as infile: #Opens up the auth log file
    for line in infile: #For every line in the file
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', line) #Look for IPS 
        if suspectIP == ip: #If the line contains the suspicious IP from earlier
            print(line) #print that line with the suspicious IP


with open('correlation.txt', 'w') as fileWrite: #Opens a new file to write information to
    fileWrite.write('\n'+'{}\n'.format(line))#writes out the lines with the suspicious IP in it to a text file





