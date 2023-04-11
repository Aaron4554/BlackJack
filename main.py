# Aaron Rodgers
# BlackJack
# 21-Mar-2023
import random


def main():
    # Create Vars
    player2 = 0
    bust = False
    play = True
    p_ace_as_11 = False
    d_ace_as_11 = False
    deck = create_deck()
    limit = 17
    while play:
        # set user hand size to 2 cards from the deck
        player1, p_ace_as_11 = p_starting_hand(deck, p_ace_as_11)
        # continue the game while neither party busts
        while not bust:

            choice = input(f'would you like a hit? your hand size is {player1} (y,n): ')
            if choice.upper() == 'Y':
                card = deal_cards(deck, 1)
                card, p_ace_as_11 = p_ace_check(player1, card, p_ace_as_11)
                player1 += card

            else:
                print(f'Your ending hand size is {player1}. lets see how the computer does')
                break

            if player1 > 21:
                if not p_ace_as_11:
                    print(f'Player 1 Bust. with a hand value of {player1}')
                    bust = True
                    break

                else:
                    print(f'your hand size is {player1}, but you previously choice to have an ace as 11, so it is now'
                          f' a 1 and your hand size is:')
                    p_ace_as_11 = False
                    player1 -= 10
                    print(player1)
        # dealer starts here
        while not bust:
            # check to see if the dealer is below the limit
            while player2 <= limit:
                card = deal_cards(deck, 1)
                card, d_ace_as_11 = ace_check(player2, card, d_ace_as_11)
                player2 += card

                if player2 > 21:
                    if not d_ace_as_11:
                        print(f'Player 2 Bust. with a hand value of {player2}\n'
                              f'Player 1 hand a hand value of {player1}')
                        bust = True
                        break

                    else:
                        d_ace_as_11 = False
                        player2 -= 10
                        print(f'Dealer bust! but they had an ace used as an 11, its now a 1 and their hand size is '
                              f'{player2}')

                if player2 >= limit:
                    winner(player1, player2)
                    break
            break
        choice = input(f'Do you want to play again? (y,n): ')
        if choice.upper() == 'N':
            play = False
            break
        else:
            play = True
            bust = False
            player1 = 0
            player2 = 0


# Create the deck
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


# Deal the cards out
def deal_cards(deck, number):
    hand_value = 0

    if number > len(deck):
        number = len(deck)

    for count in range(number):
        card = random.choice(list(deck))
        hand_value += deck[card]
        print(card)
    return hand_value


# check to see if a card delt to dealer is an ace, if it is, use it wisely
def ace_check(hand_value, card_value, d_ace_as_11):
    if card_value == 1:
        total_value = hand_value + 11
        if total_value <= 21:
            print('Ace returned as 11')
            d_ace_as_11 = True
            return 11, d_ace_as_11
        elif total_value > 21:
            print('Ace returned as 1')
            return 1, d_ace_as_11
    else:
        return card_value, d_ace_as_11


# check to see if a card delt to player is an ace, if it is, do with it what they will
def p_ace_check(hand, card, p_ace_as_11):
    if card == 1:
        choice = int(input(f'Would you like to use this ace as a 1 or 11? Your current hand size is {hand} (1,11): '))
        if choice == 1:
            return 1, p_ace_as_11
        elif choice == 11:
            p_ace_as_11 = True
            return 11, p_ace_as_11
    else:
        return card, p_ace_as_11


# deal the first two cards to the player
def p_starting_hand(deck, p_ace_as_11):
    hand = 0
    for x in range(0, 2):
        card = 0
        card += deal_cards(deck, 1)
        card, p_ace_as_11 = p_ace_check(hand, card, p_ace_as_11)
        if card is not None:
            hand += card
    return hand, p_ace_as_11


# find the winner
def winner(p1, p2):
    if p1 > p2:
        print(f'congrats, you won with a hand size of: {p1}\n'
              f'The dealer had a hand size of: {p2}')
    if p2 > p1:
        print(f'you lost to the dealer: {p2}, you had a hand size of: {p1}')
    if p1 == p2:
        print(f'it was a tie, Dealer wins!')


main()
