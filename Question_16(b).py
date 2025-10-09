# Question 16 (b)
# Daniel Lewis

def percentify(score):
    percentage = round((score / totalMarks) * 100, 1)
    return percentage

totalMarks = 200
results = {}

keepGoing = True
while keepGoing:
    name = input('Please enter the student\'s name and enter \'end\' or \'End\' when complete: ')
    if name == 'end' or name == 'End':
        break
    else:
        results[name] = 0
    
print()

highest = 0
lowest = totalMarks
highestGuy = 'No-one'
lowestGuy = 'Nobody'
totalScores = 0
    
for student in results:
    score = int(input('Please enter ' + student + '\'s results: '))
    results[student] = score
    totalScores += score
    if score > highest:
        highest = score
        highestGuy = student
    if score < lowest:
        lowest = score
        lowestGuy = student
    
print()
print('Student\'s results are:', results)
print()

print(highestGuy, 'scored the highest mark,', percentify(highest), '%')
print(lowestGuy, 'scored the lowest mark,', percentify(lowest), '%')
print()

average = percentify(totalScores / len(results))
print('The class average is:', average, '%')
