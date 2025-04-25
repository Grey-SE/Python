import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    return random.choice(cards)

def calculate_score(player_hand, computer_hand):
    player_score = sum(player_hand)
    computer_score = sum(computer_hand)

    if player_score == 21 and len(player_hand) == 2:
        return "Blackjack! You win! 🎉🍾🥂"
    elif computer_score == 21:
        return "Blackjack! You lose!"
    elif player_score > 21:
        return "You went over! You lose! 😭"
    elif computer_score > 21:
        return "Opponent went over. You win! 😁"
    else:
        if player_score > computer_score:
            return "You win! 😎"
        elif computer_score > player_score:
            return "You lose! 😤"
        else:
            return "It's a draw! 😮‍💨"

player_cards = []
computer_cards = []

is_running = True

while is_running:
    wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if wanna_play == 'y':
        print( "\n" * 20)
        print(art.logo)

        player_cards = [draw_card(), draw_card()]
        computer_cards = [draw_card()]

        wanna_add_card = 'y'

        while wanna_add_card == 'y':
            print(f'''
                    Your cards: {player_cards}, current score: {sum(player_cards)}
                    Computer's first card: {computer_cards[0]}
                    ''')

            wanna_add_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if wanna_add_card == 'y':
                player_cards.append(draw_card())
                if sum(player_cards) > 21:
                    break
            else:
                break

        if sum(player_cards) > 21:
            print(f'''
                    Your cards: {player_cards}, current score: {sum(player_cards)}
                    Computer's first card: {computer_cards[0]}
                    You final hand: {player_cards}, final score: {sum(player_cards)}
                    Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}
                    ''')
            continue

        while sum(computer_cards) <= 17:
            computer_cards.append(draw_card())

        print(f'''
                You final hand: {player_cards}, final score: {sum(player_cards)}
                Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}
                ''')

        print(calculate_score(player_cards, computer_cards))

    elif wanna_play == 'n':
        is_running = False
    else:
        print("Invalid input. Please type 'y' or 'n'.")

print("Thanks for playing!")





