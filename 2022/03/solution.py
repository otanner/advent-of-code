#!/usr/bin/env python3
import string


def get_priority(letter):
    return (string.ascii_lowercase + string.ascii_uppercase).find(letter) + 1


def main():
    with open('input.txt') as inp:
        p1_priorities = []
        p2_priorities = []
        group = []
        for line in inp.readlines():
            line = line.strip()

            # part 1
            first, second = set(line[:len(line)//2]), set(line[len(line)//2:])

            p1_priorities.append(get_priority(first.intersection(second).pop()))

            # part 2
            group.append(line)

            if len(group) < 3:
                continue

            # all elfs are here
            p2_priorities.append(get_priority(set(group[0]).intersection(set(group[1]), set(group[2])).pop()))
            group = []

    print(sum(p1_priorities))
    print(sum(p2_priorities))


if __name__ == '__main__':
    main()
