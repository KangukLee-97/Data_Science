# NumPy Exercise => Compute BMI
# BMI = weight / (height * height)
# weight => kg, height => m
import numpy as np

# Create wt array and ht array, each of size 100.
wt = np.random.random(100) * 50 + 40
ht = np.random.randint(140, 200+1, size=100)
ht = ht / 100   # cemtimeter -> meter

# Compute the BMI for the 100 students, store them in bmi array and print
print("<Print the BMI Array>")
bmi = np.zeros(100)
for i in range(0, 100):
    bmi[i] = wt[i] / (ht[i] * ht[i])
print(bmi, end="\n\n")

# The first 10 elements of wt, ht and bmi arrays
print("<Print the first 10 elements of wt, ht and bmi arrays>")
form = '%-20s%-10s%s\n'
out = form % ('wt', 'ht', 'BMI')
for i in range(0, 10):
    out += form % (wt[i], ht[i], bmi[i])
print(out)

# MatPlotLib Exercise => Draw the box plot, histogram, pie chart and scatter plot
import matplotlib.pyplot as plt

# Box Plot (boxes = 4)
set1 = []   # below 18.5 
set2 = []   # 18.5-24.9
set3 = []   # 25.0-29.9
set4 = []   # 30.0 and above

for i in range(0, 100):
    if bmi[i] < 18.5:
        set1.append(bmi[i])
    elif 18.5 <= bmi[i] < 25.0:
        set2.append(bmi[i])
    elif 25.0 <= bmi[i] < 30.0:
        set3.append(bmi[i])
    elif bmi[i] >= 30.0:
        set4.append(bmi[i])

plotData = [set1, set2, set3, set4]
plt.boxplot(plotData)
plt.show()   # Show the chart

# histogram (bins = 4)
plt.hist(bmi, bins = [10, 18.5, 25, 45.92])   # min : 10, max : about 45.91XX (45.92) / where 30? not include
plt.title("histogram of result")
plt.xticks([10, 18.5, 25, 45.92])
plt.xlabel("BMI")
plt.ylabel("Number of Students")
plt.show()

# Pie chart
plt.pie([len(set1), len(set2), len(set3), len(set4)],   # count
        autopct="%1.2f%%",   # under point
        labels=["Underweight", "Healthy", "Overweight", "Obese"])
plt.show()

# Scatter
plt.scatter(wt, ht)
plt.xlabel("weight")
plt.ylabel("height * height")
plt.show()