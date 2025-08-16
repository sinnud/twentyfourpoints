import itertools
import operator

TARGET_SCORE = 24

ops = [
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
    ('/', operator.truediv)
]

def valid_div(x, y):
    # Only allow division if x is divisible by y (integer result, y != 0)
    return y != 0 and x % y == 0

def try_all_expressions(nums):
    # Try all permutations and operator combinations
    for num_perm in itertools.permutations(nums):
        for ops_combo in itertools.product(ops, repeat=3):
            # Try all possible parenthesis placements
            a, b, c, d = num_perm
            op1, op2, op3 = ops_combo

            # ((a op1 b) op2 c) op3 d
            try:
                first = op1[1](a, b)
                if op1[0] == '/' and not valid_div(a, b): continue
                second = op2[1](first, c)
                if op2[0] == '/' and not valid_div(first, c): continue
                result = op3[1](second, d)
                if op3[0] == '/' and not valid_div(second, d): continue
                if abs(result - TARGET_SCORE) < 1e-6:
                    expr = f"(({a} {op1[0]} {b}) {op2[0]} {c}) {op3[0]} {d}"
                    return True, expr
            except ZeroDivisionError:
                continue

            # (a op1 (b op2 c)) op3 d
            try:
                first = op2[1](b, c)
                if op2[0] == '/' and not valid_div(b, c): continue
                second = op1[1](a, first)
                if op1[0] == '/' and not valid_div(a, first): continue
                result = op3[1](second, d)
                if op3[0] == '/' and not valid_div(second, d): continue
                if abs(result - TARGET_SCORE) < 1e-6:
                    expr = f"({a} {op1[0]} ({b} {op2[0]} {c})) {op3[0]} {d}"
                    return True, expr
            except ZeroDivisionError:
                continue

            # a op1 ((b op2 c) op3 d)
            try:
                first = op2[1](b, c)
                if op2[0] == '/' and not valid_div(b, c): continue
                second = op3[1](first, d)
                if op3[0] == '/' and not valid_div(first, d): continue
                result = op1[1](a, second)
                if op1[0] == '/' and not valid_div(a, second): continue
                if abs(result - TARGET_SCORE) < 1e-6:
                    expr = f"{a} {op1[0]} (({b} {op2[0]} {c}) {op3[0]} {d})"
                    return True, expr
            except ZeroDivisionError:
                continue

            # a op1 (b op2 (c op3 d))
            try:
                first = op3[1](c, d)
                if op3[0] == '/' and not valid_div(c, d): continue
                second = op2[1](b, first)
                if op2[0] == '/' and not valid_div(b, first): continue
                result = op1[1](a, second)
                if op1[0] == '/' and not valid_div(a, second): continue
                if abs(result - TARGET_SCORE) < 1e-6:
                    expr = f"{a} {op1[0]} ({b} {op2[0]} ({c} {op3[0]} {d}))"
                    return True, expr
            except ZeroDivisionError:
                continue

            # (a op1 b) op2 (c op3 d)
            try:
                first = op1[1](a, b)
                if op1[0] == '/' and not valid_div(a, b): continue
                second = op3[1](c, d)
                if op3[0] == '/' and not valid_div(c, d): continue
                result = op2[1](first, second)
                if op2[0] == '/' and not valid_div(first, second): continue
                if abs(result - TARGET_SCORE) < 1e-6:
                    expr = f"({a} {op1[0]} {b}) {op2[0]} ({c} {op3[0]} {d})"
                    return True, expr
            except ZeroDivisionError:
                continue

    return False, "No solution found."

def calculate_24(nums):
    found, expr = try_all_expressions(nums)
    if found:
        print(f"Found a solution: {expr} = {TARGET_SCORE}")
        return True
    else:
        print(f"Cannot get {TARGET_SCORE} with these numbers {nums}.")
        return False

if __name__ == "__main__":
    # Example usage
    numbers = [2, 3, 4, 5]
    calculate_24(numbers)