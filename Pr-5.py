class Employee:
    def __init__(self, name=None, age=None, employee_id=None, salary=None):
        self.name = name
        self.age = age
        
        self.__employee_id = employee_id
        self.__salary = float(salary) if salary is not None else None
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id
        
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = float(salary)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        if self.__employee_id is not None:
            print(f"Employee ID: {self.__employee_id}")
        if self.__salary is not None:
            print(f"Salary: ${self.__salary}")

    def __del__(self):
        pass


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")


class Developer(Employee):
    """
    Derived Class inheriting from Employee.
    """
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")


def main():
    if issubclass(Manager, Employee) and issubclass(Developer, Employee):
        pass 

    records = {
        "person": None,
        "employee": None,
        "manager": None
    }

    print("--- Python OOP Project: Employee Management System ---")

    while True:
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            
            records["person"] = Employee(name=name, age=age)
            print(f"\nPerson created with name: {name} and age: {age}.")
            print("\n--- Choose another operation ---")

        elif choice == 2:
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            
            records["employee"] = Employee(name, age, emp_id, salary)
            print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}.")
            print("\n--- Choose another operation ---")

        elif choice == 3:
            name = input("\nEnter Name: ")
            age = int(input("Enter Age: "))
            emp_id = input("Enter Employee ID: ")
            salary = float(input("Enter Salary: "))
            dept = input("Enter Department: ")
            
            records["manager"] = Manager(name, age, emp_id, salary, dept)
            print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {dept}.")
            print("\n--- Choose another operation ---")

        elif choice == 4:
            print("\nChoose details to show:")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            
            try:
                sub_choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input.")
                continue

            if sub_choice == 1:
                if records["person"]:
                    print("\nPerson Details:")
                    records["person"].display()
                else:
                    print("\nNo Person created yet.")
            elif sub_choice == 2:
                if records["employee"]:
                    print("\nEmployee Details:")
                    records["employee"].display()
                else:
                    print("\nNo Employee created yet.")
            elif sub_choice == 3:
                if records["manager"]:
                    print("\nManager Details:")
                    records["manager"].display()
                else:
                    print("\nNo Manager created yet.")
            else:
                print("Invalid choice.")
                
            print("\n--- Choose another operation ---")

        elif choice == 5:
            print("\nExiting the system. All resources have been freed.")
            print("\nGoodbye!")
            del records
            break
            
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()