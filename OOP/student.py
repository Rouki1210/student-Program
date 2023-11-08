class Student:
    def __init__(self, id, name, grade):
        self.__id = id
        self.__name = name
        self.__grade = grade
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def grade(self):
        return self.__grade
    
    @name .setter
    def name(self, name):
        self.__name = name
        
    @grade .setter
    def grade(self, grade):
        self.__grade = grade
        
    def show_info(self):
        print('Id: {}  Name: {}  Age: {}'.format(self.__id, self.__name, self.__age))
    