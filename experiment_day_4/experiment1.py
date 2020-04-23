import re

s1 = "Handel"
s2 = "Händel"
s3 = "Haendel"


regex = "H(ä|ae?)ndel"

if (re.match(regex, s2) != None):
    print("Pattern Matched")
else:
    print("Pattern Not Matched")