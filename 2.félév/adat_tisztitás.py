import pandas as pd # pip install pandas
import numpy as np  # pip install numpy

library = pd.read_csv("library.csv") # DataFrame-ben lesznek eltárolva
library = library.drop(["Edition Statement", "Corporate Contributors", "Corporate Author", "Contributors", "Former owner", "Engraver", "Issuance type"], axis = 1)
library = library.drop(columns = ["Shelfmarks", "Flickr URL"])

print(library.head())

# Miért axis = 1 az oszlopnak a jelölése?
matrix = np.zeros((4, 5, 7, 8))
print(matrix.shape) # (4, 5, 7, 8)
#matrix.shape[0] - sorok száma
#matrix.shape[1] - oszlopok száma
#matrix.shape[2] - mélység

##########################################
# Oszlopok újraindexelése

# 1. Nézzük meg hogy minden sorban különböző-e a kulcs-jelölt érték!

print("Identifier oszlop egyedi:", library["Identifier"].is_unique)
print("Place of Publication oszlop egyedi:", library["Place of Publication"].is_unique)

# Mivel az identifier egyedi, ezért használhatjuk indexként:
library = library.set_index("Identifier")
print(library.head())

# A date of publication oszlopot módosítsuk úgy, hogy csak az első 4 szám legyen benne

# Az extract fgv első paramétere pat (pattern), ennek kell megadni, hogy milyen mintát szedjen ki a stringből
# Ezt a mintát reguláris kifejezéssel tudjuk leírni [Regular Expression (Regex)]
years = library["Date of Publication"].str.extract(r"(\d{4})")
print(type(years))
print(years)
library["Date of Publication"] = pd.to_numeric(years[0])
print(library["Date of Publication"])
print(library.dtypes)

# Számoljuk meg hogy hány null érték van a date of publication oszlopban
print("Null értékek száma a Date of Publication oszlopban:", library["Date of Publication"].isnull().sum())
average = round(library["Date of Publication"].mean())
print(average)
library["Date of Publication"] = library["Date of Publication"].fillna(average)
library["Date of Publication"] = library["Date of Publication"].astype("int")
print(library["Date of Publication"])
print("Null értékek száma a Date of Publication oszlopban:", library["Date of Publication"].isnull().sum())

# Ezekkel megoldottuk, hogy a Date of Publication oszlop tiszta adatokat tartalmazzon