# Question4
import numpy as np
import pandas as pd

# Check the number of students whose z-scores are <= -1.0
def checkStudents(z):
    count = 0
    for i in z['scores']:
        if i <= -1.0:
            count += 1
    return count

# a. Represent the scores as a pandas DataFrame with a column 'scores'
df = pd.DataFrame({'scores': [28,35,26,32,28,28,35,34,46,42,37]})
print("<Pandas DataFrame>")
print(df)

# b. Print the mean and the standard deviation of the scores
mean_df = df['scores'].mean()
print("Mean: {0}".format(mean_df))
std_df = df['scores'].std()
print("Standard deviation: {0}".format(std_df))

# c. Print the z-scores and the number of students whose z-scores are <= -1.0
# z-score : (X - mean) / standard deviation
z = (df - mean_df) / std_df
print("<Z-Scores>")
print(z)

print("The number of students whose z-scores are <= -1.0 : {0}".format(checkStudents(z)))