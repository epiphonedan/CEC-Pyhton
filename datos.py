import pandas as pd
titulos = pd.read_csv('data/titles.csv' )
print(titulos.head(100))
print("\n"*2)
elenco = pd.read_csv('data/cast.csv', encoding='utf-8')
print(elenco.head(10))
print(len(titulos))
print(titulos[titulos.title=="Romeo and Juliet"].sort_values("year").head(5))

print(titulos[titulos.title.str.contains("Exorcist")].sort_values("year"))

print(titulos[titulos.title.str.contains("Star Wars")].sort_values("year"))

print(titulos[titulos.title.str.contains("Batman")].sort_values("year"))



print(len( titulos[ (titulos.year >= 1980) & (titulos.year <= 2000)]))