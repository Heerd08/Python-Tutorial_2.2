class Employee:
    def __init__(self, emp_id, name, base_salary):
        print("Employee Object Created!")
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Base Salary:", self.base_salary)

    def annual_salary(self):
        return self.base_salary * 12


class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, department, bonus):
        Employee.__init__(self, emp_id, name, base_salary)
        self.department = department
        self.bonus = bonus

    def total_salary(self):
        total = self.annual_salary() + self.bonus
        return total

    def display_manager(self):
        self.display_employee()
        print("Department:", self.department)
        print("Bonus:", self.bonus)
        print("Total Annual Salary:", self.total_salary())
        print()


# Creating Manager Objects
m1 = Manager(101, "Rahul", 50000, "Sales", 100000)
m2 = Manager(102, "Priya", 60000, "IT", 120000)
m3 = Manager(103, "Amit", 55000, "HR", 90000)

# Storing objects in list
managers = [m1, m2, m3]

# Display all managers
for m in managers:
    m.display_manager()