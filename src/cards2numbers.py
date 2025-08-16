def cards_to_numbers(cards):
    """
    Given a list of cards [(rank, suit), ...], extract and return a sorted list of their numbers.
    J=11, Q=12, K=13 are already represented as numbers.
    """
    numbers = [rank for rank, suit in cards]
    return sorted(numbers)

if __name__ == "__main__":
    # Example usage
    example_cards = [(11, '♠'), (4, '♦'), (13, '♥'), (2, '♣')]
    print("Cards:", example_cards)
    print("Numbers:", cards_to_numbers(example_cards))