class Employee:
    def __init__(self, emp_id, name, position, salary):
        if not isinstance(emp_id, int):
            raise ValueError("emp_id must be an integer")
        if not isinstance(name, str):
            raise ValueError("name must be a string")
        if not isinstance(position, str):
            raise ValueError("position must be a string")
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("salary must be a positive number")
        
        self._emp_id = emp_id
        self._name = name
        self._position = position
        self._salary = salary


    def emp_id(self):
        return self._emp_id


    def name(self):
        return self._name

  
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        self._name = value


    def position(self):
        return self._position


    def position(self, value):
        if not isinstance(value, str):
            raise ValueError("position must be a string")
        self._position = value

  
    def salary(self):
        return self._salary

   
    def salary(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("salary must be a positive number")
        self._salary = value

# Las pruebas unitarias y ejemplos de uso estarán en la función main.
