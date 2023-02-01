transcript = []

def course_title_checker(title): #Checks if the input course title is valid
    sub1 = ""
    sub2 = ""
    status = True
    for i in range(len(title)):

        if status:
            sub1+=title[i]
        else:
            sub2+=title[i]

        if i != len(title)-1:
            if title[i+1] in "123456789":
                status = False
    if sub1.isupper() and sub2.isnumeric():
        return True

    return False

def grade_checker(grade): #Checks if input grade is valid
    if grade.upper() in ["A+","A","A-","B","B-","C","C-","D",'F']:
        return True

    return False

def credit_checker(credit): #Checks if input credit is valid
    if credit in [1,2,4]:
        return True

    return False

def grade_num(grade): #Returns grade value
    if grade == "A+":
        return 10

    elif grade == "A":
        return 10

    elif grade == "A-":
        return 9

    elif grade == "B":
        return 8

    elif grade == "B-":
        return 7

    elif grade == "C":
        return 6

    elif grade == "C-":
        return 5

    elif grade == "D":
        return 4

    elif grade == "F":
        return 2
def checker(title,credit,grade):# Checks all the conditions and return boolean
    return course_title_checker(title) and grade_checker(grade) and credit_checker(credit)

def message(title,credit,grade):#Prints appropriate message
    if not course_title_checker(title):
        print("Improper course no")

    elif not credit_checker(credit):
        print("Improper credit")

    elif not grade_checker(grade):
        print("Improper grade")

def sgpa_calculator(transcript): #Returns sgpa after calculation
    total_credit = 0
    for i in transcript:
        total_credit += i[1]

    ans  = 0

    for i in transcript:
        ans += ((i[1] * i[3]) / total_credit)

    return ans

while True: 
    user_input = input()
    if user_input == "":
        break
    
    user_input_list = user_input.split()
    course_title = user_input_list[0]
    course_credit = int(user_input_list[1])
    course_grade = user_input_list[2]

    status = checker(course_title,course_credit,course_grade)
    if status:
        transcript.append([course_title,course_credit,course_grade,grade_num(course_grade)])

    else:
        message(course_title,course_credit,course_grade)

        
transcript.sort()
print("TRANSCRIPT: ")
for i in transcript:
    print(f"{i[0]}: {i[2]}")

print(f"SGPA: {sgpa_calculator(transcript):.2f}")
