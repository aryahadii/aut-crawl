import sys
import getopt


def main(argv=None):
    if argv is None:
        argv = sys.argv
    opts, args = getopt.getopt(argv[1:], "u", ["url"])


if __name__ == '__main__':
    sys.exit(main())
