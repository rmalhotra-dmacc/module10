"""
Author: Rajiv Malhotra
Program: student.py
Date: 10/31/2020

Student Class definition
"""




class Student:
    """Student class"""
    MAJORS = ('Political Science', 'CompSci', 'English', 'Literature')

    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")

        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError

        if major not in self.MAJORS:
            raise ValueError

        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


if __name__ == '__main__':
        student = Student('Duck', 'Daisy', 'English', 4.0)
        print(str(student))
