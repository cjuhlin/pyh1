"""Console script for pyh1."""
import argparse
import sys


def main():
    """Console script for pyh1."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "pyh1.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
