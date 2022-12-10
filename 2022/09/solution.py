#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def touching(self, other):
        return abs(self.x - other.x) < 2 and abs(self.y - other.y) < 2


def main():
    head_track = []
    head_track.append(Position(x=0, y=0))

    with open('input.txt') as inp:
        for line in inp.readlines():
            line = line.strip()

            match line.split():
                case ['L', dist]:
                    for _ in range(int(dist)):
                        last_pos = head_track[-1:][0]
                        head_track.append(Position(x=last_pos.x - 1, y=last_pos.y))
                case ['R', dist]:
                    for _ in range(int(dist)):
                        last_pos = head_track[-1:][0]
                        head_track.append(Position(x=last_pos.x + 1, y=last_pos.y))
                case ['U', dist]:
                    for _ in range(int(dist)):
                        last_pos = head_track[-1:][0]
                        head_track.append(Position(x=last_pos.x, y=last_pos.y + 1))
                case ['D', dist]:
                    for _ in range(int(dist)):
                        last_pos = head_track[-1:][0]
                        head_track.append(Position(x=last_pos.x, y=last_pos.y - 1))
                case _:
                    print('no match')

    follow_tracks = {0: head_track}

    for i in range(1, 10):
        follow_tracks.update({i: [Position(x=0, y=0)]})

    for i, tail_track in follow_tracks.items():
        if i == 0:
            continue
        current_head_track = follow_tracks[i-1]

        for pos in current_head_track:
            last_pos = tail_track[-1:][0]
            if pos.touching(last_pos):
                tail_track.append(last_pos)
            else:
                x_movement = ([-1, 1][last_pos.x < pos.x]) if last_pos.x != pos.x else 0
                y_movement = ([-1, 1][last_pos.y < pos.y]) if last_pos.y != pos.y else 0
                tail_track.append(Position(x=last_pos.x + x_movement, y=last_pos.y + y_movement))

    print(len(set(follow_tracks[1])))
    print(len(set(follow_tracks[9])))


if __name__ == '__main__':
    main()
