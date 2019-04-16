######################################################################
# Author: Emily Lovell & Scott Heggen       TODO: Change this to your names
# Username: lovelle & heggens               TODO: Change this to your usernames
#
# Assignment: T01: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
######################################################################
from time import sleep

delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False         # You start out not dead, which is good.

# Asks the user to input their name.
username = input("What do they call you, unworthy adversary? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome, " + username + ", to the labyrinth.")
sleep(delay)
print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print()
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

direction = input("Which direction would you like to go? [North/South/East/West] " )

if direction == "North":
    # Good choice!
    print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
    sleep(delay)
elif direction == "South":
    # Oh... Bad choice
    print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
    sleep(delay)
    print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
    print("Running seems like a good idea now. But... it's really, really dark.")
    print("You turn and run like the wind. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
    print("He eats you. You are delicious.")
    dead = True
else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Better luck next time!. ")
    quit()

#########################################################################################################
# TODO Add your part of the story here. Keep in mind you may NOT be coming right after the example above.



# TODO Don't forget to check if your user is dead at the end of your chapter!


#########################################################################################################

# The following is the end of the story. Don't change this section, unless you really want to
# (though it may not be used in the final story. Or will it...)
print("Look at that! You made it to the end of the story without dying! ")
print("Congratulations... now go play again and find an interesting way to perish. ")

if dead == False:
        print("After hours of wandering in the cave you met Indiana Jones")
        sleep(delay)
        print("He wants to help to search for a treasure")
        Decision = input("Do you want to join him? {Join, Stay, Leave} ")

        if Decision == "Join":
            print("Great, you found a treasure with Indiana Jones.")
            sleep(delay*3)
            print()
            print("However, he really does not like to share.")
            sleep(delay*3)
            print()
            print("When you turned around, he pulled out a gun and shoot you to your head.")
            dead = True
            #bad option
        elif Decision == "Stay":
            print("Indiana Jones went the wrong direction and fell for a trap")
            sleep(delay*3)
            print()
            print("You can hear boulder movements followed by bone cracking and human scream")
            sleep(delay*3)
            print()
            print("Indian Jones died as a hero")
            #good option
        else:
            #neutral choice
            print("You left the place and you keep going deeper into the cave.")
            sleep(delay*3)
            print("You do not know what happened with Indiana Jones")
            sleep(delay*3)
            print("The story continues")

        if dead == True:
            sleep(delay*3)
            print("Oh no! You died. Better luck next time!. ")
            quit()

        sleep(delay*3)
        print("Look at that! You made it to the end of the story without dying! ")
        print("Congratulations... now go play again and find an interesting way to perish. ")

