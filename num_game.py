import random


def game():
    # generate random # b/t 1 and 10
    secret_num = random.randint(1,10)
    guesses = 0
    print(secret_num)
    
    while guesses < 5:
        try:
            # get # guess from player
            guess = int(input("guess a # between 1-10: "))
        except ValueError:
            print("that's not a #")
            guesses += 1
        else:
            
            # compare guess to secret #
            if guess == secret_num:
                print("you got it. secret # was {}".format(secret_num))
                break
            elif guess < secret_num:
                print("too low")
            else:
                print("too high")
            guesses += 1
    else:
        print("you fail. secret # was {}".format(secret_num))
    play_again = input("want 2 play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("bye")

game()