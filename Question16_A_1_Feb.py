#Question 16(a)
#Write your name here: Daniel Lewis

# Unsure exactly what is meant by part i, in an exam would default to printing the formulae jic?

# Define variables

wages = int(input("Please enter your annual wages: "))

taxCredits = 1700

cutoff = 36800

totalTax = round((cutoff * 0.2) + ((wages - cutoff) * 0.4) - taxCredits, 2)

netIncome = wages - totalTax

percentageLost = round((totalTax / wages) * 100, 2)

# Define functions

def income_tax(wages):
    #print("Welcome to my income tax calculator")
    if wages >= cutoff:
        print("You will have to pay income tax")
        print("Your income tax bill is: €", totalTax)
        print(f"You lost {percentageLost}% of your income to tax")
        
    else:
        print("You pay no income tax")

# Main body

income_tax(wages)       
