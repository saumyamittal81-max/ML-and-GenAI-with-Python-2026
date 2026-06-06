# Student Result System

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

subjects = int(input("Enter number of subjects: "))

total = 0
for i in range(1, subjects + 1):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total += marks

percentage = total / subjects
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
print("\n STUDENT RESULT ")
print("Name       :", name)
print("Roll No    :", roll_no)
print("Total Marks:", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)