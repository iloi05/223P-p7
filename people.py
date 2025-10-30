class Person:

    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

class Faculty(Person):

    def __init__(self, first_name, last_name, department):
        super().__init__(first_name, last_name)
        self.department = department
    
    def printF(faculty_list):
        if not faculty_list:
            print("The list is currently empty, add some names in first")
            return "error"
        else:
            print("======================= FACULTY =======================")
            print("Record  Name                  Department")
            print("======  ====================  =========================")
            for i, f in enumerate(faculty_list):
                name = f"{f.firstname} {f.lastname}"
                print(f"{i:<7} {name:<21} {f.department}")

class Student(Person):
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
    
    def set_class(self, class_year):
        self.classyear = class_year

    def set_major(self, major):
        self.major = major
    
    def set_advisor(self, advisor):
        self.advisor = advisor

    def printS(student_list):
        if not student_list:
            print("The list is currently empty, add some names first")
            return "error"
        else:
            print("===================================== STUDENTS ======================================")
            print("Name                  Class      Major                       Advisor")
            print("====================  =========  ==========================  ========================")
            for s in student_list:
                name = f"{s.firstname} {s.lastname}"
                classyear = getattr(s, "classyear", "")
                major = getattr(s, "major", "")
                advisor = f"{s.advisor.firstname} {s.advisor.lastname}" if hasattr(s, "advisor") else ""
                print(f"{name:<22}, {classyear:<10} {major:<25} {advisor}")