# Task 1: Create a Dictionary of Student Marks

Student_Marks = {
    "Ayush" : 80,
    "Alice" : 85,
    "Piyush" : 90,
    "Vikas" : 95,
    "Neha" : 100 
}

name = input("Enter the student's name : ")

if name in Student_Marks:
    print(f"{name}'s marks : {Student_Marks[name]}")
else:
    print("student not found")