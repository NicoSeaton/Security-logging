search_str = "user=bin" #Creates a variable which is a string 
search_file = open("auth.log", "r") #Creates a variable which is an open file
count = 0 #creates a variable which is a count
for line in search_file: #Looks through every line in my specified file
    if line.strip().find(search_str) != -1: #Detects if each line contains the string variable i specified earlier
        count +=1 #If the string is detected then it increases the counters current amount by 1
        print (line) #It prints the line that is detected
print ("number of attempts " + str(count)) #Prints out the amount of times the event happened
search_file.close() #closes the file afterwards

# this entire program opens a file scans each line for the user bin and then -
#writes those lines and how many attempts there were for task 1.
          
    
