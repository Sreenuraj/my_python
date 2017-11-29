import sys

if len(sys.argv) < 2:
    print("usage:grep_enumerate.py 'searchstring 'filename'")

word = sys.argv[1]
for filename in sys.argv[2:]:
    for lineno, line in enumerate(open(filename), start=1):
        if word in line:
            print("{} {} {:.40}".format(filename, lineno, line.rstrip()))