class Student:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def get_info(self):
        print(self.name, self.last_name)

class School:
    def __init__(self, school_name, school_address):
        self.school_name = school_name
        self.school_address = school_address
        self.students= []

    def add_student(self, obj_student):
        self.students.append(obj_student)

    def remove_student(self, student_index):
        self.students.pop(student_index)

    def show_students(self):
        for stu in self.students:
            stu.get_info()

obj_school = School('126-ე საჯარო','ვაჟა-ფშაველას გამზირი 71')

obj_student1 = Student('სანი','ბოდლერი','1')
obj_student2 = Student('კლაუს','ბოდლერი','12')
obj_student3 = Student('ვიოლეტ','ბოდლერი','14')
obj_school.add_student(obj_student1)
obj_school.add_student(obj_student2)
obj_school.add_student(obj_student3)

obj_school.show_students()