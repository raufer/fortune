import json

from typing import List


def write_text(text: List[str], filename: str):
    with open(filename, 'w') as f:
        for line in text:
            f.write("%s\n" % line)
    print("Written '{}'".format(filename))


def write_json(d, filename: str):
    with open(filename, 'w') as f:
        json.dump(d, f, indent=4)
    print("Written '{}'".format(filename))


def read_json(filename: str):
    with open(filename, 'r') as f:
        data = json.load(f)
    print("Read '{}'".format(filename))
    return data
