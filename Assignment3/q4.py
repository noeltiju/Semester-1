class Course():
    def __init__(self,name,credits,policy,weights):
        self.name = name
        self.credits = credits
        self.policy = policy
        self.weights = weights
        self.final_cutoffs = policy
        self.students = []
        self.marks = []
        self.grades=[]
        self.stu_grades = {}

    def final_cutoff(self):
        marks_ = [[] for i in self.policy]
        for m in self.marks:
            if self.policy[0]-2 <=m<= self.policy[0]+2:
                marks_[0].append(m)
            elif self.policy[1]-2 <=m<= self.policy[1]+2:
                marks_[1].append(m)
            elif self.policy[2]-2 <=m<= self.policy[2]+2:
                marks_[2].append(m)
            elif self.policy[3]-2 <=m<= self.policy[3]+2:
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
            self.final_cutoffs[j] = (self.policy[j] + (a+b/2))

    def find_marks(self):
        for stu in self.students:
            marks = stu.get_marks()
            sum_ = sum(marks)
            self.marks.append(sum_)

    def find_grades(self):

        for mark in self.marks:
            if mark >= self.final_cutoffs[0]:
                self.grades.append('A')

            elif mark >= self.final_cutoffs[1]:
                self.grades.append('B')

            elif mark >= self.final_cutoffs[2]:
                self.grades.append('C')
            
            else:
                self.grades.append("F")

    def add_student(self,s):
        self.students.append(s)

    def get_marks(self):
        return self.marks

    def get_cutoffs(self):
        return self.final_cutoffs
        
    def get_grades(self):
        return self.grades

    def find_student_grades(self):
        for i in range(len(self.students)):
            stu = self.students[i]
            self.stu_grades[stu.get_rollno()] = self.grades[i]

    def summary(self):
        return self.stu_grades

class Student():
    def __init__(self,marks,rollno):
        self.marks = marks
        self.rollno = rollno

    def get_marks(self):
        return self.marks

    def get_rollno(self):
        return self.rollno
    
if __name__ == "__main__":
    f = open("students_marks.txt","r")
    f1 = open("students_grades.txt","w")
    students = f.read().splitlines()
    course = Course("IP",4,[80, 65, 50, 40], [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)])
    for line in students:
        line = line.split(",")
        rollno = int(line[0])
        marks = list(map(int,line[1:]))
        st = Student(marks,rollno)

        course.add_student(st)
    
    course.find_marks()
    course.final_cutoff()
    course.find_grades()
    course.find_student_grades()

    d = course.summary()

    for i in d:
        s = f"{i} has grade {d[i]}\n"
        f1.write(s)