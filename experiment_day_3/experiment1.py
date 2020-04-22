import re

fopen = open("file1.txt", "r")

contents = fopen.read()


# picked from wikipedia
# matches eccess of whitespace at the beginning or the end of the line 

# The regular expression reads only the first line, due to ^ beg and $end
# regex for this experiment
regex = "^[ \t]+|[ \t]+$" # space + 4 space (5 spaces) at the beg or end

print(re.findall(regex, contents))