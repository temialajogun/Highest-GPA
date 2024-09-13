class EmptyRosterError(Exception):
    pass

class Student:
    def __init__(self, first_name, last_name, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa

    def get_first(self):
        return self.first_name
    def get_last(self):
        return self.last_name
    def get_gpa(self):
        return self.gpa
    
class Course:
    def __init__(self):
        self.roster = []
    def add_student(self, student):
        self.roster.append(student)
    def course_size(self):
        return len(self.roster)
    def highest_gpa(self):
        if not self.roster:
            raise EmptyRosterError("Exception: Course Roster is Empty.")
        return max(self.roster, key=lambda student: student.get_gpa())

def main():
    print("Welcome to CSC/DSCI 1301: Principles in CS/DS 1")
    print("Please Add Students to the Course: (quit or q to exit).")

    course = Course()
    course_size = 0
    while True:
        first_name = input('Enter First Name: ')
        if first_name.lower() == "quit" or first_name.lower() == "q":
            break
        last_name = input("Enter Last Name: ")
        try:
            gpa = float(input("Enter GPA: "))
        except ValueError:
            print("Error: Enter a Numeric GPA")
            continue

        student = Student(first_name, last_name, gpa)
        course.add_student(student)
        course_size += 1 
        
    if course_size > 0:
        top_student = course.highest_gpa()
        print(f"\nCourse Size: {course_size} students")
        print(f"Top Student: {top_student.get_first()} {top_student.get_last()} (GPA: {top_student.get_gpa()})")
    else:
        print("Course Size: 0 students")
        print("Excpetion: Course Roster is Empty.")

if __name__ == "__main__":
    main()