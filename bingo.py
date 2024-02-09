import random

def generate_values(starting_val):
    """
    Generate a list of five unique random values within a specific range.
    """
    values = set()
    while len(values) < 5:
        values.add(random.randint(starting_val, starting_val + 14))
    return list(values)

def generate_card():
    """
    Generate a bingo card represented as a dictionary.
    """
    columns = ['B', 'I', 'N', 'G', 'O']
    start_values = [1, 16, 31, 46, 61]
    bingo_card = {column: generate_values(start) for column, start in zip(columns, start_values)}
    bingo_card['N'][2] = "FREE"
    return bingo_card

def generate_cards(num):
    """
    Generate multiple bingo cards represented as a dictionary of dictionaries.
    """
    if not isinstance(num, int):
        raise TypeError("Number of cards must be an integer")
    if num < 1:
        raise ValueError("Number of cards must be at least 1")
    
    cards = {}
    unique_cards = set()

    while len(cards) < num:
        card = generate_card()
        card_str = str(card)
        if card_str not in unique_cards:
            unique_cards.add(card_str)
            cards["FOSL" + str(len(cards))] = card

    return cards


print(generate_cards(20))