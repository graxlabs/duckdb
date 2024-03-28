import sys
from query import queryFile

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path to query file>")
        sys.exit(1)

    print(queryFile(sys.argv[1]).df())
