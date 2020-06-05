import re

# \w+ matches to group of alphanumeric character.
p = re.compile('\w+')
print(p.findall("I,went#to!him at 11 A.M., he said5 *** in some_language."))

