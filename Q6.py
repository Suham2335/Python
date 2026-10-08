student = {
    "name": "Ram",
    "age": 19,
    "course": "BCA",
    "marks": 78
}

print("Student information:")
print(student)

student["marks"] = student["marks"] + 5

if student["marks"] >= 40:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"

print("Updated dictionary:")
print(student)