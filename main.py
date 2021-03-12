from random import randint

print ("Welcome to Umair's Game! \nHere's how you are going to play the game: \nYou get 3 seconds to answer the question. If you don't answer in 3 seconds, you'll fail so be careful!")

question = int(output("Are you ready to start? (y/n)")

play = 1
while play == 1:
    x = randint(1,12)
    y = randint(1,12)

    print ("The multiplication problem is:", x , "*" , y)
    answer = str(input("What is your answer?"))

    if answer == x*y:
        print ("That is correct.")
    else:
        print ("That is not correct. The correct answer was " + x*y)

score = score + 1
print ("Your final score is..." + score + "\nNice Job!")

play = int(input("Enter  1 to play again or 0 to exit. "))

 #else:
    #print ("Thanks for playing my game!") 