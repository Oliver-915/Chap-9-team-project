#chapter 9 exercisess
import random

def unique_words(file):
    #unique_words accepts file as arguments
    infile = open(file, 'r')

    words = set()

    for line in infile:
        parts = line.split()
        for w in parts:
            words.add(w.lower())

    infile.close()

    for w in words:
        print(w)



def winners_program():
    #winners_program accepts no arguments
    infile = open('WorldSeriesWinners.txt', 'r')

    winners = infile.readlines()
    infile.close()

    year_dict = {}
    win_count = {}

    year = 1903

    for team in winners:
        team = team.strip()

        if team == "World Series Not Played in 1904":
            year_dict[1904] = "No Game"
            year = 1905
            continue

        if team == "World Series Not Played in 1994":
            year_dict[1994] = "No Game"
            year = 1995
            continue

        year_dict[year] = team

        if team in win_count:
            win_count[team] += 1
        else:
            win_count[team] = 1

        year += 1

    user_year = int(input("Enter a year (1903-2008): "))

    if year_dict[user_year] == "No Game":
        print("World Series not played that year.")
    else:
        team = year_dict[user_year]
        print(f"{team} won in {user_year}. {team} have won {win_count[team]} times.")



def create_deck():
    #create_deck accepts no arguments
    deck = []

    for i in range(4):
        for val in range(2,11):
            deck.append(val)
        for face in range(3):
            deck.append(10)
        deck.append(11)

    return deck


def deal_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

def play_game():
    deck = create_deck()

    p1 = 0
    p2 = 0

    while len(deck) > 0:
        p1 += deal_card(deck)
        p2 += deal_card(deck)

        if p1 > 21 and p2 > 21:
            print("Draw")
            return
        elif p1 > 21:
            print("Player 2 wins")
            return
        elif p2 > 21:
            print("Player 1 wins")
            return

    print("Deck finished")

def main():
    print("1. Unique Words")
    print("2. World Series Winners")
    print("3. Blackjack")

    choice = input("Enter choice: ")

    if choice == "1":
        unique_words("text.txt")
    elif choice == "2":
        winners_program()
    elif choice == "3":
        play_game()


main()