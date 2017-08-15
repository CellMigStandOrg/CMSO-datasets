"""\
Compare tabular files ignoring trailing whitespace and newlines.
"""

import sys
import argparse


def make_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('fn1', metavar="FILE1")
    parser.add_argument('fn2', metavar="FILE2")
    return parser


def main(argv):
    parser = make_parser()
    args = parser.parse_args(argv[1:])
    with open(args.fn1) as f1, open(args.fn2) as f2:
        while True:
            try:
                l1 = next(f1)
                l2 = next(f2)
            except StopIteration:
                break
            if l1.rstrip().split("\t") != l2.rstrip().split("\t"):
                print("files differ: %r != %r" % (l1, l2))
                return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
