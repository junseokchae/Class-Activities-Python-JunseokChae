#####################################################
################ Vowel Counter ######################
#####################################################

# Take a sentence or phrase as input,
# Count the number of occurrences of each vowel in the user-entered sentence, regardless of case sensitivity,
# Display the counts per vowel to the user,
# The program will keep asking the user to enter a new sentence until the user enters the command ‘quit’
sentence = ""
#defining a variable and making it into the loop
while sentence != "quit":
    sentence = input("\nType a phrase(or quit to exit program): ").lower()
    a = sentence.count("a")
    e = sentence.count("e")
    i = sentence.count("i")
    o = sentence.count("o")
    u = sentence.count("u")
    print("\nLetter A count: "+str(a))
    print("Letter E count: " + str(e))
    print("Letter I count: " + str(i))
    print("Letter O count: " + str(o))
    print("Letter U count: " + str(u))

