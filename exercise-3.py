import re

f = open('names.txt')

data = f.readlines()

new_data_pattern = re.compile(r'(^\w+, \w+).+(@\b\w+$)')

new_data_list = []

for i in data:
    match = new_data_pattern.search(i)

    if match:
        new_data_list.append(match.group())


name_pattern = re.compile(r'(^\w+, \w+)')
twitter_pattern = re.compile(r'(@\b\w+$)')

for i in new_data_list:
    name = name_pattern.search(i)
    twitter = twitter_pattern.search(i)
    print(name.group())
    print(twitter.group())





