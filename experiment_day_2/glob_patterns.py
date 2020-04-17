# glob pattern (globbing) is a kind of pattern that detects the data based on their semi matched patten...
# specify patterns having wildcard (Wikipedia)

import re

# open the file 
fopen = open("file3.txt", "r")

contents = fopen.read()


# The pattern includes kleen plus (1 or more than 1) followed by .(extention name)

# print the video files
print(re.findall(".+\.mp4", contents))

# print the java files
print(re.findall(".+\.java", contents))
