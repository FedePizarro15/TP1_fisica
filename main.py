import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def diametros_(archivo = "Trabajo Práctico 1.xlsx"):
    df = pd.read_excel(archivo, engine="openpyxl")
    datos1 = df.iloc[3:13, 4:7].mean(axis=1).values
    datos2 = df.iloc[15:19, 4:7].mean(axis=1).values
    datos3 = df.iloc[21:25, 4:7].mean(axis=1).values

    return np.array(np.concatenate((datos1, datos2, datos3)))

def std_(array):
    return np.std(array, ddof=1)

def calcular_error(desviacion):
    error_instrumental = 0.1 # (0.1 mm)
    error_total = np.sqrt(desviacion**2 + error_instrumental**2)
    return error_total

def masas_(archivo = "Trabajo Práctico 1.xlsx"):
    df = pd.read_excel(archivo, engine="openpyxl")
    datos1 = df.iloc[3:13, 10].values
    datos2 = df.iloc[15:19, 10].values
    datos3 = df.iloc[21:25, 10].values
    
    return np.array(np.concatenate((datos1, datos2, datos3)))

def graficar_promedios(diametros, masas, errores, escala_log: bool):
    if escala_log:
        plt.xscale("log")
        plt.yscale("log")
    plt.scatter(masas, diametros, color="darkblue", label="Datos", s=60, alpha=0.8)
    plt.errorbar(masas, diametros, yerr=errores, fmt="o", color="c", label="Desviación estándar")
    plt.xlabel("Masas")
    plt.ylabel("Diámetros")
    plt.title("Masa en función del diámetro")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def main():
    graficar_promedios(diametros_(), masas_(), calcular_error(std_(diametros_())), True)
    
if __name__ == "__main__":
    main()
