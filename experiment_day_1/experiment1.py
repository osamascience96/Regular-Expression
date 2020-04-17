import re

# open the file 
file = open("file1.txt", "r")

# read the contents from the file 
contents = file.read()

# find the characters starting from a followed by any character....
print(re.findall("a.", contents)) 

# find only those chars that has ha followed by any characer
print(re.findall("ha.", contents))
