# Standard Scaling
import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([28, 35, 26, 32, 28, 28, 35, 34, 46, 42, 37])

print("The mean: {0}".format(round(data.mean(), 1)))
print("The standard deviation: {0}".format(round(data.std(), 1)))

new_data = data.reshape(11, 1)
scaler = StandardScaler()
scaler = scaler.fit_transform(new_data)
print("The standard scores: ", end="\n")
for i in range(0, len(scaler)):
    print(round(scaler[i][0], 2), end=" ")

print("\nWhich scores should receive an F?")
for i in range(0, len(scaler)):
    if scaler[i][0] <= -1:
        print(round(scaler[i][0], 2), end=" ")