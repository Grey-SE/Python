import random
import game_data
import art
import os

def get_random_people():
    return game_data.data[random.randint(0, len(game_data.data) - 1)]

def is_a_has_more_followers(a, b):
    return a > b

def game():

    score = 0
    game_continue = True
    person_a = get_random_people()
    person_b = get_random_people()

    while game_continue:
        print("\n" * 20)
        print(art.logo)

        print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}")
        print(art.vs)
        print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}")

        while True:
            answer = input("Who has more followers? Type 'A' or 'B': ").lower()
            if answer in ['a', 'b']:
                break
            else:
                print("Please enter a valid choice: 'A' or 'B'.")

        a_followers = person_a['follower_count']
        b_followers = person_b['follower_count']
        correct_answer = 'a' if a_followers > b_followers else 'b'

        if answer == correct_answer:
            score += 1
            print(f"You're right! Current score: {score}.")
            person_a = person_b
            person_b = get_random_people()
            while person_a == person_b:
                person_b = get_random_people()
        else:
            print("\n" * 20)
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            break

game()
