import re

# open the file and read it 
fopen = open("file2.txt", "r")

contents = fopen.read()

# lets use the wildcard of regular expression in a more different manner
# The text in the file2 contain wods like serialize and serialise, let match the pattern
print(re.findall("seriali[sz]e", contents))
#  it will return the array of matched partterns