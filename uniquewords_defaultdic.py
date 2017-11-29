import collections
import sys
import string

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"

for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1

for word in sorted(words):
    print("'{}' appears {} time".format(word, words[word]))
