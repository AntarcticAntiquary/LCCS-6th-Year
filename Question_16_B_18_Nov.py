#Question 16 (b)
#Student name: Daniel Lewis
import random as r

ticket = []

# part (ii)
def checkResult (ticket, result):
    for num in ticket:
        if num in result:
            result.remove(num)
        else:
            print ("You lose!")
            return False
    print ("You win!")
    return True

# userNumber = int (input ("Please pick a number between 1 and 10 :"))
# ticket.append(userNumber)
# userNumber = int (input ("Please pick a number between 1 and 10 :"))
# ticket.append(userNumber)
# userNumber = int (input ("Please pick a number between 1 and 10 :"))
# ticket.append(userNumber)

# part (i)
for i in range (3):
    userNumber = int (input ("Please pick a number between 1 and 10 :"))
    ticket.append(userNumber)

print (f"Your ticket is {ticket}")
print ("The draw will start now, good luck!")
drum = [1,2,3,4,5,6,7,8,9,10]
result = []
def lotto (ticket):
    for times in range (3):
        draw = drum [r.randint (0, len(drum)-1)]
        result.append (draw)
        drum.remove (draw)
    print (f"The draw was {result}")
        
lotto (ticket)
checkResult (ticket, result)
