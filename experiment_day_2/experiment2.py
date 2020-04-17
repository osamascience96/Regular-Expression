import re

# open the file in read mode
fopen = open("file1.txt", "r")

# read the data in the file
contents = fopen.read()

# Experiment from Wikipedia
# At least two spaces are matched, 
# but only if they occur directly after a period (.) and before an uppercase letter.

# look behind positive at start and look a head positive(at least should be one[kleene plus]) at the end 

print(re.findall("(?<=\.) {2,}(?=[A-Z])+", contents))
