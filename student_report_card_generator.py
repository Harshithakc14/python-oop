class Student:
    def __init__(self,s_name,roll_no):
        self.s_name=s_name
        self.roll_no=roll_no
        self.__marks={}
    def add_marks(self,subject,marks):
        self.__marks[subject]=marks
    def calculate_average(self):
        if len(self.__marks)==0:
            return 0
        average=sum(self.__marks.values())/len(self.__marks)
        return average
    def has_passed(self,pass_marks=35):
        if len(self.__marks)==0:
            return False
        return all(mark>=pass_marks for mark in self.__marks.values())
    def get_marks(self):
        return self.__marks.copy()
class GradeCalculator:
    def calculate_grade(self,average):
        if average>=90:
            return "A"
        elif average>=75:
            return "B"
        elif average>=60:
            return "C"
        elif average>=40:
            return "D"
        else:
            return "F"
class ResultCalculator:
    def calculate_result(self,student):
        if student.has_passed():
            return "PASS"
        else:
            return "FAIL"

class ReportCardGenerator:
    def __init__(self, grade_calculator, result_calculator):
        self.grade_calculator = grade_calculator
        self.result_calculator = result_calculator

    def generate_report(self, student):
        marks = student.get_marks()
        average = student.calculate_average()
        grade = self.grade_calculator.calculate_grade(average)
        result = self.result_calculator.calculate_result(student)

        print("\n------- STUDENT REPORT CARD -------")
        print("Name:", student.s_name)
        print("Roll number:", student.roll_no)
        print("Marks:", marks)
        print("Average:", round(average, 2))
        print("Grade:", grade)
        print("Result:", result)


students={}
grade_calculator=GradeCalculator()
result_calculator=ResultCalculator()
report_generator=ReportCardGenerator(grade_calculator,result_calculator)
def menu():
    print("------------------STUDENT REPORT CARD MENU------------------")
    print("1. Add student")
    print("2. Add marks")
    print("3. view report card")
    print("4. Exit")
while True:
    menu()
    choice=int(input("enter your choice: "))
    if choice==1:
        name=input("Enter student name:  ")
        roll_no=int(input("Enter student roll number: "))
        students[roll_no]=Student(name,roll_no)
        print("Student added sucessfully!!!!!")
    elif choice==2:
        roll_number=int(input("Enter your roll number: "))
        if roll_number in students:
            sub=input("enter subject name: ")
            marks=float(input("Enter marks"))
            students[roll_number].add_marks(sub,marks)
            print("marks were added sucessfully!!")
        else:
            print("Student not found!")
    elif choice==3:
        roll_number=int(input("Enter Student roll number: "))
        if roll_number in students:
            report_generator.generate_report(students[roll_number])
    elif choice==4:
        print("Exiting student report card Generator, bye..")
        break
    else:
        print("invalid choice! please try again ")