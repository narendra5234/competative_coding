import re

string = 'Wed Jan 08, 2020; 02:47:05 pm: <narendra> Hi there!'
regex = r'(\<)([<a-zA-Z]+)(\>)'
match = re.findall(regex, string)
print(match[0][1])

string = 'abbb'
regex = r'[a-z]*'
match = re.findall(regex, string)
print(match[0][1])
