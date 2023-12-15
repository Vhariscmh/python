import pandas as pd

# Replace 'studentid.csv' with the actual path or URL of your CSV file
file_path = 'studentid.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Print the first five lines
print("First five lines:")
print(df.head())

# Print the last five lines
print("\nLast five lines:")
print(df.tail())
