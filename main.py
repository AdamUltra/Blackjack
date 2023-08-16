import Art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print(Art.logo)
    Player_Card = [random.choice(cards), random.choice(cards)]
    Player_Score = sum(Player_Card)
    Computer_Card = [random.choice(cards), random.choice(cards)]
    Computer_Score = sum(Computer_Card)
    print(f"Your cards: {Player_Card}, current score: {Player_Score}")
    print(f"Computer's first card: [{Computer_Card[0]}]")


    def check(score):
        global UInp
        if score > 21:
            print(f"Your final hand: {Player_Card}, final score: {Player_Score}")
            print(f"Computer's final hand: {Computer_Card}, final score: {Computer_Score}")
            print("You lost 😤")

        elif score == 21:
            print(f"Your final hand: {Player_Card}, final score: {Player_Score}")
            print(f"Computer's final hand: {Computer_Card}, final score: {Computer_Score}")
            print("You won!!!")

        else:
            if UInp == 'y':
                draw_card()

            else:
                if Player_Score > Computer_Score:
                    print(f"Your final hand: {Player_Card}, final score: {Player_Score}")
                    print(f"Computer's final hand: {Computer_Card}, final score: {Computer_Score}")
                    print("You won!!!")

                elif Player_Score < Computer_Score:
                    if Computer_Score > 21:
                        print(f"Your final hand: {Player_Card}, final score: {Player_Score}")
                        print(f"Computer's final hand: {Computer_Card}, final score: {Computer_Score}")
                        print("You won!!!")
                    else:
                        print(f"Your final hand: {Player_Card}, final score: {Player_Score}")
                        print(f"Computer's final hand: {Computer_Card}, final score: {Computer_Score}")
                        print("You lost 😤")


                else:
                    print(f"Your final hand: {Player_Card}, final score: {Player_Score}")
                    print(f"Computer's final hand: {Computer_Card}, final score: {Computer_Score}")
                    print("It's a draw")


    def draw_card():
        global Player_Score, UInp, Computer_Score
        UInp = input("Type 'y' to get another card, type 'n' to pass")
        if UInp == 'y':
            Player_Card.append(random.choice(cards))
            Player_Score = sum(Player_Card)
            print(f"Your cards: {Player_Card}, current score: {Player_Score}")
            print(f"Computer's first card: [{Computer_Card[0]}]")
            check(Player_Score)

        else:
            while Computer_Score <= 16:
                Computer_Card.append(random.choice(cards))
                Computer_Score = sum(Computer_Card)
            check(Player_Score)


    draw_card()
