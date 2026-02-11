import pandas as pd


# Read the student CSV file into a DataFrame
student_data = pd.read_csv("student.csv")


high_engagement_students = student_data[
    (student_data["studytime"] >= 3) &
    (student_data["internet"] == 1) &
    (student_data["absences"] <= 5)
]


# Save the filtered students to a new CSV file
high_engagement_students.to_csv("high_engagement.csv")


# Count how many students were selected
number_of_students = len(high_engagement_students)


# Calculate the average grade (if there are any students)
if number_of_students > 0:
    average_grade = high_engagement_students["grade"].mean()
else:
    average_grade = 0


print("Number of high engagement students:", number_of_students)
print("Average grade:", round(average_grade, 3))
