

def find_grades(d,final_cutoffs):
    grades = {}
    for rollno in d:
        mark = d[rollno]
        g = ""
        if mark >= final_cutoffs[0]:
            g = "A"

        elif mark >= final_cutoffs[1]:
            g = "B"

        elif mark >= final_cutoffs[2]:
            g = "C"
        
        else:
            g = 'F'

        grades[rollno] = g
    return grades

students_marks = {}
student_mark_weightage = {}
policy = [80, 65, 50, 40]
cname = "IP"
f = open("students_marks.txt","r")
entries = f.read().splitlines()
final_cutoffs=[i for i in policy]
for e in entries:
    val = e.split(",")
    marks = list(map(int,val[1:]))
    students_marks[int(val[0])] = sum(marks)
    student_mark_weightage[int(val[0])] = marks

marks_ = [[] for i in policy]
for m in students_marks.values():
    if policy[0]-2 <=m<= policy[0]+2:
        marks_[0].append(m)
    elif policy[1]-2 <=m<= policy[1]+2:
        marks_[1].append(m)
    elif policy[2]-2 <=m<= policy[2]+2:
        marks_[2].append(m)
    elif policy[3]-2 <=m<= policy[3]+2:
        marks_[3].append(m)

for j in range(len(marks_)):
    l = marks_[j]
    l.sort()
    a = 0
    diff = 0
    b = 0
    for i in range(1,len(l)-1):
        d = l[i] - l[i-1]
        if d > diff:
            diff = d
            a = l[i-1]
            b = l[i]
    final_cutoffs[j] = (policy[j] + (a+b/2))

student_grades = find_grades(students_marks,final_cutoffs)

while True:
    c = int(input("Enter choice: "))
    if c == 1:

        print(f"""

            
    Course name: {cname}

    Initial cutoffs: 
        {policy}

    Final Cutoffs: 
        {final_cutoffs}

    Student Grades: 
        {student_grades}
    """)

    #2
    elif c == 2:
        f1 = open("students_grades_5.txt","w")
        for i in student_grades:
            s = f"{i} has grade {student_grades[i]} mark {students_marks[i]}\n"
            f1.write(s)

    elif c == 3:
        rollno = int(input("Enter roll no: "))

        if rollno in student_grades:
            s = f"{i} has grade {student_grades[i]} mark {students_marks[i]} weightage {student_mark_weightage[i]}\n"
            print(s)

        else:
            print("No such record exists! ")

    elif c == 4:
        
        f1.close()
        f.close()
        break



