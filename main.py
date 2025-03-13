import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def diametros_(archivo = "Trabajo Práctico 1.xlsx") -> np.array:
    df = pd.read_excel(archivo, engine="openpyxl")
    datos1 = df.iloc[3:13, 4:7].mean(axis=1).values
    datos2 = df.iloc[15:19, 4:7].mean(axis=1).values
    datos3 = df.iloc[21:25, 4:7].mean(axis=1).values

    return np.array(np.concatenate((datos1, datos2, datos3)))

def std_(array: np.array) -> np.array:
    desviacion_std = []
    for i in array:
        desviacion_std.append(np.std(np.array([i, i+0.5, i-0.5])))
    return np.array(desviacion_std)

def calcular_error(desviacion):
    error_instrumental = 0.1 # (0.1 mm)
    error_total = np.sqrt(desviacion**2 + error_instrumental**2)
    return error_total

def masas_(archivo = "Trabajo Práctico 1.xlsx") -> np.array:
    df = pd.read_excel(archivo, engine="openpyxl")
    datos1 = df.iloc[3:13, 10].values
    datos2 = df.iloc[15:19, 10].values
    datos3 = df.iloc[21:25, 10].values
    
    return np.array(np.concatenate((datos1, datos2, datos3)))

def graficar_promedios(diametros: np.array, masas: np.array, desviacion_std: np.array, escala_log: bool, ajuste_lineal: bool):
    print(np.shape(desviacion_std))
    masas = np.array(masas, dtype=float)
    diametros = np.array(diametros, dtype=float)
    desviacion_std = np.array(desviacion_std, dtype=float)
    if escala_log:
        masas = np.log(masas)
        diametros = np.log(diametros)
        desviacion_std = 0 # A chequear
    
    plt.errorbar(masas, diametros, yerr=desviacion_std, fmt=".", color="c", label="Desviación estándar")
    
    if ajuste_lineal:
        m, b = np.polyfit(masas, diametros, 1)
        y_fit = m * masas + b
        plt.plot(masas, y_fit, color="red", label=f'Ajuste lineal: y = {m:.2f}x + {b:.2f}')
        
    plt.xlabel("Masas")
    plt.ylabel("Diámetros")
    plt.title("Masa en función del diámetro")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def main():
    graficar_promedios(diametros_(), masas_(), std_(diametros_()), escala_log=False, ajuste_lineal=False)
    
if __name__ == "__main__":
    main()
