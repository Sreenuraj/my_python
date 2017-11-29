import random


def getforename_surnames():
    forenames = []
    surnames = []
    for lines, filename in ((forenames, 'data/forenames.txt'),
                            (surnames, 'data/surnames.txt')):
        for line in open(filename, encoding='utf8'):
            lines.append(line.rstrip())
    return forenames, surnames


def main():
    forenames, surnames = getforename_surnames()
    fh = open('data/fullname.txt', 'w', encoding='utf8')
    for i in range(10):
        line = "{} {}\n".format(random.choice(forenames), random.choice(surnames))
        fh.write(line)

main()
