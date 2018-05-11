from sys import exit
#room 1: start. Room 2: knife. Room 3: death. Room 4: cookie. Room 5: Nothing. Room 6: beast, key. Room 7(locked): treasure.
beast = True 
knife = False
key = False
cookie = False
treasure = False

#room 1

def room_1():
    print ""
    print "You find yourself in a small, dimly lit room."
    print "There are four doors outlined by the rock: East, West, North, and South."
    print "Which will you go through?"

    choice = raw_input("> ");

    if "north" in choice:
        room_2()
    elif "south" in choice:
        room_5()
    elif "east" in choice:
        room_7()
    elif "west" in choice:
        crossroads()
    elif "stay" in choice:
        print "You will die if you stay here."
        room_1()
    elif "none" in choice:
        print "You will die if you stay here."
        room_1()
    else:
        room_1()
#room 2

def room_2():
    global knife
    print ""
    print "A deep, musty room filled with empty racks and pots."
    print "A pile of rusty knives rests on a rotted table."
    print "A rat is sitting on one of the racks."
    print "There are no doors besides the south one you came through."
    print "What will you do?"
    choice = raw_input("> ");

    if "south" in choice:
        print "You turn back."
        room_1()
    elif "knife" in choice:
        print "+You take a knife and strap it to your belt. It's better than nothing."
        knife = True
        room_2()
    elif "rat" in choice:
        print "The rat scampers away before you can react. It will surely return later."
        room_2()
    else:
        room_2()

#room 3

def room_3():
    death("""The passage narrows as you go along. 
    Soon, you have to squeeze through the rocks to make progress.
    It was a mistake to come this far, but it's too late now. 
    You find yourself stuck, and eventually die alone of suffocation.""")

#room 4

def room_4():
    global cookie
    print ""
    print "A suprisingly clean, cramped room."
    print "The only occupant is a round table with an overflowing plate of supiciously warm cookies."
    print "Will you take a cookie? [y/n]"

    choice = ""
    while choice != "y" and choice != "n":
         choice = raw_input("> ");
         if choice == "y":
             cookie = True
             print "+You take a cookie without much incident."
         elif choice == "n":
             print "In a faraway land, a shaggy blue monster shudders."
    print "There are two doors, one to the South and one to the East."
    print "Will you go South or East?"
    choice = raw_input("> ");

    if "east" in choice:
        crossroads()
    elif "south" in choice:
        room_5()
    else:
        room_4()

#room 5

def room_5():
    print ""
    print "This room is refreshingly roomy, spotted with plants and fungus."
    print "Vines hug the cracked walls. Strange, dark fruit grows in clumps."
    print "There are three doors, each leading North, South, or West."
    print "Which door do you choose?"
    choice = raw_input("> ");

    if "fruit" in choice:
        print ""
        print "Don't touch the fruit."
        print ""
        room_5()
    elif "north" in choice:
        room_1()
    elif "south" in choice:
        room_6()
    elif "west" in choice:
        room_4()
    else:
        room_5()

#room 6

def room_6():

    global beast
    global cookie
    global knife
    global key
    print ""
    print "An enormous, brightly lit room with one door. The walls are streaked with hair and blood." 

    if beast:
        print ""
        print "In the depths of this cavern, a huge mass stirs."
        print "A great shaggy beast, big enough to rival a bus, paws at the ground and snorts."
        print "It shakes its huge mane, dislodging a lifetime's worth of dust and spiders."
        print "For a brief moment, you can see a set of keys glint on a string around its neck."
        print "What will you do?"

        choice = raw_input("> ");

        if ("knife" in choice) and knife:
            print ""
            print "You take the rusty knife from your belt."
            print "The beast rushes you, roaring, but you hold the knife high."
            print "As it aims to take your head, you take its life with a purposeful thrust."
            print "The knife buries itself deep in its hide, slicing through the string that held the key."
            print "The beast falls. You feel an odd, deep sadness."
            print "+You take the key."
            key = True
            beast = False
            room_6()
        elif ("beast" in choice) and key:
            print ""
            print "You already have a key. Best to leave it alone."
            room_6()
        elif ("door" in choice) and key:
            print ""
            print "You already have a key. You go through the door."
            room_5()
        elif ("fight" in choice) and key:
            print ""
            print "You already have a key. Best to leave it alone."
            room_5()
        elif ("fight" in choice) and knife:
            print ""
            print "You take the rusty knife from your belt."
            print "The beast rushes you, roaring, but you hold the knife high."
            print "As it aims to take your head, you take its life with a purposeful thrust."
            print "The knife buries itself deep in its hide, slicing through the string that held the key."
            print "The beast falls. You feel an odd, deep sadness."
            print "+You take the key."
            key = True
            beast = False
            room_6()
        elif ("stab" in choice) and knife:
            print ""
            print "You take the rusty knife from your belt."
            print "The beast rushes you, roaring, but you hold the knife high."
            print "As it aims to take your head, you take its life with a purposeful thrust."
            print "The knife buries itself deep in its hide, slicing through the string that held the key."
            print "The beast falls. You feel an odd, deep sadness."
            print "+You take the key."
            key = True
            beast = False
            room_6()
        elif ("cookie" in choice) and cookie:
            print ""
            print "You take the cookie from your pocket. The beast perks up."
            print "You hold the cookie high, and the beast takes it gently."
            print "+As it chews the cookie contentedly, you take a key from its neck."
            key = True
            cookie = False
            room_6()
        elif ("feed" in choice) and cookie:
            print ""
            print "You take the cookie from your pocket. The beast perks up."
            print "You hold the cookie high, and the beast takes it gently."
            print "+As it chews the cookie contentedly, you take a key from its neck."
            key = True
            cookie = False
            room_6()
        elif "leave" in choice:
            print ""
            print "You sprint to the door."
            print "It lets you pass, watching you closely."
            room_5()
        elif "flee" in choice:
            print ""
            print "You sprint to the door."
            print "It lets you pass, watching you closely."
            room_5()
        elif "door" in choice:
            print ""
            print "You sprint to the door."
            print "It lets you pass, watching you closely."
            room_5()
        elif "fight" in choice:
            print ""
            death("""You taunt the beast. Bad move. It strikes you dead with one blow.""")
        elif "i holler at the zoo animals" in choice:
            print ""
            print "YOU FACE GOD AND WALK BACKWARDS INTO HELL."
            print "+A key manifests itself in your pocket out of fear."
            key = True
            room_6()
        else:
            death("""Before you can react, the beast rushes you. It swats you down and tears off your head in one bite.""")
    else: 
        room_6()
    
        
        

#room 7

def room_7():
    global key
    global treasure
    print ""
    print "You push on the door, but it won't budge. It seems to be locked."
    print "The only other exit is the West door you came from."
    if key:
        print ""
        print "You insert the key into the door and turn. The door swings open smoothly."
        print "As you enter the small, plain room, the door closes by itself. You can hear the lock click."
        print "You cannot go back that way..."
        print ""
        print "Inside, there are two unlocked doors to your right and left."
        print "An unimpressive wooden box sits quietly in the middle."
        print "What will you do?"
        choice = raw_input("> ");

        if "box" in choice:
            if not treasure:
                print ""
                print "You open the box, not expecting much."
                print "Inside, though, is a sight that makes you shiver with anticipation."
                print "A pirate's bounty of gold and gems sits unclaimed and ready for you to take."
                print "You gather all of it into your pockets, grinning ear to ear."
                treasure = True
            else:
                print "There's nothing there."
        elif "left" in choice:
            death("""You take only a few steps towards the door on the left before the floor collapses underneath you.
            You fall, hitting the ground several seconds later, and die instantly.""")
        elif "right" in choice:
            jungle()
        else:
            print "You can't make up your mind what to do and simply leave. The door takes pity on you and opens."
            room_1()
    else:
        choice = raw_input("> ");

        if "west" in choice:
            room_1()
        elif "open up, bastard" in choice:
            print ""
            print "The door swings open, thoroughly intimidated."
            print "As you enter the small, plain room, the door closes by itself. You can hear the lock click."
            print "You cannot go back that way..."
            print ""
            print "Inside, there are two unlocked doors to your right and left."
            print "An unimpressive wooden box sits quietly in the middle."
            print "What will you do?"
            choice = raw_input("> ");

            if "box" in choice:
                if not treasure:
                    print ""
                    print "You open the box, not expecting much."
                    print "Inside, though, is a sight that makes you shiver with anticipation."
                    print "A pirate's bounty of gold and gems sits unclaimed and ready for you to take."
                    print "You gather all of it into your pockets, grinning ear to ear."
                    print "You decide you'd like to leave now. Which way?"
                    treasure = True
                    choice = raw_input("> ");

                    if "left" in choice:
                        death("""You take only a few steps towards the door on the left before the floor collapses underneath you.
                You fall, hitting the ground several seconds later, and die instantly.""")
                    elif "right" in choice:
                        jungle()
                    else:
                        print "A strange force compells you to turn right."
                        jungle()
                else:
                    print "There's nothing there."
            elif "left" in choice:
                death("""You take only a few steps towards the door on the left before the floor collapses underneath you.
                You fall, hitting the ground several seconds later, and die instantly.""")
            elif "right" in choice:
                jungle()
            else:
                print "You can't make up your mind what to do and simply leave."
                room_1()
        else:
            room_7()
    choice = raw_input("> ");

    if "west" in choice:
        room_1()
    elif "open up, bastard" in choice:
        print ""
        print "The door swings open, thoroughly intimidated."
        print "As you enter the small, plain room, the door closes by itself. You can hear the lock click."
        print "You cannot go back that way..."
        print ""
        print "Inside, there are two unlocked doors to your right and left."
        print "An unimpressive wooden box sits quietly in the middle."
        print "What will you do?"
        choice = raw_input("> ");

        if "box" in choice:
            if not treasure:
                print ""
                print "You open the box, not expecting much."
                print "Inside, though, is a sight that makes you shiver with anticipation."
                print "A pirate's bounty of gold and gems sits unclaimed and ready for you to take."
                print "You gather all of it into your pockets, grinning ear to ear."
                treasure = True
                print "Which door do you choose?"
                choice = raw_input("> ");

                if "left" in choice:
                    death("""You take only a few steps towards the door on the left before the floor collapses underneath you.
                    You fall, hitting the ground several seconds later, and die instantly.""")
                elif "right" in choice:
                    jungle()
                else:
                    print "You can't make up your mind what to do and simply leave. The door pities you and opens."
                    room_1()
            else:
                print "There's nothing there."
        elif "left" in choice:
            death("""You take only a few steps towards the door on the left before the floor collapses underneath you.
            You fall, hitting the ground several seconds later, and die instantly.""")
        elif "right" in choice:
            jungle()
        else:
            print "You can't make up your mind what to do..."
            room_7()
    

#crossroads

def crossroads():
    print ""
    print "There are three passages. The one to the East leads to the room you fell into. The others lead North and South."
    print "Where will you go?"
    choice = raw_input("> ");

    if "east" in choice:
        print "You go East."
        room_1()
    elif "north" in choice:
        print "You go North."
        room_3()
    elif "south" in choice:
        print "You go South."
        room_4()
    else:
        crossroads()

def jungle():
    print ""
    print "You find yourself in a long, twisting corridor. Many painful, dusty steps later, a light becomes visible above you."
    print "You look up to see a hole in the ceiling."
    print "Will you climb up the hole?"
    choice = raw_input("> ");
    
    if "yes" in choice:
        print ""
        print "Ready to leave, you climb the hole, and not a moment too soon."
        print "As soon as you feet leave the ground, the dirt below you caves in, giving a glimpse of a bottomless cavern."
        print "You force your way through the roots and thick vegetation above."
        print "You finally reach the surface, never so happy to find yourself in a jungle."
        print "You escaped the Underground!"
        print "Do you want to play again? [y / n]"

    choice = ""
    while choice != "y" and choice != "n":
        choice = raw_input("> ")
        if choice == "y":

            start()
        elif choice == "n":
            exit(0)
    else:
        death("""You consider climbing up, but it's too late. The dirt caves beneath your feet.
        You fall through, down through a seemingly bottomless cavern.
        A minute later, you hit water at the very depths, and the shock kills you instantly.""")

#start

def start():
    print "Brought here by rumors of treasure, you forge ahead alone in a sweltering jungle with nothing but the clothes on your back."
    print "Your mind wanders as you trek, thinking of home, so you aren't paying attention to the path ahead."
    print "You take one wrong step and fall through an open pit."
    print "You don't fall far, but the tunnel twists and knocks you around so that you cannot see the light."
    print "A moment later, you stand and brush yourself off..."
    print ""
    room_1()

#THOU ART DEAD
#(hahahaha)
def death(d):

    global beast
    global dragon_alive
    global knife
    global key

    beast = True
    cookie = False
    knife = False
    key = False

    print d
    print "Do you want to play again? [y / n]"

    choice = ""
    while choice != "y" and choice != "n":
        choice = raw_input("> ")
        if choice == "y":

            start()
        elif choice == "n":
            exit(0)
    
start()