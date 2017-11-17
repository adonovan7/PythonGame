from sys import exit


def first_branch():
    print ("")
    print ("You continue walking along in the dark maze.")
    print ("You come to a fork in the path, one path is guarded by a mean witch and the other path is guarded by thorns and traps.")
    print ("")
    print ("Which path do you take? (Type witch / thorns)")
    next = input("> ")
    if next == "thorns":
        print ("Ouch! A thorn stabs you through the heart. Do you want to choose again (Type yes/ no)")
        next = input("> ")
        if next == "no":
            dead("The thorn kills you...")
        else:
            first_branch()
    elif next == "witch":
        witch()
    else:
        print ("that wasn't an option... Try again")
        first_branch()

 
def witch():
    print ("")
    print ("You must answer a riddle to pass the witch.")
    print ("")
    print ("She asks: Where did the program name 'Python' come from? (Type monte python/ snake)")
    next = input("> ")
 
    if next == "snake":
        dead("Nope! The witch heckles and burns you to a crisp.")
    elif next == "monte python":
        print ("The witch screams and melts. You can now continue on.")
        gold_room()
    else:
        print ("The witch has no idea what that means... try again?")
        witch()
 
def gold_room():
    print ("")
    print ("You have reached the center of the maze.")
    print ("In the center of the maze lies two boxes: One contains gold coins and endless riches....and the other contains the knowledge to use Django...")
    print ("")
    print ("Which do you choose? (Django / gold) ")
    
    next = input("> ")
 
    if next =="Django":
        print ("You made the right choice!")
        print ("Knowledge is golden!")
        print ("Enjoy the tutorial!!")
        exit(0)
    elif next== "gold":
        print ("All of the gold in the world can’t teach you Django. That’s what we’re here for! Enjoy the tutorial.")
        exit(0)
 
    else:
        dead("That wasn’t an option. You died...")
 
 
def fountain():
    print ("")
    print ("You arrive at an opening in the maze and see a fountain.")
    print ("Above the fountain is a sign that states ‘Magical water, Beware!'")
    print ("'Look in the fountain.. if you dare!'")
    print ("")
    print ("Do you drink the water, jump into the fountain, or continue on? (Type: drink / jump / continue)")
 
    next = input("> ")
 
    if "continue" in next:
        print ("Well that's no fun! Try again...")
        fountain()
    elif "drink" in next:
        print ("Ahhh, so refreshing")
        first_branch()
    elif "jump" in next:
        print ("It was a magic portal! You are transported away...")
        gold_room()
    else:
        print ("Not this time, you rebel. Try again!")
        fountain()
 
 
def dead(why):
    print (why, "Bummer!")
    print ("")
    print ("")
    print ("")
    print ("THE END")
    exit(0)
 
def start():
    print ("You are wandering in a forest and stumble upon a magical labyrinth.")
    print ("✧･ﾟ: *✧･ﾟ:* *:･ﾟ✧*:･ﾟ✧  ✧･ﾟ: *✧･ﾟ:* *:･ﾟ✧*:･ﾟ✧")
    print ("There are two paths, one to your left and one to your right.")
   print ("")
   print ("Which path do you choose? (left / right) ")

    next = input("> ")
 
    if next == "left":
        fountain()
    elif next == "right":
        first_branch()
    else:
        dead("That wasn't an option! A lion emerges from the maze and eats you.")
 
 
start()
