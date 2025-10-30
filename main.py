from people import Faculty
from people import Student

faculty = []
students = []
choices = ["1", "2", "3", "4", "9"]

while True:
    print()
    print("     *** TUFFY TITAN STUDENT/FACULTY MAIN MENU")
    print()
    print("1. Add faculty")
    print("2. Print faculty")
    print("3. Add student")
    print("4. Print student")
    print("9. Exit the program")
    print()

    prompt = input("Enter menu choice: ")
    if prompt == "1":
        first = input("Enter first name: ")
        last = input("Enter last name: ")
        d = input("Enter department: ")
        nfaculty = Faculty(first, last, d)
        faculty.append(nfaculty)
    elif prompt == "2":
            Faculty.printF(faculty)
    elif prompt == "3":
        sfirst = input("Enter first name: ")
        slast = input("Enter last name: ")
        classy = input("Enter class year: ")
        m = input("Enter major: ")
        fa = input("Enter faculty advisor: ")
        nstudent = Student(sfirst, slast)
        nstudent.set_class(classy)
        nstudent.set_major(m)
        nstudent.set_advisor(fa)
        students.append(nstudent)
    elif prompt == "4":
            Student.printS(students)
    elif prompt == "9":
        break
    if prompt not in choices:
        print("You've entered an invalid option, try again")
        continue
    