# Aaron Rodgers
# BlackJack
# 21-Mar-2023
import random


def main():
    # Create Vars
    player2 = 0
    bust = False
    deck = create_deck()

    print('Thanks for playing!')
    player1 = p_starting_hand(deck)

    while not bust:
        choice = input(f'would you like a hit? your hand size is {player1} (y,n): ')
        if choice.upper() == 'Y':
            card = deal_cards(deck, 1)
            ace_check(player1, card)

            player1 += card
        else:
            print(f'Your ending hand size is {player1}. lets see how the computer does')
            break
        if player1 > 21:
            print(f'Player 1 Bust. with a hand value of {player1}\n'
                  f'Player 2 hand a hand value of {player2}')
            bust = True
            break
    # bust does not need to be set back to true, player lost.
    while not bust:
        card = deal_cards(deck, 1)
        ace_check(player2, card)

        player2 += card
        if player2 > 21:
            print(f'Player 2 Bust. with a hand value of {player2}\n'
                  f'Player 1 hand a hand value of {player1}')
            bust = True
            break


def create_deck():
    deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3, '4 of Spades': 4, '5 of Spades': 5,
            '6 of Spades': 6, '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9, '10 of Spades': 10,
            'Jack of Spades': 10, 'Queen of Spades': 10, 'King of Spades': 10,

            'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3, '4 of Hearts': 4, '5 of Hearts': 5,
            '6 of Hearts': 6, '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9, '10 of Hearts': 10,
            'Jack of Hearts': 10, 'Queen of Hearts': 10, 'King of Hearts': 10,

            'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3, '4 of Clubs': 4, '5 of Clubs': 5,
            '6 of Clubs': 6, '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9, '10 of Clubs': 10,
            'Jack of Clubs': 10, 'Queen of Clubs': 10, 'King of Clubs': 10,

            'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3, '4 of Diamonds': 4, '5 of Diamonds': 5,
            '6 of Diamonds': 6, '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9, '10 of Diamonds': 10,
            'Jack of Diamonds': 10, 'Queen of Diamonds': 10, 'King of Diamonds': 10,
            }
    return deck


def deal_cards(deck, number):
    hand_value = 0

    if number > len(deck):
        number = len(deck)

    for count in range(number):
        card = random.choice(list(deck))
        hand_value += deck[card]
        print(card)
    return hand_value


def ace_check(hand_value, card_value):
    if card_value == 1:
        total_value = hand_value + 11
        if total_value > 21:
            print('Ace returned as 11')
            return 11
        else:
            print('Ace returned as 1')
            return 1


def p_ace_check(hand, card):
    if card == 1:
        choice = int(input(f'Would you like to use this ace as a 1 or 11? Your current hand size is {hand} (1,11): '))
        if choice == 1:
            return 1
        elif choice == 11:
            return 11
    else:
        return card


def p_starting_hand(deck):
    hand = 0
    for x in range(0, 2):
        card = 0
        card += deal_cards(deck, 1)
        card = p_ace_check(hand, card)
        if card is not None:
            hand += card
    return hand


main()
