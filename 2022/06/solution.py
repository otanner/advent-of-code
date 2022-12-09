#!/usr/bin/env python3


def get_marker_position(line, *, marker_length):
    for pos in range(len(line)-marker_length):
        if len(set(line[pos:pos+marker_length])) == marker_length:
            return pos + marker_length

    return 0


def main():
    with open('input.txt') as inp:
        for line in inp.readlines():
            line = line.strip()

            # part 1
            print(get_marker_position(line, marker_length=4))

            # part 2
            print(get_marker_position(line, marker_length=14))


if __name__ == '__main__':
    main()
