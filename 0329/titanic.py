# Kaggle 타이타닉 데이터 분석 및 시각화
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv("./titanic/train.csv")
test = pd.read_csv("./titanic/test.csv")

# 상위 5줄의 Data를 출력
print("***** Train_set *****")
print(train.head(), end="\n")
print("***** Test_set *****")
print(test.head(), end="\n")

# 데이터를 요약
print("***** Train_set *****")
print(train.describe(), end="\n")
print("***** Test_set *****")
print(test.describe(), end="\n")

# 컬럼 값 출력
print(train.columns.values)

# 결측값이 존재하는지 확인
print(train.isna().head())
print(test.isna().head())

# 결측값의 갯수 확인
print("***** In the train set *****")
print(train.isna().sum())
print("***** In the test set *****")
print(test.isna().sum())

# 결측값을 지정값으로 채우기
train.fillna(train.mean(), inplace=True)
test.fillna(test.mean(), inplace=True)
print(train.isna().sum())
print(test.isna().sum())

print(train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False))

graph = sns.FacetGrid(train, col="Survived")
graph.map(plt.hist, 'Age', bins=20)
print(graph)
grid = sns.FacetGrid(train, col="Survived", row="Pclass", height=2.2, aspect=1.6)
grid.map(plt.hist, 'Age', alpha=.5, bins=20)
grid.add_legend()
print(grid)

# 각 컬럼에 대한 정보 출력
print(train.info())

# 컬럼 삭제 (axis=0이면 행, axis=1이면 열 삭제)
train = train.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)
test = test.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)

# LabelEncoder : 숫자가 아닌 값을 숫자로 바꿔준다
# ex) Sex -> f와 m이 존재한다 => Encoder를 통해서 0 또는 1로 바꿔준다
train['Sex'].unique()
encoder = LabelEncoder()
encoder.fit(train['Sex'])
encoder.fit(test['Sex'])
train['Sex'] = encoder.transform(train['Sex'])
test['Sex'] = encoder.transform(test['Sex'])