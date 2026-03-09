# Tautology
# https://open.kattis.com/problems/tautology

import sys

def eval(expression: str, i: int, env: dict) -> tuple[int, int]:
    c = expression[i]

    if c in "pqrst":
        return env[c], i + 1

    if c == "N":
        v, j = eval(expression, i + 1, env)
        return (1 - v), j


    left, j = eval(expression, i + 1, env)
    right, k = eval(expression, j, env)

    if c == "K":     
        return (left & right), k
    if c == "A":  
        return (left | right), k
    if c == "C":   
        return ((1 - left) | right), k
    if c == "E":  
        return (1 if left == right else 0), k

    return "Character not found"


def is_tautology(expression: str) -> bool:
    vars_list = ["p", "q", "r", "s", "t"]

    for values in range(32):
        env = {}
        for index, v in enumerate(vars_list):
            env[v] = (values >> index) & 1

        val, next_i = eval(expression, 0, env)

        if val == 0:
            return False

    return True


for line in sys.stdin:
    line = line.strip()
    if line == "0":
        break
    if is_tautology(line): 
        print("tautology")
    else: 
        print("not")
