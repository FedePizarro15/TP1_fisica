import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def diametros_(archivo = "Trabajo Práctico 1.xlsx"):
    df = pd.read_excel(archivo, engine="openpyxl")
    datos1 = df.iloc[3:13, 4:7].mean(axis=1).values
    datos2 = df.iloc[15:19, 4:7].mean(axis=1).values
    datos3 = df.iloc[21:25, 4:7].mean(axis=1).values

    return np.array(np.concatenate((datos1, datos2, datos3)))

def std_(array: np.array):
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

def graficar_promedios(diametros: np.array, masas: np.array, errores: float, escala_log: bool, ajuste_lineal: bool):
    masas = np.array(masas, dtype=float)
    diametros = np.array(diametros, dtype=float)
    if escala_log:
        masas = np.log(masas)
        diametros = np.log(diametros)
    
    plt.scatter(masas, diametros, color="darkblue", label="Datos", s=60, alpha=0.8)
    plt.errorbar(masas, diametros, yerr=errores, fmt="o", color="c", label="Desviación estándar")
    
    if ajuste_lineal:
        # Ajuste lineal mediante mínimos cuadrados
        m, b = np.polyfit(masas, diametros, 1)  # grado 1 para línea
        y_fit = m * masas + b
        plt.plot(masas, y_fit, color="red", label=f'Ajuste lineal: y = {m:.2f}x + {b:.2f}')
        
    plt.xlabel("Masas")
    plt.ylabel("Diámetros")
    plt.title("Masa en función del diámetro")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def main():
    graficar_promedios(diametros_(), masas_(), calcular_error(std_(diametros_())), True, True)
    
if __name__ == "__main__":
    main()
