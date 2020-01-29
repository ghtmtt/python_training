import pandas as pd
import matplotlib.pyplot as plt

file = '/home/matteo/lavori/miei/2020_python_ravenna/python-course/data/air.csv'

df = pd.read_csv(
    file, 
    sep=';', 
    na_values=[-200], 
    parse_dates=[["Date", "Time"]],
    usecols=["Date", "Time", "CO(GT)", "T", "RH", "AH"]
).rename(columns={"Date_Time": 'tstamp', 'CO(GT)': 'CO', 'T': 'T', 'RH': 'rel_hum', 'AH': 'abs_hum'})

# print(df.head())

df["tstamp2"] = pd.to_datetime(df["tstamp"], format='%d/%m/%Y %H.%M.%S')
print(df.head())

df.index = df["tstamp2"]

# print(df.index.day_name())

# print(df.groupby(df.index.day_name())["CO"].mean().sort_values(ascending=False))
# print(df.groupby([df.index.day_name(), df.index.hour])["CO"].mean().sort_values(ascending=False)

month_values = df.resample("M")["CO"].agg(["mean", "max"])
# print(month_values)

month_values.to_csv('/home/matteo/Desktop/month_mean.csv')

plt.show()

