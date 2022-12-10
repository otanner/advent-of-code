#!/usr/bin/env python3


def main():
    x_register = 1
    cycle_count = 0

    x_register_values = []

    with open('input.txt') as inp:
        for line in inp.readlines():
            line = line.strip()

            match line.split():
                case ['noop']:
                    cycle_count += 1
                    x_register_values.append(x_register)
                case ['addx', value]:
                    cycle_count += 1
                    x_register_values.append(x_register)
                    cycle_count += 1
                    x_register_values.append(x_register)
                    x_register += int(value)
                case _:
                    print('no match')

    # part 1
    print(sum([
        x_register_values[19]*20,
        x_register_values[59]*60,
        x_register_values[99]*100,
        x_register_values[139]*140,
        x_register_values[179]*180,
        x_register_values[219]*220,
    ]))

    # part 2
    row = []
    for i, reg_value in enumerate(x_register_values):
        row_cycle = i % 40

        if not row_cycle:
            print(''.join(row))
            row = []

        if reg_value - 1 <= row_cycle <= reg_value + 1:
            row.append('#')
        else:
            row.append('.')

    print(''.join(row))


if __name__ == '__main__':
    main()
