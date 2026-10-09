
students = [
    {"name": "Ram", "Math": 80, "English": 75, "Science": 90},
    {"name": "Sita", "Math": 85, "English": 90, "Science": 88},
    {"name": "Hari", "Math": 70, "English": 65, "Science": 75},
    {"name": "Gita", "Math": 95, "English": 92, "Science": 98},
    {"name": "John", "Math": 60, "English": 70, "Science": 65}
]

def calculate_total(student):
    return student["Math"] + student["English"] + student["Science"]

def calculate_percentage(total):
    return (total / 300) * 100

name = input("Enter student name: ")

try:
    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            found = True

            try:
                total = calculate_total(student)
                percentage = calculate_percentage(total)

                print("Student Name:", student["name"])
                print("Total Marks:", total)
                print("Percentage:", percentage, "%")

            except KeyError:
                print("Error: Subject marks are missing.")

            break

    if not found:
        raise ValueError("Student not found.")

except ValueError as e:
    print("Error:", e)