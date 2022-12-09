#!/usr/bin/env python3
import pathlib


def main():
    path = pathlib.PurePath('/')
    dir_sizes = {}

    with open('input.txt') as inp:
        for line in inp.readlines():
            line = line.strip()

            match line.split():
                case ['$', 'ls']:
                    pass
                case ['$', 'cd', '..']:
                    path = path.parent
                    print(f'chdir {path.as_posix()}')
                case ['$', 'cd', directory]:
                    path = path / directory
                    print(f'chdir {path.as_posix()}')
                case ['dir', dirname]:
                    print(f'directory {dirname}')
                case [size, filename]:
                    dir_sizes.update({path: dir_sizes.get(path, 0) + int(size)})
                    for d in path.parents:
                        dir_sizes.update({d: dir_sizes.get(d, 0) + int(size)})
                    print(f'{path.as_posix()}/{filename} with {size=}')
                case _:
                    print('no match')

    # part 1
    print(sum([s for s in dir_sizes.values() if s < 100_000]))

    # part 2
    total_disk = 70_000_000
    disk_needed = 30_000_000

    disk_unused = total_disk - dir_sizes[pathlib.PurePosixPath('/')]
    large_enough_dirs = [(d.as_posix(), s) for d, s in dir_sizes.items() if s > disk_needed - disk_unused]

    print(min(large_enough_dirs, key=lambda x: x[1]))


if __name__ == '__main__':
    main()
