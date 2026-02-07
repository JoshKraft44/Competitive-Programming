import sys

# Evaluate the WFF in prefix form starting at position i.
# Returns: (value, next_index)
def eval_wff(expr: str, i: int, env: dict) -> tuple[int, int]:
    c = expr[i]

    # Variables
    if c in "pqrst":
        return env[c], i + 1

    # NOT (unary)
    if c == "N":
        v, j = eval_wff(expr, i + 1, env)
        return (1 - v), j

    # Binary operators: K, A, C, E
    # Parse left operand, then right operand (both are WFFs)
    left, j = eval_wff(expr, i + 1, env)
    right, k = eval_wff(expr, j, env)

    if c == "K":      # and
        return (left & right), k
    if c == "A":      # or
        return (left | right), k
    if c == "C":      # implies: w -> x is false only when w=1 and x=0
        return ((1 - left) | right), k
    if c == "E":      # equals: true if same
        return (1 if left == right else 0), k

    # Should not happen for valid input
    raise ValueError(f"Unknown symbol: {c}")


def is_tautology(expr: str) -> bool:
    vars_list = ["p", "q", "r", "s", "t"]

    # Try all 2^5 = 32 assignments
    for mask in range(32):
        env = {}
        for idx, v in enumerate(vars_list):
            # Bit idx of mask decides the variable's value (0/1)
            env[v] = (mask >> idx) & 1

        val, next_i = eval_wff(expr, 0, env)

        # For a valid WFF, we should consume the entire string
        # (Not strictly required, but nice sanity check)
        # if next_i != len(expr): ...

        if val == 0:
            return False

    return True


def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "0":
            break
        print("tautology" if is_tautology(line) else "not")


if __name__ == "__main__":
    main()