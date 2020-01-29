import pandas as pd


# pd.set_option('display.float_format')

d = [10, 30, 40]
i = [1, 2, 3]

s = pd.Series(d, i)

# print(s)

d = {'a': 10, 'b':20, 'c':30}

sd = pd.Series(d)
# print(sd)

# print(sd.index)

# print(sd[2])

l = [10, 3, 6, 7, 8]

df = pd.DataFrame(l)
# print(df)

d = {'one': [1,2,3], 'two': [4,5,6], 'three': [7,8,9]}
df = pd.DataFrame(d)
# print(df)

# print(df["one"])

df["four"] = df["one"] + df["two"]
# print(df)
# print(df["four"])

del df["four"]

df["five"] = 9

# print(df)

# print(df)

df.index = [1,2,3]
# print(df)


# print(df.iloc[0])
# print(df.loc[1])

df.rename(columns={'one': 'ONE'}, inplace=True)
# print(df)

file = r'/home/matteo/lavori/miei/2020_python_ravenna/python-course/data/natural_disasters.csv'

natural = pd.read_csv(file)
# print(natural.head())

# print(natural["Entity"] == 'Flood')

sub = natural[(natural["Entity"] == 'Flood') & (natural["Year"] > 1950) ]

sub1 = natural[(natural["Entity"] == 'Flood') | (natural["Entity"] == 'Earthquake') ]

# print(natural.describe())

# print(natural[["Year","Deaths"]].describe().round(2))

# print(natural["Deaths"].sum())

# print(natural.head())

natural["Deaths"].idxmax()


# print(natural.iloc[natural["Deaths"].idxmax()])


gb = natural.groupby("Entity")["Deaths"].sum()

# print(gb)


e = natural[natural["Entity"] == 'Earthquake']
# print(e["Deaths"].sum())

t = natural[natural["Entity"] == 'Earthquake'].groupby("Entity")["Deaths"].sum()
# print(t)


f = natural[(natural["Entity"] == 'Flood') & (natural["Year"] >= 1950) & (natural["Year"] <= 1980)]

print(f["Deaths"].mean())


