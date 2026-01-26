# Enter name: Daniel Lewis

#uptherebels
county = ["Dublin", "Laois", "Dublin", "Dublin", "Dublin", "Dublin", "Dublin", "Kildare", "Laois", "Kildare", "Dublin", "Laois", "Dublin"]

rent = [2500, 1200, 2000, 2100, 1900, 1999, 1790, 1500, 1000, 1390, 1980, 1105, 1999]

# Part i
print()
print(f"The total people in the survey is: {len(rent)+1}") # +1 to account for inputs in part ii
print()

# Part ii
acceptablecounties = ["Laois", "Kildare", "Dublin"]
loopguard = True
while loopguard:
    inputcounty = input("Please enter your county :")
    if inputcounty in acceptablecounties:
        county.append(inputcounty)
        loopguard = False
    else:
        print("Invalid entry")
inputrent = int(input("Please enter your total monthly rent :"))
rent.append(inputrent)
print()

print("-"*18)
print("{:<12}".format("County")+"{:<12}".format("Rent €"))
print("-"*18)
for index in range(len(county)):
    print("{:<12}".format(county[index])+"{:<12}".format(rent[index]))
print()

# Part iii
total = 0
for tenant in rent:
    total += tenant
average = round(total / len(rent), 2)
print(f"The average rent value is {average} euro / month across all three counties")

# Part iv
DBtotal = 0
KDtotal = 0
LStotal = 0
DBcount = 0
KDcount = 0
LScount = 0
for tenant in range(len(rent)):
    if county[tenant] == "Laois":
        LStotal += rent[tenant]
        LScount += 1
    elif county[tenant] == "Kildare":
        KDtotal += rent[tenant]
        KDcount += 1
    elif county[tenant] == "Dublin":
        DBtotal += rent[tenant]
        DBcount += 1
    else:
        print("There has been a mistake")
LSavg = round(LStotal / LScount, 2)
KDavg = round(KDtotal / KDcount, 2)
DBavg = round(DBtotal / DBcount, 2)
print(f"The average rent is {LSavg} per month in Laois")
print(f"The average rent is {KDavg} per month in Kildare")
print(f"The average rent is {DBavg} per month in Dublin")
