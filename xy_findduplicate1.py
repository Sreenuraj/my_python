import json
import sys
from pprint import pprint
import urllib.request as ur
import os


def getstoreid():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print("usage: {} storeid.txt".format(sys.argv[0]))
        sys.exit()
    storeid = []
    for filename in sys.argv[1:]:
        for line in open(filename, encoding='utf8'):
            line = line.rstrip()
            storeid.append(line)
    return storeid


def findduplicate():
    allstoreid = getstoreid()
    resultfile = 'result.txt'
    if os.path.isfile(resultfile):
        os.remove(resultfile)

    for storeid in allstoreid:
        fh = open(resultfile, 'a', encoding='utf-8')
        filtered = {}
        url = "http://productlocation.global.tesco.org:80/v2/stores/"+storeid+"/mods"
        response = ur.urlopen(url)
        data = json.loads(response.readall().decode('utf-8'))
        for content in data:
            value = [content]
            if content['modCode'] in filtered:
                filtered[content['modCode']] += value
            else:
                filtered[content['modCode']] = value

        if len(filtered) != 0:
            result = showresult(filtered, storeid)
            pprint(result, fh)
        fh.close()


def showresult(filtered, storeid):
    result = {}
    for each in filtered:
        if len(filtered[each]) > 1 and each is not None:
            line = "Duplicate found for mod: "+each
            # pprint(filtered[each], fh)
            result[storeid] = [line, filtered[each]]
        elif len(filtered[each]) > 1 and each is None:
            if storeid in result:
                line = str(len(filtered[each]))+' mods where NULL for store '
                result[storeid].append(line)
            else:
                result[storeid] = (str(len(filtered[each]))+' mods where NULL for store ')
    return result


def main():
    findduplicate()
    print('done')

main()
