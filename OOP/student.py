class Student:
    def __init__(self, id, name, age):
        self.__id = id
        self.__name = name
        self.__age = age
    
    @property
    def get_id(self):
        return self.__id
    
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
        
    def set_age(self, age):
        self.__age = age
        
    def show_info(self):
        print('Id: {}  Name: {}  Age: {}'.format(self.__id, self.__name, self.__age))
    
class School:
    def __init__(self, name):
        self.__name = name
        self.__students = []
    
    @property    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        
    def add_student(self, student):
        self.__students.append(student)

    def find_student_by_id(self, id):
        for student in self.__students:
            if student == id:
                return student
            return None

    def update_info_student(self, id, name, age):
        student = self.find_student_by_id(id)
        if student is None:
            print ('Not found')
            return
        self.__students.set_name(name)
        self.__students.set_age(age)
        print (f'Student {name} has been updated with new info')
        return
        
    def ls_student(self):
        for student in self.__students:
            student.show_info()
    
    
student1 = Student(1, "Alice", 20)
student2 = Student(2, "Bob", 22)

school = School('Greenwich university')
school.add_student(student1)
school.add_student(student2)


school.update_info_student(1, "Alicia", 25)
school.ls_student()
