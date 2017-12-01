#######################################################
################# Battle Ship #########################
#######################################################

import random
rand1 = random.randint(0,99)    #Set a ships position by random
rand2 = random.randint(0,99)    #Set a ships position by random
while rand1 == rand2:
    rand2 = random.randint(0, 99)   #No two ships' positions should be identical
rand3 = random.randint(0,99)    #Set a ships position by random
while rand1 == rand3 or rand2 == rand3:
    rand3 = random.randint(0, 99)   #No two ships' positions should be identical
rand4 = random.randint(0,99)    #Set a ships position by random
while rand1 == rand4 or rand2 == rand4 or rand3 == rand4:
    rand4 = random.randint(0, 99)   #No two ships' positions should be identical
rand5 = random.randint(0,99)    #Set a ships position by random
while rand1 == rand5 or rand2 == rand5 or rand3 == rand5 or rand4 == rand5:
    rand5 = random.randint(0, 99)   #No two ships' positions should be identical


print("LET'S PLAY BATTLESHIP!!")
line0 = ["   ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
line1 = ["1  ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
line2 = ["2  ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
line3 = ["3  ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
line4 = ["4  ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
line5 = ["5  ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
line6 = ["6  ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
line7 = ["7  ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
line8 = ["8  ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
line9 = ["9  ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
line10 = ["10 ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
MAP = [line0, line1, line2, line3, line4, line5, line6, line7, line8, line9, line10]    #Making a two-dimensional list
for line in MAP:
    print(" ".join(line))   #joining for printing it smoothly
ships = 5
missles = 30
hits = []
misses = []
while ships > 0 and missles > 0:    #if ships or missles become 0, the game should be over
    target = input("Choose your target (Ex: A1): ").lower()
    targetletter = target[0]    #the letter part would be the column
    targetrow = target[1:]      #the number part would be the row
    while (targetletter != "a" and targetletter != "b" and targetletter != "c" and targetletter != "d" and \
                       targetletter != "e" and targetletter != "f" and targetletter != "g" and targetletter != "h" \
                   and targetletter != "i" and targetletter != "j")\
            or (targetrow != "1" and targetrow != "2" and targetrow != "3" and targetrow != "4" and targetrow != "5"\
                and targetrow != "6" and targetrow != "7" and targetrow != "8" and targetrow != "9" and targetrow != "10"):
            #if the entry is not valid, the user should enter the data once more
        print("Invalid entry - please enter a letter(A-J) and number(1-10)")
        target = input("Choose your target (Ex: A1): ").lower()
        targetletter = target[0]
        targetrow = target[1:]
    targetrow = int(targetrow)
    if targetletter == "a":
        targetcolumn = 1
    elif targetletter == "b":
        targetcolumn = 2
    elif targetletter == "c":
        targetcolumn = 3
    elif targetletter == "d":
        targetcolumn = 4
    elif targetletter == "e":
        targetcolumn = 5
    elif targetletter == "f":
        targetcolumn = 6
    elif targetletter == "g":
        targetcolumn = 7
    elif targetletter == "h":
        targetcolumn = 8
    elif targetletter == "i":
        targetcolumn = 9
    elif targetletter == "j":
        targetcolumn = 10
    #changing the data entry into the number
    targetnumber = (targetcolumn-1)*10 + targetrow - 1
    if targetnumber == rand1 or targetnumber == rand2 or targetnumber == rand3 or targetnumber == rand4 or targetnumber == rand5:
        ships = ships - 1
        missles = missles - 1
        MAP[targetrow][targetcolumn] = "X"
        print("HIT!!!\nMissles Remaining: " + str(missles))
    #if the entered number is in the ships positions' list, it would be hit


    else:
        missles = missles - 1
        misses.append(targetnumber)
        MAP[targetrow][targetcolumn] = "O"
        print("Miss!!!\nMissles Remaining: " + str(missles))
    for line in MAP:
        print(" ".join(line))
#if it is not, it would be miss
if ships == 0:
    print("CONGRATULATIONS!! YOU WON THE GAME!!")
#If the game is over and no more ships are there, the user wins!
else:
    print("SORRY, YOU RAN OUT OF MISSILES....BETTER LUCK NEXT TIME")
#If the game is over and ship are still there, the user loses!