class Student:
    def __init__(self, id, name, age):
        self.__id = id
        self.__name = name
        self.__age = age
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @name .setter
    def name(self, name):
        self.__name = name
        
    @age .setter
    def age(self, age):
        self.__age = age
        
    def show_info(self):
        print('Id: {}  Name: {}  Age: {}'.format(self.__id, self.__name, self.__age))
    