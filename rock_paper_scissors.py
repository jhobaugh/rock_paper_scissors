# import random and create a tuple of rock paper and scissors to randomize from
import random
rps = ("rock", "paper", "scissors")

# create a boolean for the retry loop
retry = True

# use a while loop to ask if the player wants to play again and an integer variable for who is winning
while retry:
    c_winner = 0
    p_winner = 0
    bool_winner = True
    print("The game is rock paper scissors! Lets begin!")
    # use a while loop with the parameters of who won the game on a count of three
    # use the random function to determine the random variable that the computer chooses
    # create the input string
    # print current score and what the computer chose
    while bool_winner:
        computer = random.choice(rps)
        print("The current score is player: ", p_winner, " Computer: ", c_winner)
        player = input(str("Choose rock paper or scissors: "))
        print("Computer chose " + computer)


        # use an if/else statements with parameters to decide when to deduct or add a point to the winning score
        if computer == "rock":
            if player == "paper":
                print("1 point to the player!")
                p_winner += 1

            elif player == "rock":
                print("Its a draw, try again!")

            elif player == "scissors":
                print("1 point to the computer!")
                c_winner += 1

            else:
                print("invalid response try again!")

        elif computer == "paper":
            if player == "scissors":
                print("1 point to the player!")
                p_winner += 1

            elif player == "paper":
                print("Its a draw, try again!")

            elif player == "rock":
                print("1 point to the computer!")
                c_winner += 1

            else:
                print("invalid response try again!")
        else:
            if player == "rock":
                print("1 point to the player!")
                p_winner += 1

            elif player == "scissors":
                print("Its a draw, try again!")

            elif player == "paper":
                print("1 point to the computer!")
                c_winner += 1

            else:
                print("invalid response try again!")
                # break loop statement
        if c_winner == 3 or p_winner == 3:
            bool_winner = False

    # when the loop is broken determine who won and announce that
    if c_winner != 3:
        print("Congratulations! You win!")
        keep_going = input(str("Would you like to try again? (y/n): "))
        if keep_going != "y":
            print("Thanks for playing!")
            break
    else:
        print("Sorry! You lose!")
        keep_going = input(str("Would you like to try again? (y/n): "))
        if keep_going != "y":
            print("Thanks for playing!")
            break
    # ask if the player wants to play again


