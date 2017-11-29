import json
from pprint import pprint
import urllib.request

url = "http://productlocation.global.tesco.org:80/v2/stores/2132/mods"
# req = urllib.request.Request(url)
response = urllib.request.urlopen(url)
data = json.loads(response.readall().decode('utf-8'))

filtered = {}

for content in data:
    value = [content]

    if content['modCode'] in filtered:
        filtered[content['modCode']] += value
    else:
        filtered[content['modCode']] = value

for each in filtered:
    if len(filtered[each]) > 1 and each is not None:
        print("duplicate found for :", each)
        pprint(filtered[each])

    elif len(filtered[each]) > 1 and each is None:
        print("Mode was NULL for:", len(filtered[each]), 'mods')
