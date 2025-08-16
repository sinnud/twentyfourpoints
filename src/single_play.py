import re
import ast
import operator
from src.get_cards import get_four_cards, display_cards
from src.cards2numbers import cards_to_numbers
from src.core_calculate import try_all_expressions

def safe_eval(expression, allowed_numbers):
    """Safely evaluate a mathematical expression using only allowed numbers and operations."""
    try:
        tree = ast.parse(expression, mode='eval')
    except SyntaxError:
        return None
    
    def eval_node(node):
        if isinstance(node, ast.Expression):
            return eval_node(node.body)
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            elif isinstance(node.op, ast.Sub):
                return left - right
            elif isinstance(node.op, ast.Mult):
                return left * right
            elif isinstance(node.op, ast.Div):
                if right == 0:
                    raise ZeroDivisionError
                return left / right
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -eval_node(node.operand)
        else:
            raise ValueError("Unsupported operation")
    
    return eval_node(tree.body)

def single_play():
    TARGET_SCORE = 24
    print("=" * 50)
    print("Welcome to Twenty Four Points! Single player mode.")
    solution = None
    while not solution:
        cards = get_four_cards()
        numbers = cards_to_numbers(cards)
        found, solution = try_all_expressions(numbers)
        if not found:
            print(f"No solution for these cards {numbers}. Let me get another one...")
            solution = None
            continue

    print("Your cards are:")
    display_cards(cards)
    print(f"Find a way to use all four numbers to get {TARGET_SCORE}.")
    print("Enter your answer (e.g., (8-3)*(8-3))...")
    answer = input("Your answer: ").strip()
    
    try:
        # Only allow numbers from the drawn cards
        used_numbers = [int(num) for num in re.findall(r'\d+', answer)]
        if sorted(used_numbers) != sorted(numbers):
            print("You must use each card number exactly once.")
            print(f"You lose. Invalid numbers used.")
            print(f"A possible solution is: {solution}")
            print("=" * 50)
            return answer
        
        result = safe_eval(answer, numbers)
        if result is None:
            print(f"Invalid expression: {answer}")
            print("You lose.")
            print(f"A possible solution is: {solution}")
        elif abs(result - TARGET_SCORE) < 1e-6:
            print(f"You win! `{answer}` = {result}.")
            print(f"A possible solution is: {solution}")
        else:
            print(f"Incorrect answer: {answer} = {result}, not {TARGET_SCORE}.")
            print("You lose.")
            print(f"A possible solution is: {solution}")
    except Exception as e:
        print(f"Invalid input {answer}.")
        print("You lose.")
        print(f"A possible solution is: {solution}")
    print("=" * 50)
    return answer

if __name__ == "__main__":
    single_play()