import re

# regular expression that matches any numeral
s1 = "+923364179686.923364179689E92"
s2 = "03364179686"
s3 = ".523e-75834"

# capture the numeral
regex = "^[+-]?(\d*(\.\d+)?)([eE][+-]?\d+)?$"

if (re.match(regex, s3) != None):
    print(True)
else:
    print(False)
