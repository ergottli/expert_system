import argparse

COMMENT_SYMBOL = '#'


def parse_file(data):
    for row in data:
        row = row.split(COMMENT_SYMBOL)[0].strip()
        if len(row) < 1:
            continue
        print(row)


def parse_input():
    parser = argparse.ArgumentParser(description="expert_system 21-school Moscow")
    parser.add_argument('-v', help='visualizer', action='store_true')
    parser.add_argument('-i', help='interactive mode', action='store_true')
    parser.add_argument('file', help='input file', type=argparse.FileType('r'))

    args = parser.parse_args()
    data = args.file.readlines()
    parse_file(data)


if __name__ == '__main__':
    parse_input()
