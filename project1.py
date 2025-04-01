name = input("Hey type your name: ")
print("Hello " + name + " welcome to my game!")

should_we_play = input("Do you want to play? ").lower()

if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play!")

    direction = input("Do you want to go left or right? (left/right) ").lower()
    if direction == "left":
        print("You went left and fell of a cliff, game over, try again!")
    elif direction == "right":
        choice = input("Okay, you now see a bridge, do you want to swin under it or cross it? (swim/cross)")

        if choice == "swim":
            print("You got eaten by an alligator, you die, the end!!")
        else:
            print("You won! You found the gold!")
    else:
        print("Sorry, not a valid option")
else:
    print("We are not playing...")
