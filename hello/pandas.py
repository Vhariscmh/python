import pandas as pd

# Create two sample DataFrames
data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
data2 = {'A': [7, 8, 9], 'B': [10, 11, 12]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Concatenate the DataFrames along the rows (axis=0)
result = pd.concat([df1, df2], ignore_index=True)

# Display the result
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
print("\nConcatenated DataFrame:")
print(result)
