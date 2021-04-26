# Lab3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.preprocessing as preprocessing
from sklearn.linear_model import LinearRegression
import math
# pd.set_option('display.max_rows', None)

def standard_scaling(dataframe):   # StandScaling function
    standard_scaler = preprocessing.StandardScaler()
    standard_scaled_df = standard_scaler.fit_transform(dataframe)
    standard_scaled_df = pd.DataFrame(standard_scaled_df, columns=['Age', 'Height (Inches)', 'Weight (Pounds)', 'BMI'])
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6, 5))
    ax1.set(title="Before Scaling (StandardScaler)", xlabel="Height, Weight")
    sns.kdeplot(dataframe['Height (Inches)'], label="Height (Inches)", ax=ax1)
    sns.kdeplot(dataframe['Weight (Pounds)'], label="Weight (Pounds)", ax=ax1)
    ax2.set(title="After Scaling (StandardScaler)", xlabel="Height, Weight")
    sns.kdeplot(standard_scaled_df['Height (Inches)'], label="Height (Inches)", ax=ax2)
    sns.kdeplot(standard_scaled_df['Weight (Pounds)'], label="Weight (Pounds)", ax=ax2)
    ax1.legend()
    ax2.legend()
    plt.show()


def minmax_scaling(dataframe):   # MinMaxScaling function
    minmax_scaler = preprocessing.MinMaxScaler()
    minmax_scaled_df = minmax_scaler.fit_transform(dataframe)
    minmax_scaled_df = pd.DataFrame(minmax_scaled_df, columns=['Age', 'Height (Inches)', 'Weight (Pounds)', 'BMI'])
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6, 5))
    ax1.set(title="Before Scaling (MinMaxScaler)", xlabel="Height, Weight")
    sns.kdeplot(dataframe['Height (Inches)'], label="Height (Inches)", ax=ax1)
    sns.kdeplot(dataframe['Weight (Pounds)'], label="Weight (Pounds)", ax=ax1)
    ax2.set(title="After Scaling (MinMaxScaler)", xlabel="Height, Weight")
    sns.kdeplot(minmax_scaled_df['Height (Inches)'], label="Height (Inches)", ax=ax2)
    sns.kdeplot(minmax_scaled_df['Weight (Pounds)'], label="Weight (Pounds)", ax=ax2)
    ax1.legend()
    ax2.legend()
    plt.show()


def robust_scaling(dataframe):   # RobustScaling function
    robust_scaler = preprocessing.RobustScaler()
    robust_scaled_df = robust_scaler.fit_transform(dataframe)
    robust_scaled_df = pd.DataFrame(robust_scaled_df, columns=['Age', 'Height (Inches)', 'Weight (Pounds)', 'BMI'])
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6, 5))
    ax1.set(title="Before Scaling (RobustScaler)", xlabel="Height, Weight")
    sns.kdeplot(dataframe['Height (Inches)'], label="Height (Inches)", ax=ax1)
    sns.kdeplot(dataframe['Weight (Pounds)'], label="Weight (Pounds)", ax=ax1)
    ax2.set(title="After Scaling (RobustScaler)", xlabel="Height, Weight")
    sns.kdeplot(robust_scaled_df['Height (Inches)'], label="Height (Inches)", ax=ax2)
    sns.kdeplot(robust_scaled_df['Weight (Pounds)'], label="Weight (Pounds)", ax=ax2)
    ax1.legend()
    ax2.legend()
    plt.show()


def replace_weight(coef, hei, intercept):   # Replace dirty values of Weight
    wei = coef * hei + intercept
    return wei


def replace_height(coef, wei, intercept):   # Replace dirty values of Height
    hei = (wei - intercept) / coef
    return hei


# --------------------------- Read the CSV dataset file ---------------------------
df = pd.read_csv("bmi_data_lab3.csv")

# --------------------------- Peek into the dataset (data exploration) ---------------------------
# <Print dataset statistical data, feature names & data types>
print("**** Statistical data ****")
print(df.describe(), end="\n")
print("**** Feature names & Data types ****")
print(df.info(), end="\n")

# <Plot height & weight histograms for each BMI value>
fig,

# <Plot scaling results for height and weight>
# scale_temp_df = df.dropna(axis=0)   # Drop the NaN values for test scaling.
scale_test_df = df.drop(columns="Sex")  # Make the temporary data frame dropped the Sex columns (not numeric)

# Operate Scaling function (Standard, MinMax, Robust)
standard_scaling(scale_test_df)
minmax_scaling(scale_test_df)
robust_scaling(scale_test_df)


# --------------------------- Missing value manipulation ---------------------------
# <Remove all likely-wrong values (eye inspection)> - finished
# <Print count of rows with NaN and count of NaN for each column>
print("\n**** Count of rows with NaN ****")
null_df = df[df.isnull().any(axis=1)]
print("Result: {0}".format(len(null_df)))
print("**** Count of NaN for each column ****")
print(df.isnull().sum(axis=0), end="\n")

# <Extract all rows without NaN>
print("**** Extract all rows without NaN ****")
print(df.dropna(axis=0))   # 현재 일부분만 출력중. 나중에 확인해보기

# <Fill NaN with mean, median, or using ffill/bfill methods>
# I will pick the ffill method and test.
print("**** Fill with ffill method ****")
print(df.fillna(axis=0, method="ffill"))


# --------------------------- Cleaning the Input Dataset ---------------------------
scale_test_df = scale_test_df.dropna(axis=0)   # Drop the NaN values
x = scale_test_df['Height (Inches)']
y = scale_test_df['Weight (Pounds)']
line_fit = LinearRegression()

# <Compute the linear regression equation E for height, weight values>
# Draw the Linear regression graph
line_fit.fit(x.values.reshape(-1, 1), y)
plt.plot(x, y, 'o')
plt.plot(x, line_fit.predict(x.values.reshape(-1, 1)))
plt.show()

# <Compute replacement values using E (height, weight)>
inclination = line_fit.coef_   # Graph inclination
intercept = line_fit.intercept_   # Graph intercept
for i in range(0, len(df)):
     temp = df.loc[i, ['Height (Inches)', 'Weight (Pounds)']]
     temp_height = temp['Height (Inches)']
     temp_weight = temp['Weight (Pounds)']

     if math.isnan(temp_weight) == True:
         wei = replace_weight(inclination, temp_height, intercept)
         df.loc[[i], 'Weight (Pounds)'] = wei
     elif math.isnan(temp_height) == True:
         hei = replace_height(inclination, temp_weight, intercept)
         df.loc[[i], 'Height (Inches)'] = hei