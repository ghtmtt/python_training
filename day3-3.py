import pandas as pd
import matplotlib.pyplot as plt

file = '/home/matteo/lavori/miei/2020_python_ravenna/python-course/data/natural_disasters.csv'

df = pd.read_csv(file)

# df.plot(x='Year', y='Deaths', kind='box')

gb = df.groupby("Entity").mean()

# gb.plot(y="Deaths", kind='bar', color='red')

# group by Year with mean aggregation function and make a plot of type line where Y axis = Deaths

gy = df.groupby("Year").sum()

gy.plot(y="Deaths", kind='line')

# plt.show()


file1 = '/home/matteo/lavori/miei/2020_python_ravenna/python-course/data/d1.csv'
file2 = '/home/matteo/lavori/miei/2020_python_ravenna/python-course/data/d2.csv'

d1 = pd.read_csv(file1)
d2 = pd.read_csv(file2)

d3 = d1.merge(d2, left_on="Code", right_on="Code", suffixes=('_left', '_right'))
print(d3.head())
