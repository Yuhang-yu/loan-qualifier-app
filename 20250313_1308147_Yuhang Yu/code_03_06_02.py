# Based on students score, we will give letter grade. Use the folowing WKU grading table
score = int(input("Enter the student's score: "))

if score > 93:
    grade = 'A'
elif score >= 90:
    grade = 'A-'
elif score >= 87:
    grade = 'B+'
elif score >= 84:
    grade = 'B'
elif score >= 80:
    grade = 'B-'
elif score >= 77:
    grade = 'C+'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"The letter grade for a score of {score} is: {grade}")