import pandas as pd


crime_data = pd.read_csv("crime.csv")


# Function to determine crime risk level
def get_risk_level(violent_crime_rate):

    # High crime if rate is 0.50 or higher
    if violent_crime_rate >= 0.50:
        return "HighCrime"

    # Otherwise low crime
    else:
        return "LowCrime"


# Create a new column called "risk"
crime_data["risk"] = crime_data["ViolentCrimesPerPop"].apply(get_risk_level)


# Group by risk and calculate average unemployment
average_unemployment = crime_data.groupby("risk")["PctUnemployed"].mean()

print("Average unemployment rate by crime risk:")

for risk_level in average_unemployment.index:
    average_rate = average_unemployment[risk_level]
    print(risk_level + ":", round(average_rate, 4))
