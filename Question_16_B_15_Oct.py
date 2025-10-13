# Question 16(b)
# Student Name: Daniel Lewis

def euro_format(price):
    price = str(price)
    price_list = list(price)
    price_list.insert(0, '€')
    while len(price_list) < 5:
        price_list.append('0')
    price = ''.join(price_list)
    return price
    

def display_table(Dict):
    print()
    print('=== Your Shopping List ===')
    for item, price in Dict.items():
        price = euro_format(price)
        print(f'{item}\t\t{price}')

items = {} # Dictionary to store items and prices together

print('Shopping Trip Calculator') # title

print()
no = int(input('Enter how many items would you like to add to this list: ')) # Get list length

for i in range(no): # Add the specified number of items to the list
    print()
    name = input('Enter the item\'s name :') 
    price = round(float(input('Enter this item\'s price :')), 2) # Round to 2 for money
    items[name] = price
    
display_table(items)

print()
print('=== Shopping Summary ===')
total = 0
maximum = 0
maxItem = 0
minItem = 0
minimum = 10000000000000000 # absurdly large number
for item in items:
    price = items[item]
    total += price
    if price > maximum:
        maximum = price
        maxItem = item
    if price < minimum:
        minimum = price
        minItem = item
average = round(total / no, 2)
print(f'Total cost: {euro_format(total)}')
print(f'Most expensive item: {maxItem} ({euro_format(maximum)})')
print(f'Least expensive item: {minItem} ({euro_format(minimum)})')
print(f'Average price per item: {euro_format(average)}')

budget = round(float(input('Enter your budget :')), 2)
if total > budget:
    print('You are over budget!')
    print(f'Additional money needed: {euro_format(total - budget)}')
else:
    print('You are within budget!')
    print(f'Money remaining: {euro_format(budget - total)}')

print()
print('=== Items by Price (High to Low) ===')
sortedDict = sorted(items.items(), key  = lambda item : item[1])
display_table(sortedDict)
