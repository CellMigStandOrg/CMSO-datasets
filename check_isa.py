import os
import glob

import isatools.io.isatab_parser as isatab_parser


def main():
    for d in glob.glob("cmso*/isa"):
        print("validating %s" % d)
        rec = isatab_parser.parse(os.path.abspath(d))
        assert hasattr(rec, "metadata")


if __name__ == "__main__":
    main()
