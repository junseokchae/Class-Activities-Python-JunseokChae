#############################################
############# Tax Schedule ##################
#############################################

#0. Situation
#0-1. Single
#0-1-1. 0~8000 -> 10%
#0-1-2 8000-32000 -> 800 + 15%
#0-1-3 32000 -> 4400 + 25%

#0-2. Married
#0-2-1. 0-16000 -> 10%
#0-2-2.16000-64000 -> 1600 + 15%
#0-2-3. 64000- -> 8800 + 25%

#1. Flowchart
#1. Start
#2. Input(Marriage Status, Taxable income)
#3-1. Decision Point: Marriage Status = Single? -> Yes: 3-1-1, No: 3-2
#3-1-1. Decision Point: Income <= 8000? -> Yes: Tax = 0.1 * Income, No: 3-1-2
#3-1-2. Decision Point: Income <= 32000? -> Yes: Tax = 0.15 * (Income - 8000) + 800, No: Tax = 0.25 * (Income - 32000) + 4400
#3-2. Decision Point: Marriage Status = Married?
#3-2-1. Decision Point: Income <= 16000? -> Yes: Tax = 0.1 * Income, No: 3-2-2
#3-2-2. Decision Point: Income <= 64000? -> Yes: Tax = 0.15 * (Income - 16000) + 1600, No: Tax = 0.25 * (Income - 64000) + 8800

#2. Intro to Program
print("-"*100)
print("Tax Schedule")
print("-"*100)
print("\nWe will calculate your tax amount!")

#3. Data Entry

marriagestatus = input("\nEnter your marritial status(Married, Single): ").lower()
while marriagestatus != "married" and marriagestatus != "single":
    print("You have entered the wrong value. Please try again.")
    marriagestatus = input("\nEnter your marritial status(Married, Single): ").lower()
#In case user type capital or lower letter other than I code, I will store the users' input into lower case.
taxableincome = float(input("Enter your taxable income($): "))
while taxableincome < 0:
    print("The value cannot be lower than zero. Please enter the value again.")
    taxableincome = float(input("Enter your taxable income($): "))

#4. calculate the tax
if marriagestatus == "single":
    if taxableincome <= 8000:
        tax = taxableincome * 0.1
    elif taxableincome <= 32000:
        tax = (taxableincome-8000) * 0.15 + 800
    else:
        tax = (taxableincome-32000) * 0.25 + 4400
elif marriagestatus == "married":
    if taxableincome <= 16000:
        tax = taxableincome * 0.1
    elif taxableincome <= 64000:
        tax = (taxableincome-16000) * 0.15 + 1600
    else:
        tax = (taxableincome-64000) * 0.25 + 8800

#5. Display the result
print("\nYour total tax is ${:.2f}".format(tax))
