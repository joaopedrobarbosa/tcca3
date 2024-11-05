# main.py
from parser import parser


def main():
    with open("program.bahia", "r", encoding="utf-8") as f:
        data = f.read()
    parser.parse(data)


if __name__ == "__main__":
    main()
