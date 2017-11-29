import optparse


def main():
    usage = """%prog [options] [path1 [path2 [... pathN]]]

The paths are optional; if not given . is used."""

    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-H", "--hidden", dest="hidden",
            action="store_true",
            help=("show hidden files [default: off]"))
    parser.add_option("-m", "--modified", dest="modified",
            action="store_true",
            help=("show last modified date/time [default: off]"))
    orderlist = ["name", "n", "modified", "m", "size", "s"]
    parser.add_option("-o", "--order", dest="order",
            choices=orderlist,
            help=("order by ({0}) [default: %default]".format(
                  ", ".join(["'" + x + "'" for x in orderlist]))))
    parser.add_option("-r", "--recursive", dest="recursive",
            action="store_true",
            help=("recurse into subdirectories [default: off]"))
    parser.add_option("-s", "--sizes", dest="sizes",
            action="store_true",
            help=("show sizes [default: off]"))
    parser.set_defaults(order=orderlist[0])
    opts, args = parser.parse_args()
    if not args:
        args = ["."]
    return opts, args

main()

