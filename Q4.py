
employees = {
    101: {"name": "Ram", "department": "IT", "salary": 30000},
    102: {"name": "Sita", "department": "HR", "salary": 35000},
    103: {"name": "Hari", "department": "Finance", "salary": 40000},
    104: {"name": "Gita", "department": "Marketing", "salary": 32000},
    105: {"name": "John", "department": "IT", "salary": 45000}
}

def find_employee(emp_id):
    if emp_id not in employees:
        raise KeyError("Employee ID does not exist.")
    return employees[emp_id]

def yearly_salary(salary):
    return salary * 12

def increase_salary(salary, percentage):
    return salary + (salary * percentage / 100)

try:
    emp_id = int(input("Enter employee ID: "))
    employee = find_employee(emp_id)

    print("Employee Name:", employee["name"])
    print("Department:", employee["department"])

    old_salary = employee["salary"]
    print("Old Monthly Salary:", old_salary)

    percentage = float(input("Enter salary increase percentage: "))

    if percentage < 0:
        raise ValueError("Percentage cannot be negative.")

    new_salary = increase_salary(old_salary, percentage)
    employee["salary"] = new_salary

    print("New Monthly Salary:", new_salary)
    print("Yearly Salary:", yearly_salary(new_salary))

except KeyError as e:
    print("Error:", e)

except ValueError as e:
    print("Invalid input:", e)