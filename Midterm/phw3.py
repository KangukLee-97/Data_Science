# Programming Homework 3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.preprocessing as preprocessing
from sklearn.linear_model import LinearRegression


def standard_scaling(dataframe):  # StandScaling function
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


def minmax_scaling(dataframe):  # MinMaxScaling function
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


def robust_scaling(dataframe):  # RobustScaling function
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


# --------------------------- Read the Excel dataset file ---------------------------
df = pd.read_excel("bmi_data_phw3.xlsx")

# --------------------------- Data Exploration ---------------------------
# <Print dataset statistical data, feature names & data types>
print("**** Statistical data ****")
print(df.describe(), end="\n")
print("**** Feature names & Data types ****")
print(df.info(), end="\n")

# <Plot height & weight histograms for each BMI value>
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6,5))

# <Plot scaling results for height and weight>
scale_test_df = df.drop(columns="Sex")  # Make the temporary data frame dropped the Sex columns (not numeric)

# Operate Scaling function (Standard, MinMax, Robust)
standard_scaling(scale_test_df)
minmax_scaling(scale_test_df)
robust_scaling(scale_test_df)

