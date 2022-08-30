'''
    Module File for sample class with:
        Variables:
            1. Class Variable
            2. Instance Variable
        Methods:
            1. Class Method
            2. Instance Method
            3. Static Method
'''


class Employee:
    '''
        An Employee class
            Class Variables (shared accross all instances)
                empcount
            Instance Variables
                name
                salary
    '''
    empcount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empcount += 1

    def display_employee(self):
        '''
            Instance Method to display Employee
        '''
        print('Name :', self.name, '| Salary :', self.salary)

    @classmethod
    def display_employee_count(cls):
        '''
            Class Method to display Employee count
        '''
        print('Employee Count :', cls.empcount)

    @staticmethod
    def employee_json(employee):
        '''
            Static Method to return Employee details as Dictionary
        '''
        return {"name": employee.name, "salary": employee.salary}

if __name__ == '__main__':
    # Documentation String of the class (if defined) else None
    print('Doc :', Employee.__doc__)
    # Name of the class
    print('Name :', Employee.__name__)
    # Module name in which class is defined
    #   '__main__' in interactive mode
    print('module :', Employee.__module__)
    # Tuple containing the base classes
    # In the order of their occurrence in the base class list
    print('Bases :', Employee.__bases__)
    # Dictionary containing the class NameSpace
    print('Dict :', Employee.__dict__)

    # First Instance of class Employee
    employee1 = Employee('John', 30000)
    employee1.display_employee()
    employee1.display_employee_count()
    print(employee1.employee_json(employee1))

    # Second Instance of class Employee
    employee2 = Employee('Advin', 30000)
    employee2.display_employee()
    employee2.display_employee_count()
    print(employee2.employee_json(employee2))

    ### Magic Methods of class ###
    Employee.__setattr__(employee1, 'age', 30)
    ## employee2.__setattr__('age', 32)
    #   Unnecessarily calls dunder method __setattr__.
    #   Set attribute directly or use setattr built-in function.
    employee2.__setattr__('age', 32)

    print(Employee.__getattribute__(employee1, 'age'))
    ## employee2.__getattribute__('name')
    #   Unnecessarily calls dunder method __getattribute__.
    #   Access attribute directly or use getattr built-in function.
    print(employee2.__getattribute__('age'))

    Employee.__delattr__(employee1, 'age')
    try:
        print(Employee.__getattribute__(employee1, 'age'))
    except AttributeError as error:
        print(error)

    ## employee2.__delattr__('age')
    #   Unnecessarily calls dunder method __delattr__.
    #   Use del keyword
    employee2.__delattr__('age')
    try:
        print(employee2.age)
    except AttributeError as error:
        print(error)

    ### Built-in methods to access class attributes ###
    setattr(employee1, 'age', 30)
    print(getattr(employee1, 'age'))
    delattr(employee1, 'age')
    print(hasattr(employee1, 'age'))
    print(hasattr(employee1, 'name'))
