import re
from src.get_cards import get_four_cards, display_cards
from src.cards2numbers import cards_to_numbers
from src.core_calculate import try_all_expressions

def single_play():
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
    print("Find a way to use all four numbers to get 24.")
    print("Enter your answer (e.g., (8-3)*(8-3))...")
    answer = input("Your answer: ").strip()
    # Judge answer
    try:
        # Only allow numbers from the drawn cards
        used_numbers = [int(num) for num in re.findall(r'\d+', answer)]
        if sorted(used_numbers) != sorted(numbers):
            print("You must use each card number exactly once.")
            print(f"You lose. `{answer}` <> {result}.")
            print(f"A possible solution is: {solution}")
            print("=" * 50)
            return answer
        result = eval(answer)
        if abs(result - 24) < 1e-6:
            print(f"You win! `{answer}` = {result}.")
            print(f"A possible solution is: {solution}")
        else:
            print(f"Incorrect answer `{answer}` <> {result}.")
            print("You lose.")
            print(f"A possible solution is: {solution}")
    except Exception:
        print(f"Invalid input {answer}.")
        print("You lose.")
        print(f"A possible solution is: {solution}")
    print("=" * 50)
    return answer

if __name__ == "__main__":
    single_play()