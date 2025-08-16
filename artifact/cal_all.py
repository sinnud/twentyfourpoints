import os, sys, itertools, ast

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(ROOT_PATH, 'src'))
from core_calculate import try_all_expressions

def solution():
    input_file = os.path.join(ROOT_PATH, "artifact", "all_list.txt")
    output_file = os.path.join(ROOT_PATH, "artifact", "solution.txt")
    noans_file = os.path.join(ROOT_PATH, "artifact", "no_answer.txt")
    with open(input_file, "r") as fin, open(output_file, "w") as fout, open(noans_file, "w") as fn:
        for line in fin:
            numbers = ast.literal_eval(line.strip())  # Convert string like [2, 3, 4, 5] to list
            result, expr = try_all_expressions(numbers)
            if result:
                fout.write(f"{numbers}: {expr}\n")
            else:
                fn.write(f"{numbers}\n")

def get_all_cards():
    suits = ['♠', '♥', '♦', '♣']
    ranks = list(range(1, 14))  # 1-10, J=11, Q=12, K=13
    deck = [(rank, suit) for rank in ranks for suit in suits]
    return deck

def cards_to_numbers(cards):
    return sorted([rank for rank, suit in cards])

def cal_all():
    deck = get_all_cards()
    all_combinations = itertools.combinations(deck, 4)
    output = set()
    for combo in all_combinations:
        numbers = cards_to_numbers(combo)
        output.add(tuple(numbers))
    output_file = os.path.join(ROOT_PATH, "artifact", "all_list.txt")
    with open(output_file, "w") as f:
        for numbers in sorted(list(output)):
            f.write(f"{numbers}\n")

if __name__ == "__main__":
    # cal_all()
    # print("All combinations of 4 cards have been written to artifact/all_list.txt")
    solution()
    print("Solutions for all combinations have been written to artifact/solution.txt")