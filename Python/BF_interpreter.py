from itertools import product
from re import *

BEST   = 0
WINNER = ''
TOKENS = "+_<>.[]"


def brainfuck_programs(length=9):
    chars = "+-<>[]."
    for program in product(chars, repeat=length):
        p = ''.join(program)
        if p[0] in "[]." or "<>" in p or "><" in p or "+-" in p or "-+" in p or p.count('[') != p.count(']'):
            continue
        yield p


def beaver_hunt():
    global BEST, WINNER
    gen = brainfuck_programs()
    for i, program in enumerate(gen):
        print(program)
        result = run_bf(program)
        print(result)
        if result > BEST:
            BEST = result
            WINNER = program
            print(f"NEW LEADER: {program} CLOCKED IN AT {result} STEPS!")
    print(WINNER, BEST)


def run_bf(code):
    jump_table = {}
    stack = []
    for i, t in enumerate(code):
        if t == '[':
            stack.append(i)
        if t == ']':
            if not stack:
                return -1
            j = stack.pop()
            jump_table[i] = j
            jump_table[j] = i

    tape  = [0]*4000
    ptr   = 2000
    idx   = 0
    steps = 0
    while True:
        if ptr >= 4_000 or ptr < 0 or steps > 10_000:
            return 0
        if idx == len(code):
            return steps

        match code[idx]:
            case '+':
                tape[ptr] = (tape[ptr] + 1) % 256
            case '-':
                tape[ptr] = (tape[ptr] - 1) % 256
            case '>':
                ptr += 1
            case '<':
                ptr -= 1
            case '[':
                if not tape[ptr]:
                    idx = jump_table[idx]
            case ']':
                if tape[ptr]:
                    idx = jump_table[idx]
            case '.':
                pass

        idx += 1
        steps += 1


beaver_hunt()