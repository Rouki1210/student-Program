class Employee:
    def __init__(self, name, id: int, salary: float):
        self.__name = name
        self.__id = id
        self.__salary = salary
    
    @property
    def get_id(self):
        return self.__id
    
    @property
    def get_name(self):
        return self.__name
    
    
    def set_name(self, name):
        self.__name = name
    
    def set_salary(self, salary):
        self.__salary = salary
    
    def increase_salary(self, salary):
        self.__salary += salary
    
    def show_info(self):
        print("Name : {}".format(self.__name))
        print("ID   : {}".format(self.__id))
        print("Salary: {}".format(self.__salary))

        

class Company:
    def __init__(self, name):
        self.__name = name
        self.__employees = []
        
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        
    def add_employee(self, employee):
        self.__employees.append(employee)
        
    def __find_by_id(self, id):
        for e in self.__employees:
            if e == id:
                return e
            return None
    
    def del_employee(self, id):
        employee = self.__find_by_id(id)
        if employee is None:
            print("Employee not found")
            return
        self.__employees.remove(employee)
        print('Delete employee {employee.name} successfully')
        
    def list_employee(self):
        for employee in self.__employees:
            employee.show_info()
        
    def increase_salary(self, id, salary):
        employee = self.__find_by_id(id)
        if employee is None:
            print("Employee not found")
            return
        employee.increase_salary(salary)
        print('Increase salary of employee {employee.name} successfully')
            

employee_A = Employee('John', 1, 200323)
employee_B = Employee('Marry', 2, 232344)
company_A = Company('ABC Company')

company_A.add_employee(employee_A)
company_A.add_employee(employee_B)

company_A.list_employee()

company_A.increase_salary(1, 5000)

company_A.list_employee()

company_A.del_employee(1)

company_A.list_employee()