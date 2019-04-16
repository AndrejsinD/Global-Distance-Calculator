######################################################################
# Author: The Spring 2019 226 Class!
#
# Assignment: T01: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements
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
# Audrey, Lesley, and Anya
# Refactored by Team 1

print("You found yourself inside the mouth of the Mammoth Cave. It's dark outside but you see the light inside the cave." )

direction = input("You have a choice to make [stay outside or follow the light]")

if direction =="stay outside":
    #Good choice!
    print("Great decision! You have a hammock and some food. You will survive until morning")

    sleep(delay)

elif direction == "follow the light":
    #Bad choice
    print("Hungry hungry hyenas live in this cave and you have just disturbed their sleep.")
    sleep(delay)
    print("The rangers dropped their flashlight the last time they toured the cave.")
    print("The hyenas are closing in behind you. The exit is blocked...")
    print("You have been eaten alive. Good job!")
    dead=True

else:
    #Neutral choice
    print("You got scared of your own shadow.You passed out for several hours.")
    print("After you wake up, you decide to go deeper into the cave. The adventure continues.")

if dead==True:
    print("Oh, no! It was not your luck today! You died.")
    quit()


#########################################################################################################
# Darian and Alex
# Refactored by Team 2

print("You are in a dark cave. You decide to move further into the cave, and you notice a fork into three paths.")
sleep(delay)
path = input("Which path will you take? [Left/Center/Right]")

if path == "Left":
    # Neutral
    print("As you follow the path you find and pick up a stick, and you find a waterfall, and you continue onward.")
    sleep(delay)

elif path == "Center":
    # Bad Choice
    choice = input("Choose a number between 1 and 10.")
    if choice == "8":
            print("You have bested me in the game of numbers, mortal.")
            print("You find a waterfall up ahead, and continue onward.")
    else:
        print("You have chosen incorrectly, foolish mortal.")
        print("You find yourself cornered as 50 goblins jump and attack. You die!")
        dead = True
    sleep(delay)






elif path == "Right":
    # Reward
    print("You find the sword of the Goblin King on the path and come to a waterfall, and you continue onward.")
    sleep(delay)

if dead == True:
    print("Damn those goblins! Choose a different path and try again!")
    quit()


#########################################################################################################
# Evan, Hila, and Megan
# Refactored by Team 3

print("You hear a large explosion from behind and your head hits the ground WHACK")
sleep(delay)
print("...")
sleep(delay)
print("...")
sleep(delay)
print("Your eyes blur and you wake up in a cold, dark cellar. You see a collection of metal bars in front of you.")
print("You realize you are in a jail cell.")
if not dead:
    choice1=input("What would you like to do? [look/escape]")
if choice1.find("look") is not -1 and not dead:
    print("You see your bed, a small nightstand with a rubber duck sitting on top, and a small hole in the corner.")
elif choice1.find("escape") is not -1 and not dead:
    print("You flail your arms through the prison cell bars screaming for attention.")
    sleep(delay)
    print("A guard dressed in full chain mail blazoned by the kings crest approaches you.")
    print("What is all this raquet for?! Silence!")
    print("He hits you over the head with his mace killing you instantly.")
    dead = True

else:
    print("you waste away in prison and die of boredom")
    dead = True
if not dead:
    choice2 = input("What will you do now? [squeak rubber ducky/pick up bedsheets]")
if not dead:
    if choice2.find("squeak") is not -1 and not dead:
        print("The sharp squeak of the small toy duck rings through the empty hall.")
        sleep(delay)
        print("...")
        sleep(delay)
        print("A guard dressed in full chain mail blazoned by the kings crest approaches you.")
        choiced = input("What will you do? [bargain/attack]")
        if choiced.find("bargain") is not -1 and not dead:
            print("You give the guard your best sales pitch: 'Will you let me out for this rubber ducky?'")
            print("The guard looks at you confused but agrees. The doors open up and you are free from the prison.")

        elif choiced.find("attack") is not -1 and not dead:
            print("you throw the small yellow duck at the guard")
            sleep(delay)
            sleep(delay)
            print("The guard is furious with you and swings his mace and kills you.")
            dead=True

        else:
            print("you waste away in prison and die of boredom")
            dead = True

    elif choice2.find("bedsheets") is not -1 and not dead:
        print("You take the bedsheets.")
        sleep(delay)
        print("A guard dressed in full chain mail blazoned by the kings crest approaches you.")
        choiceb=input("'What are you doing with those bed sheets?' What will you do? [bargain/attack]")
        if choiceb.find("bargain") is not -1 and not dead:
            print("You give the guard your best sales pitch: 'Will you let me out for these bed sheets?'")
            sleep(delay)
            print("The guard looks at you confused, 'how dare you address sir reginold the third in this way!.")
            sleep(delay)
            print("The guard is furious with you and swings his mace and kills you.")
            dead = True

        elif choiceb.find("attack") is not -1 and not dead:
            print("you lasso the bedsheets around the guardsman's neck and strangle him to death")
            sleep(delay)
            print("The guard falls limp you take the cell key and you are free")

    else:
        print("you waste away in prison and die of boredom")
        dead = True

else:
    if not dead:
        print("you waste away in prison and die of boredom")
        dead = True
        quit()

if dead:
    print("you were unable to escape ye old prison rest in peace")
    quit()
if not dead:
    print("congratulations you have escaped prison")
    quit()


#########################################################################################################
# Irfan and David
# Refactored by Team 4

username = input("Who do you think you are?")
print()
print("Welcome, " + username + ", but the place is not very welcoming")
sleep(delay)

print("How are you? Dizzy? Hungry? Tired? Thirsty?")
print("Look around, what do you see?")
sleep(delay)

print("Oops! I forgot to tell you that you are in a dark cave.")
print("To see, you need light. Get out of this place!")

sleep(delay)

print("You can choose which way to go")
print("Only one direction will lead you towards light, & obviously towards food & water.")

print("You should choose wisely, Right, Left, Front, or Back")

sleep(delay)

direction = input

print("So you think it is a wise decision?")

if direction == "Right":
    print("You successfully came out of the cave. Food and water is waiting for you!")
elif direction == "Back":
    print("You went even deeper inside the cave")
    print("Did you hear that? A hissssssss!")
    print("That is a rattle snake, and it looks agitated")
    print("What? You tried to run?! You agitated the other snakes as well!")
    print("The cave is full of them!")
    print("Goodbye! You acted like the dumbest stupid")
    dead = True


if direction == "Front":
    print("That is not a way out. It is just the cave wall.")
if direction == "Left":
    print("Why do you keep hitting the cave wall again and again?")
if dead == True:
    print("Better luck next time!")

    quit()


#########################################################################################################
# Jalen and Tabias
# Refactored by Team 5

print()
print("Welcome, " + username + ", to space.")
sleep(delay)
print("In front of you are 3 doors. All three doors lead you to different destinations. ")
print("Be careful one of the doors leave you stuck in a black hole")
print()
sleep(delay * 2)
print("You are trapped in your space ship and you are running out of air.")
print("Don't panic, take time to think, Good luck.")
print()
sleep(delay)
direction = input(" Which door do you choose? Door 1/Door 2/Door 3] ")

if direction == "Door 1":
    # Good choice!
    print("You have found an extra hour supply of air, you're not finished yet, but at least you're not dead...")
    sleep
if direction == "Door 2":
    # That's it...!
    print("You open the door, you find yourself in front of the space pod to take you back home.")
    print("As soon as you open the space pod, you start shaking from excitement ")
if direction == "Door 3":
    # uh-oh...bad choice
    print("you open the door, you see nothing, black emptiness. Youre sucked into this cold black hole, you freeze.")
    print("Oh no! You died. Better luck next time!. ")
    dead = True
if dead == True:
    print("oh no! better luck next time!")
    quit ()


#########################################################################################################
# Karmadri and Lisandro
# Refactored by Team 6

direction = input("Which direction would you like to go? {North, South, East, West}" )

if direction == "South":
    # right choice.
    print("You locate a stream of water on the floor. Following it could lead you to the exit.")
    sleep(delay)
elif direction == "East":
    #Wrong choice
    print("In the darkness, you fail to see a sinkhole that you fall into, never to escape.")
    # print('')
    # num = input("Before falling to your doom, you reach out into the darkness and attempt to grab onto the edge."
    #                  " How far do you extend your arm? (1-90)")
    # if num < 45:
    #     print('You did not reach out far enough, therefore you fell to your death.')
    dead = True
else:
    # neutral choice
    print("You continue your travel but you're as equally confused as you were moments ago.")
    sleep(delay)

if dead == True:
    print ("You are banished to the sinkhole for the rest of your days. Better luck next time!")
    quit()


#########################################################################################################
# Kenzie and Caleb
# Refactored by Team 7

print("You're walking through a jungle, looking for treasure when suddenly, something hard hits your head"
      + "and you fall to the ground.\n")
sleep(delay*5)
print("When you wake up, you hear dark chanting coming from within the depths of the jungle.")
sleep(delay*2)
print(" OO AHH AHH AHH, OO AHH AHH AHH")
sleep(delay*2)
print("Looking around, you see a tribe of indians surrounding you and a giant fire in the middle of the circle. "
      + "The leader walks up to you and asks what your purpose is")

answer = input("What do you tell him? {Truth/Lie} ")
if answer == "Truth":
    #Bad choice
    print("'I was sent to look for treasure.'")
    sleep(delay*2)
    print("The tribe of indians get angry and decide they must get rid of you!")
    print("They pick you up and start heading toward the fire...\n")
    dead = True

else:
    #We lie!
    print("' I am lost. I am just trying to find my way out of the jungle.'")
    print("The leader looks at you and tells you he will leave you overnight and decide what to do with you" +
          " when tomorrow comes.")
    sleep(delay*5)

if dead == True:
    print("Oh!! What a horrible way to die. Better luck next time!")
    quit()


print("Little does the leader know...")
print("You have had a knife in your pocket the whole time")
print("While the indians are done with you for the night, you cut yourself free, but hold the ropes" +
      " so you do not look suspicious.\n")
sleep(delay*3)

print("You are thinking of ways to escape. You come up with three options: ")
print("You can wait until the leader gets close and attack him and fight your way to freedom.")
print("You can wait until everyone is asleep and then quietly make your escape.")
print("You can tell the leader that you want to be a part of the tribe and try to figure out your escape from there.\n")
sleep(delay)

option = input("Which option do you choose? [Attack/Wait/Join] ")
sleep(delay)

if option == "Attack":
    #Bad choice
    print("You wait until the tribe leader walks in front of you and then...")
    sleep(delay)
    print("You take your knife and stab him, killing him")
    print("You try to run, but the rest of the tribe gets to you first and kill you for killing their leader.\n")
    dead = True

elif option == "Wait":
    #good choice
    print("So you sit there...waiting until everyone goes to sleep.")
    print("Once you see the last person has finally fallen asleep, you decide to make your move.")
    print("You quietly slip out of the ropes and creep away from the tribe")
    sleep(delay*3)
    print("You have been walking through the jungle for hours when suddenly you run into someone...another adventurer!")
    sleep(delay)

else:
    #Neural choice
    print("You call the leader of the tribe over to you.")
    print("'I do not have anywhere to go. I was wondering if I could possibly join your tribe")
    print("The leader says a decision will be made later that night during the Ceremony...\n")
    #later that night
    print("The Ceremony has begun and the whole tribe is doing their chant...\n")
    sleep(delay * 3)
    print("OO AHH AHH AHH, OO AHH AHH AHH")
    sleep(delay)
    print("The leader yells 'SILENCE!!!!' " + username + "'wants to join our tribe.'")
    print("'I have decided that we shall give " + username + " a chance'")
    print("'We shall teach " + username + " our ways'\n")
    sleep(delay*5)
    print("You are set free, but now you have to be a part of the tribe")

if dead == True:
    print("Oh!! What a horrible way to die. Better luck next time! ")
    quit()

#########################################################################################################
# Liberty and Joseph
# Refactored by Team 8

#A Haunted house with four doors and each doors leads to different destination
print()
print("You are trapped in a haunted house with four doors")
print("Some doors will lead you out to go home and others let you to the voracious\n and unmerciful Creatures ")
print("Each door lead to different destination, and you have to avoid the evil door in order to stay alive")
print()

direction = input ("which door will you like pass through? [door1/door2/door3/door4]")

if direction == "door1":
    #Door1 Oh Nooo.. you just made a bad choice!
    print("You just open the evil door .")
    sleep(delay)
    print("This door lead to a room filled up with thousands of zombies.")
    print("It is difficult to survive among these zombies")
    print("you have no choice than to be eaten up by the zombies")
    print("Your blood taste like an orange juice, and your flesh taste like a barbaque chicken to the zombies")
    #Door2 Comprises of good and bad choices
elif direction == "door2":
    print("Wow!!! You have  made a wonderful choice but you have to enter a code  \n on the door")
    print("there are two codes in front of the door, one among the two codes exit you from the haunted house")
    print("the other code open the door for a hungry Snakes into the room")
    choice = input (' Enter code 1 or 2 on the door locker')
    x = int(choice)
    if x== 1:
        print("You are Lucky!!! Go out and never come back to this area again")
        print("Congratulation, you survive the haunted house alive")
    elif x==2:
        print("ALERT!! WRONG DOOR!!")
        print("You just open the door for two massive python snakes")
        sleep(delay)
        print("Say your last words before you find yourselves in our stomachs")
        print("You are now Dead")
  #Even or odd number decision keep you alive or dead
elif direction== "door4":
    print("This is the worst door. but there are still options to make towards your survival")
    print("However in this section you will need to pick a number, "
          '''the right number will extend your chance of living ''')
    option= input("enter any number you like")
    x= int(option)
    y = x % 2
    z = int(y)
    if z==0:
        print ("You entered an even number which closes the gate, and prevent the deadly animals from entering.")
        print("However you are still in the room but safer than if you had proceeded with that way.")
    elif z== 1:
        print("You entered an odd number")
        print("The dragon will now feed on you")
        print(" You are Dead without any further travel!!! ")
#The best option to make
elif direction == "door3":
    print(" You are now safe")
    print("this door automatically get you out of the haunted house")
    print("Look at that! You made it safe without being killed! ")
    print("Congratulations... now go play again and explore every other door in the haunted house.")


#########################################################################################################
# Mahmoud and Shageldi
# Refactored by Team 9

print("\n    Once upon a time, while completing a cross country hike, you became so thirsty. Somewhere in the woods, you see a bar and decide to visit. The bar is completely empty, meaning there was no alive soul. You take a menu and it lists three types of drinks: Tea, Beer, Soda. One of the drinks is poisonous.")
choice = input("Choose what you want to drink: ").lower()
corpse = False
if choice == "tea":
    # this is a good choice
    print("\nGreat Choice!!! You get one more drink on the house with no poison in it")
    sleep(3)

elif choice == "beer":
    # this is a bad choice, which would kill the player
    print("\nCongratulations!  You have 5 more minutes to write a letter to your family for the last time.")
    sleep(3)
    corpse = True
else:
    # this is a neutral choice
    print("\nNot that bad! It is time to leave the bar. Safe trips.")
    sleep(3)
    print("\nDemon laughing: Hahaha  hahaha hahaha")

if corpse == True:
    print("\nThis is the end of your life journey.")
    quit()

#########################################################################################################
# Nicole and Eleni
# Refactored by Team 10

username = input("What is your name? How do you prefer to be called? ")

print()
print("Welcome, " + username + ",to Las Vegas.")
sleep(delay)
print("We are at Omnia, a club in Las Vegas. A tall, blond, man comes in holding an AK47 gun in his right hand.")
sleep(delay * 2)
print("Everyone is panicked, your friend Erica freaks out and decides to hide under the table.")
sleep(delay * 2)
print("You are standing on the other side of the room. The door is located really close to you.")
print()
sleep(delay * 2)
print("You have 3 options")
sleep(delay * 2)
print("Run Away, Hide with your friend, or Fight for your life")
print()
sleep(delay)

Choice = input("What did you decide to do? [Run/Hide/Fight]")

if Choice == "Run":
    #Safe Choice
    print('You are safe!')  #Safe option
    sleep(delay * 2)
elif Choice == "Hide":
    #Correct options
    print("The story continues. You survived!")
    sleep(delay * 2)
elif Choice == "Fight":
    #Wrong Choice
    print("You are dead! Sorry :( ")
    sleep(delay * 2)
    dead = True
else:
    print("You were not able to do that.")


#########################################################################################################
# Roberto and David
# Refactored by Team 11

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


#########################################################################################################
# Sandesh
# Refactored by Team 12

print("The further you go the colder the cave seems to get.")
print("In the distance you can hear a muted *splat* *splat* sound of water droplets hitting the cave floor.")
print("A chill runs down your back, as you realize that the cave is becoming darker and darker the further you go in.")
print("...\n")
sleep(delay)
sleep(delay)
sleep(delay)
print("The cave seems to be more menacing now and your senses are on high alert.")
print("A rivulet of sweat trickles down your back despite the chill of the cave.")
print("Your ears are filled with the sound of your ever increasing heart beat ")
print("and the tentative slap of your feet against the cave floor as you slowly make your way forward.")
print("...\n")
sleep(delay)
sleep(delay)
sleep(delay)
print("Your slow march comes to a sudden end as you spot a figure of shadow in front of you.")
print("The figure, no the monster seems to be coming closer. You can either run away, charge the monster, or hide")

choice2 = input("What do you decide to do? (run, charge, hide)")

if choice2 == "run":
    print("You turn in the other direction and run as fast as you can with no thought of where you are heading.")
    sleep(delay)
    sleep(delay)
    print("You finally stop and catch your breath. The monster had not followed you.")
    print("You are completely lost but at least there are no monsters near you, hopefully.")

elif choice2 == "charge":
    print("You may be scared but you are not a coward")
    print("Throwing caution to the wind, you sprint towards the monster as fast as you can, ")
    print("shouting at the top of your lungs")
    sleep(delay)
    print("All of a sudden the ground below you drops and you tumble down.")
    print("As you fall you hit your head on the rock multiple times.")
    print("You reach the bottom of the slope with you head busted open.\n")
    sleep(delay)
    print("YOU HAVE DIED!")
    dead = True

else:
    print("You press your self against the nearest indent in the cave wall")
    print("hoping that the darkness of the cave would be enough to hide you.")
    print("Minutes pass and you begin to calm down.")
    print("After a minute or two you begin to realize that the monster was not there anymore.")
    print("You realize that the monster was never there to begin with. ")
    print("You realize that the monster was just a figment of your flustered imagination.")
    sleep(delay)
    sleep(delay)
    print("You decide to continue on.")
    print("After a while of walking the ground begins to slop downwards.")
    print("at the bottom of the slope you see a faint light")

#########################################################################################################
# Johnathan and Will
# Refactored by Team 13

print("You choose to leave the cave.\n")
sleep(delay * 3)
print("The first thing that you see when exiting the cave is a demonic tornado from hell!")
print("As the tornado rages on you notice a tank not to far away.\n")
choice = input("Your options are either to FIGHT, RUNAWAY, or to TANK\n")
if choice == "FIGHT":
    print("As you approach the tornado, hands up screaming your battlecry, you are sucked up into it.")
    print("You burn alive as your limbs are ripped from your body.\n")
    dead = True
elif choice == "TANK":
    print("You open open up the tank hatch to find a little German man speaking Japanese")
    sleep(delay * 2)
    choice = input("You can either PUNCH him and take the tank or try to SPEAK Japanese back\n")
    if choice == "PUNCH":
        sleep(delay * 3)
        print("The man doesn't even flinch as your fist connects.")
        print("He draws his Luger and put 7 shots into your chest")
        dead = True
    elif choice == "SPEAK":
        print("You mutter something that you think sounds like Japanese to the man\n")
        sleep(delay * 2)
        print("He looks at you like you're an idiot and presses a button on the wall.\n")
        sleep(delay)
        print("The tank surprisingly fires a large burst of water from its cannon towards the tornado\n")
        sleep(delay *2)
        print("Congratulations, you survived the horrible fire tornado.")
        print("The German gives you a shiny pendant! You now continue on your journey into the unknown\n")
elif choice == "RUNAWAY":
    print(" You chose to run back into the cave.")
    sleep(delay*2)
    print("As you blindly sprint into the pitch black cave you slam into a cave wall\n")
    sleep(delay)
    print("You fall to the ground and head your head on a rock.")
    sleep(delay * 5)
    print("You wake up several hours later and don't remember anything")


#########################################################################################################
# Nmasichi, Kabelo, and Christian
# Refactored by Team 14

print("Hello " + username + " You are in heaven. You noticed you have wings on your back and you have white clothes on.... \n Kudos!!! You are an angel  ")
direction = input("where would you like to take your adventure to? You unworthy angel \n [East : You hear nothing]\n [West: You see a delicious looking apple] \n [South: You hear the cry of a child] \n [North: a woman screaming in agony]")

if direction == "west ":
    print("You are tempted to eat the Golden apple because you have heard stories of the powers you can receive from it. \n The moment you bite into the apple, you feel like you are on fire. \n You look down at yourself and you see flesh lying around your feet covered in blood. \n You feel like you are getting weak, like you may be on the verge of death. \n God has no pity. He sends you to the gate separating hell from everything, which is guarded by a big three headed dog, Cerberus. \n Once Cerberus takes note of your scent, he quickly pounces on you. The middle head bit your arm clean off, and you scream in agony.\n Cerebrus takes its left paw with its sharp claws and stabs a hole in your stomach. \n You are unable to move and begin coughing out blood. \n Cerebrus then takes 2 claws and puts them in the hole he created and rips you straight in half spewing your blood everywhere. \n You are dead   ")

    dead = True
elif direction == "east":
    print("You were not tempted by the other paths and so you are given the ability to see the near future. \n God says that there is a catch so you can't consistently use it for greed .\n You may only be able to use this ability when you are nearest to daeth as it will allow you the chance to preserve your life should you choose to do so. \n God painlessly rids you of your wings. God decides to send you to earth to carry out a normal-ish human life. ")

    sleep(delay)
else:
    print("You search for what you heard and you realize there is no one. You come to face Lucifer but you return to God. \n God smites you because you were tempted by the worst of God's creations. God grabs both bases of your wings and without any mercy he rips them from your body. \n He then banishes your pathetic being to the likes of earth. ")
    sleep(delay)


#########################################################################################################
# Trent and Dustin
# Refactored by Team 15

print("\nThis is your captain speaking\n")
sleep(delay*2)
print("We are rapidly loosing altitude and cabin pressure is becoming unstable.\nPlease follow all safety guidelines and...")
sleep(delay*5)
print("---")
sleep(delay)
print("~Everything goes dark. What was supposed to be an exciting vacation to the Caribbean has\n turned into a nightmare~")
sleep(delay)
print("---")
sleep(delay*3)
print("~You finally come to, but everything is still dark~")
sleep(delay)
print("---")
sleep(delay*3)
print("~A shaky voice can be heard in the distance~\n")
sleep(delay*3)
print("  HELLOOO... Is anyone else out here?")
sleep(delay*2)
print("---")

choice1 = input("~What do you want to do~ [call out/remain silent] ")
sleep(delay)
if choice1 == "call out":
   print("---")
   sleep(delay*2)
   print("  Sunlight floods in as David, another survivor,\n  lifts debris from the crash off of you")
   print("---")
   sleep(delay * 2)
   choice2 = input("what do you and david choose to do? [explore the island/create sos signal]")
   if choice2 == "explore the island":
       print("---")
       sleep(delay * 2)
       dead = True
   elif choice2 == "create sos signal":
        print("---")
        sleep(delay * 2)
        rescued = True
elif choice1 == "remain silent":
   print("---")
   sleep(delay*2)
   print("~you wait a while until you are sure the person the voice belonged to is gone~")
   sleep(delay)
   print("~you realise that you are pinned down by something big, and can't get out.\nYou die")
else:
    print("you remain alone walking the beaches of the island")
if dead == True:
    print("You stepped on a deadly coral snake and die.\nDavid is left to survive on the island alone")
if rescued == True:
    print("A helicopter spots the sos sign and rescues you")


#########################################################################################################
# Tristan and Azah
# Refactored by Team 16

print("You enter into the abandoned cabin, trying to find a place to rest for the night.")
sleep(delay)
print("You go to the table to start unpacking, first your backpack, and then your water.")
sleep(delay)
print("After a few minutes of trying to get your stuff set up and a fire going for the night, you begin to "
      "hear heavy footsteps outside")
sleep(delay*2)
print("Quick! Where to hide at?")
choice = ""

choice = input("Under the Table, Closet, Don't move, Play dead, ")
if choice == "Table" or choice == "table":
    print("You get under the Table, trying to make no noise.")
    sleep(delay)
    print("In through the Cabin door comes a bear! It stops, and begins sniffing the room")
    sleep(delay)
    print("It walks over to the table, stopping in front of it and growling. Uh oh, you think it's found you.")
elif choice == "Closet" or choice == "closet":
    print("You scramble to the closet, shutting it, keeping it just open enough to peek outside.")
    sleep(delay)
    print("In through the Cabin door comes a bear! It stops, and begins sniffing the room")
    sleep(delay)
    print("It lumbers over to the closet, clawing at the door and roaring. Uh oh, you think it's found you.")
elif choice == "Stand still" or choice == "stand still" or choice == "Stand Still":
    print("You hold your ground, staring at the door anxious.")
    sleep(delay)
    print("In through the Cabin door comes a bear! It stops, and stares directly at you, roaring.")
elif choice == "Play dead" or choice == "play dead" or choice == "Play Dead":
    print("You drop to the floor, trying to be as still as you can be.")
    sleep(delay)
    print("In through the Cabin door comes a bear! It stops, and begins sniffing the room")
    sleep(delay)
    print("The bear walks over to you. You can only assume it noticed your breathing, "
          "it's roared and scared you to your feet.")
sleep(delay*2)
print ("The bear seems to charging up a swing at you! ")
choice = input("Will you: Dodge, Attack, or Block? ")
if choice == "Dodge" or choice == "dodge":
    print("The bear lunges at you, and you side step the attack.")
elif choice == "Block" or choice == "block":
    print("The bear lunges at you, you hold up your shield and the bears claw's deflect off of it")
elif choice == "Attack" or choice == "attack":
    print("You swing your sword at the bear and catch it in the arm!")
    sleep(delay)
    print("You feel pretty good about yourself until the bear cracks your skull with it's claw")
    dead = True
if dead == True:
    sleep(delay)
    print("Your story ends there, Bear food.")
else:
    sleep(delay)
    print("The bear's claws whizzes by your head in a second swing. The bear falls and you stick your sword"
          " through it's skull, Good job! You finally now have a moment to relax and eat.")

# Secondary Assignment

if dead == False:
    sleep(delay)
    print("Now it's time to divide your Rations for the day")
    sleep(delay)
    choice = int(input("You have 8 Rations remaining, how many are you going to cook? "))
    if choice >=1 and choice <=2:
        print("Not a whole lot, but enough to keep you going for the day, you assume. You'll have to wait and see")
    elif choice >=3 and choice <=5:
        print("You're cooking a fair bit of your Rations. Let's hope you find more, or have enough for the week.")
    elif choice >=6 and choice <=8:
        print("At least you'll eat well tonight, you better hope it was worth it.")
    elif choice >= 9:
        print("Ambitious huh? You don't have that many Rations. You cook as many as you can.")
    elif choice <=0:
        print("None huh? Guess you're trying to keep some, smart.")
    else:
        print("You're so unsure of how many to cook, you don't cook any, you'll just go hungry tonight.")


#########################################################################################################
# Ben and Luis
# Refactored by Team 17

# Start of our code.
# gets input from the user, 1 2 or 3 for simplicity. Could do rock, sword, or cave.
print("You appear in a cave. It is dark, and smells weird. You look around...")
sleep(2)
print("You hear a growling sound coming from deeper in the cave. \nYou see a sword, a mysterious glowing green rock.")
print()
# we can either use a loop to handle 'incorrect' choices, or an else to catch anything we didn't think of.


# get input from user, present options, and store that as a string

opt1 = input("""What would you like to do?\n 
1. Pick up sword to fight off the growling monster.\n
2. Investigate the mysterious rock.\n
3. Venture deeper into the cave to try to reason with the monster.\n 
Press 1, 2, or 3 depending on your choice, or type a command.""")

# type cast the user's input as a string, and make all characters in that string lowercase.
choice = str(opt1).lower()

# neutral choice

# the user can either enter 1, sword, or fight to get this option.
if '1' in choice or "sword" in choice or "fight" in choice:
    print("""You pick up the sword, attempt to fight the monster, \n
    You manage to kill the monster, but you are badly wounded in the process. You are able to continue on.""")
    sleep(delay)
    print("""You see a growing red flask on the ground.\n
          Do you want to drink the strange liquid you found in a cave? Yes or No?""")
    opt2 = str(input("What do you want to do?")).lower()

    # special case, check if the user is named 'emily', or 'azis' and if so, do a special thing.
    if 'emily' in username.lower() or 'azis' in username.lower():
        print("A wizard changed your name. You are hereafter known only as The Old Man.")
        username = "The Old Man"
    # if user wants to drink the potion, or the liquid
    elif 'drink' in opt2 or 'potion' in opt2 or 'liquid' in opt2 or 'yes' in opt2:
        sleep(delay)
        print("seriously?")
        print("...")
        sleep(delay * 2)
        print("""You weirdo. \n 
        You literally found that on the floor of a cave...
        \n You drink the liquid, and it kills you.""")
        # they died, change the variable to reflect that.
        dead = True
    elif 'nothing' in opt2 or 'no' in opt2:
        sleep(delay * 3)
        print("Good choice. \nOnly a weirdo would drink liquid they found on the floor of a cave, right?")
        sleep(delay * 2)
        print("RIGHT...?")
        sleep(delay * 2)

        # catch any other input here. Kill them off
    else:
        sleep(delay * 2)
        print("You roll off a ledge of a hidden cliff, and die.")
        dead = True
# positive choice
elif '2' in choice or "rock" in choice or "touch" in choice:
    print("""You touch the magic rock, and you are teleported to a mysterious room.""")
    sleep(delay * 2)
    print("It is the living room of a fancy mansion.")
    MansionTest = False
    MansionRing = False
    MansionCheck3 = False
    while not MansionTest:
        print("There are 3 doors, 2 windows, and a Piano as well as some other furniture of little importance.")
        MansionChoice = input("What would you like to do?\n [Door 1/2/3] [Window 1/2] [Piano]")
        if 'piano' in MansionChoice.lower() and 'play' in MansionChoice.lower():
            print("You play a tune that you didn't know you could play.\n Congrats " + username + "!!!")
            sleep(delay)
        elif 'piano' in MansionChoice.lower():
            print("It is a very nice Piano!")
            print("You should try playing it!")
            sleep(delay)
        elif 'door' in MansionChoice.lower() and '1' in MansionChoice.lower():
            print("You opened door 1!!!")
            sleep(delay * 2)
            print("You find the owner of this mansion...")
            print("He is not happy...")
            sleep(delay)
            print("He stabs you with his knife.")
            print("You bleed out.")
            dead = True
            MansionTest = True
            sleep(delay)
        elif 'door' in MansionChoice.lower() and '2' in MansionChoice.lower():
            print("You opened door 2!!!")
            sleep(delay * 2)
            print("It is another room.")
            print("You walk in.")
            sleep(delay)
            print("And everything goes white.")
            MansionTest = True
            sleep(delay)
        elif 'door' in MansionChoice.lower() and '3' in MansionChoice.lower():
            print("You opened door 3!!!")
            sleep(delay * 2)
            print("Behind this door there is another door.")
            print("You open that door.")
            sleep(delay)
            if MansionRing:
                print("You see another room.")
                if MansionCheck3:
                    print("Wait. Was this here before?!")
                    sleep(delay)
                print("This room is like nothing you have seen before.")
                sleep(delay)
                print("You decide to go through.")
                sleep(delay)
                MansionTest = True
            else:
                print("There is an additional door behind that door.")
                print("You decide to stop and close all doors you just opened.")
                MansionCheck3 = True
                sleep(delay)
        elif 'window' in MansionChoice.lower() and '1' in MansionChoice.lower():
            print("You look through window 1!!!")
            sleep(delay * 2)
            print("It is dark outside...")
            print("Too dark to see anything...")
            sleep(delay)
            print("The darkness stares back at you...")
            sleep(delay)
            print("You witness unspeakable horrors...")
            sleep(delay)
            print("And you slip...")
            sleep(delay)
            print("Into Madness...")
            MansionTest = True
            dead = True
        elif 'window' in MansionChoice.lower() and '2' in MansionChoice.lower():
            print("You look through window 2!!!")
            sleep(delay * 2)
            print("It is very dark outside.")
            print("You can't see anything.")
            sleep(delay)
            print("You have a feeling that there is something in the furniture.")
            print("It is just a feeling, though.")
            sleep(delay)
        elif 'furniture' in MansionChoice.lower():
            print("You check through the furniture")
            sleep(delay * 2)
            print("You find ring.")
            print("It fits you perfectly!")
            sleep(delay)
            print("You decide to take it with you.")
            print("It may prove useful later.")
            sleep(delay)
            MansionRing = True
        else:
            print("You did nothing!")
            print("Please try again.")
            sleep(delay)
else:
    print("""Confused, you venture deeper into the cave, and try to talk to the monster.""")
    sleep(delay)
    print("""Thinking the monster wanted a hug, you go in to embrace it, and it eats you.""")
    dead = True

# at the end, check if user is dead or not.
if dead:
    sleep(delay)
    print("Sorry " + username + ".\n You have died. \n Better luck next time!")
# we don't need to add an else statement before the lines after this, as the "quit()" function will end the program.
    quit()


#########################################################################################################
# Minh and Taran
# Refactored by Team 18

print("")
print("You  come across a dungeon armory.")
print("the door behinds you lock behinds you as the one in front of you opens. \n")
print("what weapon would you like to use from the armory?")
print("1. Sword")
print("2. Staff")
print("3. Bow and Arrow")
print("4. bare hands")
choice_1 = input()
if choice_1 == "1":
    print("You got an iron sword!!")
    print("You see yourself as a knight")
elif choice_1 == "2":
    print("You got a wooden staff")
    print("You feel dark magic around you")
elif choice_1 == '3':
    print("You got bow and 20 arrows")
    print("you feel weird carrying the bow?")
elif choice_1 == '4':
    print("You just feel weaker than before")
else:
    print("you are kidding me right? You want that?")
    print("the story teller killed you!!!")
    dead = True

choice_2 = input("you entered the dungeon, there are 2 doors to the left and to the right, which will you choose?"   )

if choice_2 == 'left' or choice_2 == 'Left':
    print("you encounter the dark wizard")
    print("what you going to do?")
    print("1. hit     2. technique     3. run")
    fight = input()
    if fight == '1':
        print("He use thunderbolt")
        print("you fried a bit")
        if choice_1 == '1':
            print("you swing your sword, cutting him in half")
        elif choice_1 == '2':
            print("you beat him continuously with your staff")
        elif choice_1 == '3':
            print("you shoot an arrow straight into his heart")
            print("sadly you aren't cupid")
        elif choice_1 == '4':
            print("you punch him to death")
            print("whose weak now")
        print("he died")
        print("A chest appear in front of you")
        print("you open it, gold coming out, you're rich")
        print("You escape the dungeon and you live a happily life ever after. You died because of old")
        dead = True
    elif fight == '2':
        print("you dance your move in front of him, he got mad")
        print("he use his staff to whack your head")
        dead = True
    elif fight == '3':
        print("you return back to the room")
        print("you went in the other door")
        print("You see a beautiful woman sitting on the bed")
        print("1. flirt       2. 'Attack'  ")
        choice_3 = input("what will you do?")
        if choice_3 == '1' or choice_3 == '2':
            print("she turned into a dragon and ate you")
            print("you died")
            dead = True


    else:
        print("you are kidding me right?")
        print("the story teller killed you!!!")
        dead = True

elif choice_2 == "right" or choice_2 == "Right":
    print("You see a beautiful woman sitting on the bed")
    print("1. flirt       2. 'Attack'      3. run ")
    choice_3 = input("what will you do?")
    if choice_3 == '1' or choice_3 == '2':
        print("she turned into a dragon and ate you")
        print("you died")
        dead = True
    elif choice_3 == '3':
        print("you return to the room")
        print("you went to the left door")
        print("you encounter the dark wizard")
        print("what you going to do?")
        print("1. hit     2. technique  ")
        fight = input()
        if fight == '1':
            print("He use thunderbolt")
            print("you fried a bit")
            if choice_1 == '1':
                print("you swing your sword, cutting him in half")
            elif choice_1 == '2':
                print("you beat him continuously with your staff")
            elif choice_1 == '3':
                print("you shoot an arrow straight into his heart")
                print("sadly you aren't cupid")
            elif choice_1 == '4':
                print("you punch him to death")
                print("whose weak now")
            print("he died")
            print("A chest appear in front of you")
            print("you open it, gold coming out, you're rich")
            print("You escape the dungeon and you live a happily life ever after. You died because of old")
            dead = True
        elif fight == '2':
            print("you dance your move in front of him, he got mad")
            print("he use his staff to whack your head")
            dead = True
        else:
            print("you are kidding me right?")
            print("the story teller killed you!!!")
            dead = True
    else:
        print("you are kidding me right?")
        print("the story teller killed you!!!")
        dead = True
else:
    print("you are kidding me right?")
    print("the story teller killed you!!!")
    dead = True


#########################################################################################################
# Willy and Justin
# Refactored by Team 19

sleep(delay)
print()
boxes = input('You see 3 boxes in the path. You have an innate curiosity of what resides in those boxes. What would you like to do? (Open Right, Open Middle, Open Left, Keep Walking.)  ')
sleep(delay)
if boxes == "Open Right" :
    sleep(delay)
    print()
    print('A cat pops out and claws your eye out! Talk about a bad day! You are now only capable of seeing half as well!')
    sleep(delay)
elif boxes == "Open Middle":
    sleep(delay)
    print()
    print('A leprechaun pops out with a flamethrower. You have been burned by the Irishman!')
    dead = True
elif boxes == "Open Left":
    print()
    sleep(delay)
    print("A happy leprechaun pops out, hands you a shiny golden piece, and leads you on his happy journey home!")
else:
    sleep(delay)
    print("You continue walking in the darkness ahead, fearful of what resides in the boxes. You are still lost.")
if dead == True:
    print()
    print('You have died! By a leprechaun! HAHAHAHAHAHAHAHAHAHAHA!!!!')
    quit()


#########################################################################################################
# Bryan and Hailey (Fall 2018)
# Refactored by Team 20

print()
print(username, "continues on their quest")
sleep(delay)
print("You continue your path in the forest")
print("As you walk through the forest, you encounter a bear wearing a fez and sunglasses.")
print(
    "You notice that the fez has the name 'Bosco' labeled on it. You deduce that this is the famous runaway circus bear, Bosco the Bear.")
sleep(delay)
print()
print("However, Bosco has took notice of you and stands on his hind legs and takes interest in you.")
print("You must make a choice, or it could end very badly for you!")

choice = input("What would you like to do? [Entertain or Fight?]")

if choice == "Fight":
    #Good Choice!
    print("You choose to engage in fisticuffs with Bosco the Bear. This seems like a very bad idea.")
    print()
    sleep(delay)
    print("Luckily for you, Bosco the Bear lived in the circus his whole life. He does not know how to fight.")
    print("Feeling intimated, Bosco the Bear flees. Dropping his fez and glasses.")
    print()
    print("You are free to continue on your journey while rocking the fez and glasses. Well at least you look nice.")
    print()
elif choice == "Entertain":
    # Bad Choice
    print("Bosco the Bear is not amused with your performance.")
    print()
    sleep(delay)
    print("He ran away from the circus because he hated that life.")
    print("Your entertainment reminded him of that hatred. How inconsiderate of you.")
    print()
    sleep(delay)
    print("In a fit of rage, Bosco the Bear kills you with his bare hands.")
    print()
    dead = True
else:
    #Neutral Choice
    print("Bosco the Bear is confused by your actions.")
    print("Bosco the Bear does not see you as a threat and leaves.")
    print()
    print("You are free to continue on your journey.")
    print()

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hiting the green play button. ")
    quit()