import pandas as pd
student_data = pd.read_csv("student.csv")


# Function to assign a grade band based on grade
def get_grade_band(grade):

    if grade <= 9:
        return "Low"

    elif grade <= 14:
        return "Medium"

    else:
        return "High"


# Create the grade_band column
student_data["grade_band"] = student_data["grade"].apply(get_grade_band)


# Group students by grade band and calculate statistics
grade_summary = student_data.groupby("grade_band").agg(

    # Count number of students
    number_of_students=("grade_band", "count"),

    # Average number of absences
    average_absences=("absences", "mean"),

    # Average study time
    average_studytime=("studytime", "mean")
)


print("Grade Band Summary:")
print(grade_summary)


# Save the updated dataset
student_data.to_csv("student_bands.csv")

print("Saved file: student_bands.csv")
