# Question 16(a)
# Examination Number: Daniel Lewis

def display_list():
    global shopping_list
    shopping_list.sort() # part(v)
    print()
    print("Shopping List:")
    counter = 1 # part (i)
    for item in shopping_list:
        print(str(counter)+'.', item)
        counter += 1 # increment counter
    print()
    print('Total items:', len(shopping_list)) # part(ii)
    

shopping_list = ["milk", "bread", "eggs"]

display_list()

print()
new = input('Enter a new item: ') # part (iii)
shopping_list.append(new)

display_list()

print()
remove = input('Enter an item to remove: ') # part (iv)
if remove in shopping_list:
    shopping_list.remove(remove)
    print(f'{remove} has been removed from the list')
else:
    print(f'{remove} is not in the shopping list')
    
print()
display_list()

print()
target = input('Enter an item to search for: ')
target = target.lower()
if target in shopping_list:
    pos = shopping_list.index(target)
    print(f'{target} is in the shopping list at position {pos}')
else:
    print(f'{target} is not in the shopping list')
