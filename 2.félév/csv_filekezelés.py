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

# Másik megoldás
max_index = data["Age"].argmax() # Legnagyobb elem indexe
max_name = data.iloc[max_index, 3].replace('"', '').strip()
max_age = data.iloc[max_index, 2]
print(f"A legidősebb nyertes {max_name} volt. {max_age} évesen nyerte a díjat.")

# Keressük meg, hogy mikor nyert a Fargo című film!
találatok = data[data["Movie"].str.contains("Fargo")]
print(találatok[["Year", "Movie"]])

# Ki nyerte a legtöbb díjat?
most_frequent_name = data["Name"].value_counts().idxmax()
frequency = data["Name"].value_counts().max()
print(f"A legtöbb Oscart {most_frequent_name} nyerte. Összesen {frequency} alkalommal.")

# Ábrázoljuk egy scatter-plot-on, az oscar nyerteseket age és évszám szempontból

data = pd.read_csv("oscar_age_female.csv", usecols = ["Year", "Age"])
plt.scatter(data["Year"], data["Age"])
plt.title("Életkor-évszám diagramm")
plt.xlabel("Évszám")
plt.ylabel("Életkor")
plt.close()

# Ábrázoljuk egy kördiagrammon, hogy az egyes életkorok milyen sűrűn nyertek oscart!

counts = data["Age"].value_counts()
counts = counts.head(10)

explode_list = [0.1 for i in range(len(counts))]
explode_list[0] = 0.1

plt.pie(counts, labels=counts.index, autopct="%1.1f%%", explode=explode_list)
plt.close()

# Határozzuk meg a magánhangzók sűrűségét!

letters = pd.read_csv("letter_frequency.csv", skipinitialspace=True)
vowels = "AEUIO"
vowel_count = 0
for index, row in letters.iterrows():
    if row["Letter"] in vowels:
        vowel_count += row["Percentage"]
print(f"A betűk {round(vowel_count, 2)}%-a magánhangzó.")

