# Experiment on independent occurances
# In this experiment the occurances depends upon the size of the string

import re

s1 = "aabbbbabababababa"
s2 = "abbababababababab"


# a followed by only 3 b's or more occurances of b and then followed by any number of character
regex = "ab{3}.*"

print(re.search(regex, s2))

# to be continued