import optparse


def main():
    usage = """%prog [options] [filename][filename1][filename'n']
We can have 'n' number of files. """
    version = '%prog-1.0'
    parser = optparse.OptionParser(usage=usage,version=version)
    parser.add_option('-q', '--qtest', dest='testing', default='sreenu',
                      help='store the testing value [default: %default]')
    parser.add_option('-t', '--true', dest='quit', action='store_true',
                      help='use it for setting true to quit')
    parser.add_option('-F', '--false', dest='quit', action='store_false', help='use it for setting true to quit')
    parser.add_option('-y', '--yes', dest='quit1', action='store_true', default=True,
                      help='use it for setting true to quit[default: %default]')
    parser.add_option("-f", "--filename", metavar="FILE", help="write output to FILE")
    parser.add_option("-m", "--mode", default="intermediate",
                      help="interaction mode: novice, intermediate or expert [default: %default]")
    parser.add_option('-i', '--integer', dest='integer', help='except only integer')

    orderlist = ["name", "n", "modified", "m", "size", "s"]
    parser.add_option("-o", "--order", dest="order",
                      choices=orderlist, help=("order by ({0}) [default: %default]".format(
            ", ".join(["'" + x + "'" for x in orderlist]))))

    # parser.parse_args()
    # print(options.testing)
    # print(args)

    group = optparse.OptionGroup(parser, "Other options", "These option are other options")
    group.add_option('-r', '--result', dest='showresult',
                     help='option if opted shows the result[default: %default]')
    group.add_option('-d', '--dead', dest='dead', help='just kill the app')

    parser.add_option_group(group)
    (options, args) = parser.parse_args()

    if options.integer != <class 'int'>:
        parser.error('not an integer')
    print(options, args)

main()
