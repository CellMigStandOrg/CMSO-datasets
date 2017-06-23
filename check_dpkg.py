import glob

import datapackage


def main():
    for fn in glob.glob("cmso*/*/dp/*.json"):
        print("validating %s" % fn)
        datapackage.DataPackage(fn).validate()


if __name__ == "__main__":
    main()
