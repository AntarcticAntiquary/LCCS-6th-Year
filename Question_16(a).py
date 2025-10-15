# Question 16(a)
# Student name: Daniel Lewis

def username():
    name = input('Please enter your username: ')
    return name

def get_grade(percentage):
    if percentage >= 80:
        return 'A'
    elif percentage >= 60:
        return 'B'
    else:
        return 'C'

username = username()
print(f'Welcome, {username}, to the student result calculator') # part(iv)

print()
student_name = input("Please enter the students name: ")
#student_score = int(input("Please enter the students mark: "))
student_score = float(input("Please enter the students mark: ")) # part (i)
exam_total = int(input('Please enter the total amount of marks going for the exam: ')) # part (ii)
score_as_a_percentage=round((student_score/exam_total)*100, 1) # part (iii)
grade = get_grade(score_as_a_percentage)

print(student_name,"scored",score_as_a_percentage,"%. They got a " + grade + '.')
