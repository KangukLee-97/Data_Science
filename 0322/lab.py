# Lab3
import pandas as pd
import numpy as np

# Create a Pandas (4,4) DataFrame from the following numpy array
df = pd.DataFrame({'column_a': [3., '?', 2., 5.],
                   'column_b': ['*', 4., 5., 6.],
                   'column_c': ['+', 3., 2., '&'],
                   'column_d': [5., '?', 7., '!']})

# Display the DataFrame
print(df)
print("------------------------------------------------")

# Replace any non-numeric value with NaN and Display the DataFrame
df.replace({"?": np.nan, "*": np.nan, "+": np.nan, "&": np.nan, "!": np.nan}, inplace=True)
print(df)
print("------------------------------------------------")
# isna with any and sum
# print("<isna with any>")
# print(df.isna().any())
# print("<isna with sum>")
# print(df.isna().sum(), end="\n")

# dropna with how any, how all, thresh 1, thresh 2
# df.dropna(axis=0, how="any", inplace=True)
# print("<dropna with how any>")
# print(df)

# df.dropna(axis=0, how="all", inplace=True)
# print("<dropna with how all>")
# print(df)

# df.dropna(axis=0, thresh=1, inplace=True)
# print("<dropna with thresh 1>")
# print(df)

# df.dropna(axis=0, thresh=2, inplace=True)
# print("<dropna with thresh 2>")
# print(df)

# fillna with 100, mean, median
# df.fillna(100, inplace=True)
# print("<fillna with 100>")
# print(df)
# print("------------------------------------------------")

# mean
# df = df.apply(pd.to_numeric)
# mean_a = df['column_a'].mean()
# mean_b = df['column_b'].mean()
# mean_c = df['column_c'].mean()
# mean_d = df['column_d'].mean()
# df['column_a'].fillna(mean_a, inplace=True)
# df['column_b'].fillna(mean_b, inplace=True)
# df['column_c'].fillna(mean_c, inplace=True)
# df['column_d'].fillna(mean_d, inplace=True)
# print("<Mean>")
# print(df)

# median
# df = df.apply(pd.to_numeric)
# median_a = df['column_a'].median()
# median_b = df['column_b'].median()
# median_c = df['column_c'].median()
# median_d = df['column_d'].median()
# df['column_a'].fillna(median_a, inplace=True)
# df['column_b'].fillna(median_b, inplace=True)
# df['column_c'].fillna(median_c, inplace=True)
# df['column_d'].fillna(median_d, inplace=True)
# print("<Median>")
# print(df)

# ffill, bfill
# df.fillna(axis=0, method="ffill", inplace=True)
# print("<ffill>")
# print(df)

# df.fillna(axis=0, method="bfill", inplace=True)
# print("<bfill>")
# print(df)