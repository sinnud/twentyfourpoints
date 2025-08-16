import random

def get_four_cards():
    """Randomly select 4 cards from a standard deck (no jokers)."""
    suits = ['♠', '♥', '♦', '♣']
    ranks = list(range(1, 14))  # 1-10, J=11, Q=12, K=13
    deck = [(rank, suit) for rank in ranks for suit in suits]
    selected = random.sample(deck, 4)
    return selected

def display_cards(cards):
    """Display the selected cards in a readable format."""
    rank_map = {11: 'J', 12: 'Q', 13: 'K'}
    for rank, suit in cards:
        rank_str = rank_map.get(rank, str(rank))
        print(f"{rank_str}{suit}", end=' ')
    print()

if __name__ == "__main__":
    cards = get_four_cards()
    print("Your cards are:")
    display_cards(cards)
