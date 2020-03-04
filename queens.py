#!/usr/bin/env python3

import random

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(nextX - state[i]) in (0, nextY- i):
             return True
    return False

def queens(num, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num -1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length= len(solution)):
        return '. '*(pos) + 'X '+'. '*(length -pos-1)
    for pos in solution:
        print(line(pos))

def main():
    prettyprint(random.choice(list(queens(8))))

if __name__ == '__main__':
    main()
