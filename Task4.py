from itertools import groupby #importing groupby for use later
import re #Imports the use of regular expressions

with open('auth.log') as myAuthlog: #Opens the auth.log file as the variable myAuthlog
    myAuthlog = (line for line in myAuthlog if "Failed password for" in line) #Goes through each line in myAuthlog and searches for "Failed password for"
    for key, group in groupby(myAuthlog, key = lambda x: x[:9] + re.search('from(.+?) port', x).group(1)): #Groups the specified information based on characteristics in this attacks per hour per day

        print ("%d attacks an hour on %s"% (len(list(group)), key)) #Prints out the attacks per hour per day
