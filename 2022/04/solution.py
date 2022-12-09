#!/usr/bin/env python3


def get_section(start, end):
    return set(range(int(start), int(end) + 1))


def main():
    p1_amount = 0
    p2_amount = 0
    with open('input.txt') as inp:
        for line in inp.readlines():
            line = line.strip()

            elf1, elf2 = line.split(',')
            sections1 = get_section(*elf1.split('-'))
            sections2 = get_section(*elf2.split('-'))

            # part 1
            if sections1.issubset(sections2) or sections2.issubset(sections1):
                p1_amount += 1

            # part 2
            if len(sections1.intersection(sections2)) > 0:
                p2_amount += 1

    print(p1_amount)
    print(p2_amount)


if __name__ == '__main__':
    main()
