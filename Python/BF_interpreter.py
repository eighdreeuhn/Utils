from itertools import product
from re import *

BEST   = 0
WINNER = ''
TOKENS = "+_<>.[]"


def brainfuck_programs(length=9):
    chars = "+-<>[]."
    for program in product(chars, repeat=length):
        p = ''.join(program)
        if p[0] in "[]." or p.count('[') != p.count(']'):
            continue
        yield p


def beaver_hunt():
    gen = brainfuck_programs()
    for program in gen:
        run_bf(program)


def run_bf(code):
    global BEST, WINNER
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
        if ptr >= 4000 or ptr < 0:
            return 0
        if idx == len(code):
            return steps
        match code[idx]:
            case '+':
                tape[ptr] = (tape[ptr] + 1) % 256
            case '-':
                tape[ptr] = (tape[ptr] - 1) % 256
        continue


beaver_hunt()
