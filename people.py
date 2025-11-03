# Name: Ivy Loi
# Date: 11/2/25
# Purpose of file: Create classes and functions to be used in main.py file

import re # To be used for valid_major and valid_dep function (error check function)

class Person:

    def __init__(self, first_name, last_name):
        '''Setting member variables firstname and lastname'''
        self.firstname = first_name
        self.lastname = last_name

class Faculty(Person):

    def __init__(self, first_name, last_name, department):
        '''Calls Person __init__ function and sets member variable department'''
        super().__init__(first_name, last_name)
        self.department = department

    def valid_dep(department):
        '''Makes sure department name doesn't contain special characters'''
        # fullmatch makes sure if input matches the accepted letters and symbols
        # it accepts capital (A-Z) and lowercase (a-z) letters including space and hyphen
        # returns True when accepted letters and symbols matches, false otherwise
        # This is the same for valid_major
        return re.fullmatch(r"[A-Za-z -]+", department) is not None
    
    def valid_dep_len(department):
        '''Makes sure department name isn't only one character long'''
        return len(department.strip()) > 1
    
    def printF(faculty_list):
        '''Prints faculty list'''
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
        '''Calls Person __init__ function'''
        super().__init__(first_name, last_name)
    
    def set_class(self, class_year):
        '''Sets member variable classyear'''
        self.classyear = class_year

    def set_major(self, major):
        '''Sets member variable major'''
        self.major = major
    
    def set_advisor(self, advisor):
        ''' Sets member variable advisor if exists in faculty list'''
        self.advisor = advisor
        
    def valid_major(major):
        '''Makes sure major name does not contain special characters'''
        return re.fullmatch(r"[A-Za-z -]+", major) is not None
    
    def valid_major_len(major):
        '''Makes sure major name is longer than one character'''
        return len(major.strip()) > 1
    
    def advisor_match(major, advisor):
        '''Makes sure major matches advisor department'''
        return major.strip().lower() == advisor.department.strip().lower()

    def printS(student_list):
        '''Prints student list'''
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
                advisor = f"{s.advisor.firstname} {s.advisor.lastname}"
                print(f"{name:<21} {classyear:<10} {major:<27} {advisor}")