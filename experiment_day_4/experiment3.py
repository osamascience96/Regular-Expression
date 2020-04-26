# Experiment on independent occurances
# In this experiment the occurances depends upon the size of the string

import re

s1 = "abbbabababababa"
s2 = "abbababababababab"


# a followed by only 3 b's or more occurances of b and then followed by any number of character
regex = "ab{3}.*"

print(re.match(regex, s1))

s3 = "abbbbaaaabababaaaabbba"

# a followed by 3 minimum or more than 3 occurances of b and then followed by any number of characters
regex = "ab{3,}.*"

print(re.match(regex, s3))

s4 = "abbbbbactreihewrha"

# a followed by 2 minimum or 5 maximum occurances of b and then followed by any number of characters but not b
regex = "^ab{2,5}[^b]+$"

print(re.match(regex, s4))

