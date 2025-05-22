import pandas as pd # terminálba: pip install pandas


data = pd.read_csv("oscar_age_female.csv")
print(data)
print(type(data)) # <class 'pandas.core.frame.DataFrame'>

print(data["Name"])

átlag_életkor = data["Age"].mean()
print(f"Az Oscar nyertesek átlag életkora: { átlag_életkor }")

legidősebb_kor = data["Age"].max()
print(f"A legidősebb nyertes {legidősebb_kor} éves volt.")

fiatal_nyertesek = data[data["Age"] < 26]
print(fiatal_nyertesek)

max_age_row = data[data["Age"] == legidősebb_kor]
print(max_age_row)
print("A legidősebb nyertes:", max_age_row.iloc[0, 3].strip().replace('"', ''))