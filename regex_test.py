import re

f = open('regex_test.txt')

data = f.readlines()

name_pattern = re.compile(r'[A-Z][a-z]+.+ [A-Z][a-z]+')

for i in data:
    match = name_pattern.search(i)

    if match:
        print(match.group())