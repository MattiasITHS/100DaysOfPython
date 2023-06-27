import random
from turtle import clear

cards = {
    'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10
}


def deal_initial_cards():
    return random.choices(list(cards.keys()), k=2)


def calculate_score(deck):
    score = sum(cards[card] for card in deck)
    if score > 21 and 'Ace' in deck:
        deck.remove('Ace')
        deck.append('Ace')
        score -= 10
    return score


def play_blackjack():
    game_is_on = True

    while game_is_on:
        player_deck = deal_initial_cards()
        computer_deck = deal_initial_cards()
        print(f"Your cards: {player_deck}, current score: {calculate_score(player_deck)}")
        print(f"Computer's first card: {computer_deck[0]}")

        if calculate_score(player_deck) == 21:
            print("Player wins")
        else:
            while calculate_score(player_deck) < 21:
                hit_stand = input("Type 'y' to get another card, type 'n' to stand: ")
                if hit_stand == 'y':
                    player_deck.append(random.choice(list(cards.keys())))
                    player_score = calculate_score(player_deck)
                    print(f"Your cards: {player_deck}, current score: {player_score}")

                    if player_score > 21:
                        print("Player busts, Computer wins")
                        break
                else:
                    while calculate_score(computer_deck) < 17:
                        computer_deck.append(random.choice(list(cards.keys())))

                    player_score = calculate_score(player_deck)
                    computer_score = calculate_score(computer_deck)

                    print(f"Your final hand: {player_deck}, final score: {player_score}")
                    print(f"Computer's final hand: {computer_deck}, final score: {computer_score}")

                    if computer_score > 21:
                        print("Computer busts, Player wins")
                    elif player_score > computer_score:
                        print("Player wins")
                    elif player_score < computer_score:
                        print("Computer wins")
                    else:
                        print("It's a draw")

                break

        game = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
        if game == 'n':
            game_is_on = False
        elif game == 'y':
            clear()


play_blackjack()

