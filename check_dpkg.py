import glob

from biotracks.validation import Validator


def main():
    validator = Validator()
    for fn in glob.glob("cmso*/*/dp/*.json"):
        print("validating %s" % fn)
        validator.validate(fn)


if __name__ == "__main__":
    main()
