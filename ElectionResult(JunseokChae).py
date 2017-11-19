###############################################
############## Election #######################
###############################################

# Ask the user how many candidates are running in the current election,
numofcandidates = int(input("Enter the number of the candidates: "))
# For each numbered candidate up to the user-entered count of candidates, allow the user to enter a name
# and the number of votes that person received.
candidates = []
votes = []
for i in range (numofcandidates):
    candidates.append(input("\nEnter the name of candidate " + str(i+1) + ": "))
    votes.append(int(input("Enter the number of votes for candidate " + str(i+1) + ": ")))
#the number of candidates are varies so range of for loop should be varied
#by making lists, we manage various numbers of variables
# Calculate and output a list of all candidate names,
sumofvotes = sum(votes)
votesrates = []
firstorlast = []
print("\nElection Results")
print("-"*150)
for i in range (numofcandidates):
    votesrates.append(votes[i]/sumofvotes*100)
    if votes[i] == max(votes):
        firstorlast.append("<-- First Place")
    elif votes[i] == min(votes):
        firstorlast.append("<-- Last Place... HAHAHAHA!")
    else:
        firstorlast.append("")
#Don't forget the else part, if you forget, the first candidate will have the value of First Place and the second candidate will have the value of Last Place
# Display what share of the total vote, as a percentage, that each candidate won,
    print("{0}      - {1:.1f}% {2}".format(candidates[i], votesrates[i],firstorlast[i]))
#We can print various things at once by using format
# Highlight the candidate(s) with highest and lowest vote counts