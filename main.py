# Name: Ivy Loi
# Date: 11/2/25
# Purpose of file: Implement class functions written in people.py file

from people import Faculty
from people import Student

faculty = []
students = []
choices = ["1", "2", "3", "4", "9"]
years = ["Freshman", "freshman", "Sophmore", "sophmore", "Junior", "junior", "Senior", "senior"]

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
        if not first.strip():
            print("First name can not be blank, returning to main menu...")
            continue
        last = input("Enter last name: ")
        if not last.strip():
            print("Last name cannot be blank, returning to main menu...")
            continue
        d = input("Enter department: ")
        if not d.strip():
            print("Department cannot be left blank... returning to main menu.")
            continue
        if not Faculty.valid_dep_len(d):
            print("Department input must be longer than one character, returning to main menu...")
            continue
        if not Faculty.valid_dep(d):
            print("Invalid department entered\nSpecial characters and numbers not excepted except for spaces and hyphens(-)\nReturning to main menu...")
            continue
        nfaculty = Faculty(first, last, d)
        faculty.append(nfaculty)
    elif prompt == "2":
            Faculty.printF(faculty)
    elif prompt == "3":
        if not faculty:
            print("You need to add at least one faculty member before adding a student.")
            continue
        sfirst = input("Enter first name: ")
        if not sfirst.strip():
            print("First name can not be blank, returning to main menu...")
            continue
        slast = input("Enter last name: ")
        if not slast.strip():
            print("Last name can not be blank, returning to main menu...")
            continue
        classy = input("Enter class year (Freshman, Sophmore, Junior, Senior): ")
        if classy not in years:
             print("You've entered an invalid class year, returning to main menu...")
             continue
        m = input("Enter major: ")
        if not m.strip():
            print("Major cannot be left blank... returning to main menu.")
            continue
        if not Student.valid_major_len(m):
            print("Major input must be longer than one character, returning to main menu...")
            continue
        if not Student.valid_major(m):
            print("Invalid major entered\nSpecial characters and numbers not excepted except for spaces and hyphens(-)\nReturning to main menu...")
            continue
        fa = input("Enter faculty advisor (Index number of advisor from faculty advisor list): ")
        try:
            fa = int(fa)
            advisor = faculty[fa]
        except (ValueError, IndexError):
            print("Invalid advisor record number, returning to main menu...")
            continue
        if not Student.advisor_match(m, advisor):
            print(f"Advisor department '{advisor.department}' does not match student major '{m}'. Returning to main menu...")
            continue
        nstudent = Student(sfirst, slast)
        nstudent.set_class(classy)
        nstudent.set_major(m)
        nstudent.set_advisor(advisor)
        students.append(nstudent)
    elif prompt == "4":
        Student.printS(students)
    elif prompt == "9":
        break
    if prompt not in choices:
        print("You've entered an invalid option, try again")
        continue
    