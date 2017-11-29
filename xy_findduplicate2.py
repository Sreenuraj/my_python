import json
import sys
from pprint import pprint
import urllib.request as ur
import os
import optparse



def getstoreid():
    usage = """%prog [options] [path1 [path2 [... pathN]]]
The paths are optional; if not given . is used."""
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-l", "--list", dest="storeid", help="supply the list of store id like : --list 2132,5232,...")
    parser.add_option("-f", "--file", dest="filename",
                      help="Give full path of the file containing store id eg: --file e://data//storeid//storeid.txt")
    opts, args = parser.parse_args()
    # print("storeid:", opts.storeid)
    stores = []
    if opts.filename is not None:
        # print(opts.filename)
        for each in open(opts.filename):
            each = each.rstrip()
            stores.append(each)
    elif opts.storeid is not None:
        stores = opts.storeid.split(',')
        # return opts.storeid
    else:
        print("use help: {} '-h' or '--help'".format(sys.argv[0]))
        sys.exit()

    return stores


def findduplicate():
    allstoreid = []
    try:
        allstoreid = getstoreid()
        # print(allstoreid)
    except TypeError:
        print('no stores')

    resultfile = 'result.txt'
    if os.path.isfile(resultfile):
        os.remove(resultfile)

    for storeid in allstoreid:
        fh = open(resultfile, 'a', encoding='utf-8')
        filtered = {}
        url = "http://abc/v2/stores/"+storeid+"/mods"
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
    print('please check result.txt file for the result')

main()
