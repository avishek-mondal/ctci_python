import random

def main():
    cards = [i for i in range(1, 53)]
    shuffle_cards(cards)
    print(cards)

def shuffle_cards(cards):
    n = len(cards)
    for i in range(n):
        k = random.randint(0, i)
        temp = cards[k]
        cards[k] = cards[i]
        cards[i] = temp