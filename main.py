import pandas as pd
import matplotlib.pyplot as plt

archivo = "Trabajo Práctico 1.xlsx"
df = pd.read_excel(archivo, engine="openpyxl")

print(df.iloc[3, 4:7])

df["diametro_promedio"] = df.iloc[5:15, 5].mean(axis=1)

print(df["diametro_promedio"])