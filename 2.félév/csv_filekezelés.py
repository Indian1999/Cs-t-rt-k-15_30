import csv
import pandas as pd # terminálba: pip install pandas
import matplotlib.pyplot as plt # pip install matplotlib.pyplot

"""
file = open("oscar_age_female.csv", "r")

data = csv.reader(file, delimiter = ",")
for row in data:
    print(row)

file.close()
"""

data = pd.read_csv("oscar_age_female.csv")
print(data)
print(type(data)) # <class 'pandas.core.frame.DataFrame'>
print(data.head(10))

# Mennyi volt a nyertesek átlag életkora?
print("A női oscar nyertesek átlag életkora:", round(data["Age"].mean(), 1))

# Keressük meg a legidősebb nyertest!
max_age = data["Age"].max()
print(max_age)
max_row = data[data["Age"] == max_age]
max_name = max_row.iloc[0, 3].replace('"', '').strip()
print(f"A legidősebb nyertes {max_name} volt. {max_age} évesen nyerte a díjat.")

# Keressük meg, hogy mikor nyert a Fargo című film!

# Ki nyerte a legtöbb díjat?