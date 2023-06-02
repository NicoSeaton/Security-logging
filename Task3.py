from itertools import groupby #importing groupby for use later
import re #importing regular expressions for use later

with open('auth.log') as myAuthlog: #open auth log file 
    myAuthlog = (line for line in myAuthlog if "Failed password for" in line) #takes the lines that contain failed password for from the log file
    for key, group in groupby(myAuthlog, key = lambda x: x[:9]): #Groups the specified information based on two sets of characteristics in this case attacks and time
        print ("%d attacks an hour on %s"% (len(list(group)), key)) #prints put the number of attacks per hour
