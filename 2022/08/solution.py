#!/usr/bin/env python3
import numpy as np


def main():
    arr = []

    with open('input.txt') as inp:
        for line in inp.readlines():
            line = line.strip()

            arr.append(list(map(int, line)))

    nparr = np.asarray(arr)

    # part 1
    trees_seen = 0
    it = np.nditer(nparr, flags=['multi_index'])

    for tl in it:
        y, x = it.multi_index

        north = np.all(nparr.T[x, :y] < tl)
        east = np.all(nparr.T[x+1:, y] < tl)
        south = np.all(nparr.T[x, y+1:] < tl)
        west = np.all(nparr.T[:x, y] < tl)

        if np.any([north, east, south, west]):
            trees_seen += 1

    print(trees_seen)

    # part 2
    scenic_score = 0
    it = np.nditer(nparr, flags=['multi_index'])

    for tl in it:
        y, x = it.multi_index

        def calc_distance(trees):
            if np.all(trees < tl):
                return len(trees)

            return (min(np.argwhere(trees >= tl)) + 1)[0]

        north = np.flip(nparr.T[x, :y])
        east = nparr.T[x+1:, y]
        south = nparr.T[x, y+1:]
        west = np.flip(nparr.T[:x, y])

        scenic_score = max(scenic_score, calc_distance(north) * calc_distance(east) * calc_distance(south) * calc_distance(west))

    print(scenic_score)


if __name__ == '__main__':
    main()
