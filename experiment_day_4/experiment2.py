# Experiment on dependent occurances
# In this experiment the occurances depends upon the size of the string
import re

# occur once or none
s1 = "color"
s2 = "colour"

# can be or no u
regex = "colou?r"

print(re.search(regex, s2))


# kleen star
s1 = "abbbba"
s2 = "abba"
s3 = "aa"

# 0 or more occurances

# a followed by b(0)|b(loop) and then ends at a
regex = "ab*a"

print(re.match(regex, s3))

# kleen plus
s1 = "abbbba"
s2 = "abba"
s3 = "aa"

# 1 or more occurances, but not 0

# a followed by b(1)|b(loop) and then ends at a
regex = "ab+a"

print(re.match(regex, s2))
