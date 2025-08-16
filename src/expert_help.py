from src.core_calculate import try_all_expressions, TARGET_SCORE

def expert_help():
    print("-" * 30 + " Expert Help " + "-" * 30)
    print("Expert Help: Enter 4 numbers separated by spaces (e.g., 1 3 4 6):")
    user_input = input("Numbers: ").strip()
    try:
        numbers = [int(x) for x in user_input.split()]
        if len(numbers) != 4:
            print("Please enter exactly 4 numbers.")
            print("-" * 30 + " ### END ### " + "-" * 30)
            return user_input
    except ValueError:
        print("Invalid input. Please enter integers only.")
        print("-" * 30 + " ### END ### " + "-" * 30)
        return user_input

    found, solution = try_all_expressions(numbers)
    if found:
        print(f"Solution: {solution} = {TARGET_SCORE}")
    else:
        print("I can not solve it.")
    print("-" * 30 + " ### END ### " + "-" * 30)
    return 'help' # keep in expert_help status

if __name__ == "__main__":
    expert_help()