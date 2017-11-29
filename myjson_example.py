import json
from pprint import pprint

file = "E:\\Perl_WD\\json\\test.json"

with open(file) as json_file:
    data = json.load(json_file)

filtered = {}

for content in data:
    value = [content]
    #   for each in filtered:
    if content['modCode'] in filtered:
        filtered[content['modCode']] += value
    else:
        filtered[content['modCode']] = value

    # print(filtered)

for each in filtered:
    if len(filtered[each]) > 1:
        print("duplicate found for :", each)
        pprint(filtered[each])

