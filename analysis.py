import pandas as pd

data = pd.read_csv("patient.csv")

average_age = data["Age"].mean()
average_heart_rate = data["Heart_Rate"].mean()
average_length_of_stay = data["Length_of_Stay"].mean()

high_heart_rate_patients = data[data["Heart_Rate"] > 100]

print("Patient Vitals Analysis")
print("-----------------------")

print("Average patient age:", average_age)
print("Average heart rate:", average_heart_rate)
print("Average length of stay:", average_length_of_stay)

print("\nPatients with heart rate above 100:")
print(high_heart_rate_patients)
