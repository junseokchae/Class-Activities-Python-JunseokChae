#####################################################
############## Eureka Water Company #################
#####################################################

#0. Situation
#Eureka Water Company charges the homeowner a single rate based on the total amount of water used by a customer in the billing period.
# The amount charged will be calculated based on which of the following ranges their total water usage falls under.
# Note, it is not a cumulative charge.
# Your program will figure out which single range the usage falls into, then calculate the cost based on that range’s cost.
# Up to and including 1000 cubic feet -> $15.00 flat rate
# Over 1,000 cubic feet and up to and including 2,000 cubic feet -> $0.0175 per cubic foot
# Over 2,000 cubic feet and up to and including 3,000 cubic feet -> $0.02 per cubic foot
# Over 3,000 cubic feet -> $70.00 flat rate

#1. Flow Chart
#1. Start
#2. Input the amount
#3. Decision point: 1 -> amount <= 1000? -> Yes: rate = 15
#4. Decision point: 2 -> 1000 < amount <= 2000? -> Yes: rate = amount * 0.0175
#5. Decision point: 3 -> 2000 < amount <= 3000? -> Yes: rate = amount * 0.02
#6. Decision point: 4 -> amount > 3000? -> Yes: rate = 70
#7. Output the amount
#8. Finish

#2. Intro to Program
print("-" * 100)
print("Eureka Water Company")
print("-" * 100)
print("\nWe will serve you best quality of water with reasonable price")

#3. Input the data
amount = float(input("\nEnter usage of water (cubic feet): "))
# the usage is number, so we need to change the data into float.

#4. Calculation
while amount < 0:
    print("The amount you entered is smaller than 0. It is weird.")
    amount = float(input("\nEnter usage of water (cubic feet): "))

if amount == 0:
    rate = 0
elif amount <= 1000:
    rate = 15
elif amount <= 2000:
    rate = amount * 0.0175
elif amount <= 3000:
    rate = amount * 0.02
else:
    rate = 70

#5. Display the result
print("Your total charge is ${:.2f}".format(rate))
#The cost should be fitted into currency format which has two digits after the decimal point.



