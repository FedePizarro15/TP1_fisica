import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def diametros_(archivo = "Trabajo Práctico 1.xlsx") -> tuple[np.array, np.array]:
    df = pd.read_excel(archivo, engine="openpyxl")
    datos1_prom = df.iloc[3:13, 4:7].mean(axis=1).values
    datos2_prom = df.iloc[14:19, 4:7].mean(axis=1).values
    datos3_prom = df.iloc[20:25, 4:7].mean(axis=1).values
    
    datos1_std = df.iloc[3:13, 4:7].values
    datos2_std = df.iloc[14:19, 4:7].values
    datos3_std = df.iloc[20:25, 4:7].values
    datos_std = np.array(np.concatenate((datos1_std, datos2_std, datos3_std)))
    for i in range(len(datos_std)):
        datos_std[i] = np.std(datos_std[i])
    
    return np.array(np.concatenate((datos1_prom, datos2_prom, datos3_prom))), datos_std.mean(axis=1)

def incertidumbres_diametro(diametros_std):
    diametros_i = []
    for i in range(len(diametros_std)):
        diametros_i.append(np.sqrt(0.0025 + (diametros_std[i] / np.sqrt(3))))
    return np.array(diametros_i)

def incertidumbres_masas():
    return np.ones(20) * 0.01

def masas_(archivo = "Trabajo Práctico 1.xlsx") -> np.array:
    df = pd.read_excel(archivo, engine="openpyxl")
    datos1 = df.iloc[3:13, 10].values
    datos2 = df.iloc[14:19, 10].values
    datos3 = df.iloc[20:25, 10].values
    
    return np.array(np.concatenate((datos1, datos2, datos3)))

def propagacion_de_errores(diametros: np.array, diametros_i: np.array, masas: np.array, masas_i: np.array):
    diametros_i_ln = np.abs(diametros_i / diametros)
    masas_i_ln = np.abs(masas_i / masas)
    
    return diametros_i_ln, masas_i_ln

def graficar_promedios(diametros: np.array, masas: list, diametros_i: np.array, masas_i: np.array, escala_log: bool, ajuste_lineal: bool, mismo_grafico: bool):
    masas = np.array(masas, dtype=float)
    diametros = np.array(diametros, dtype=float)
    diametros_i = np.array(diametros_i, dtype=float)
    masas_i = np.array(masas_i, dtype=float)
    xlabel_ = "Masas (g)"
    ylabel_ = "Diámetros (mm)"
    if escala_log: # Log natural
        diametros_i, masas_i = propagacion_de_errores(diametros, diametros_i, masas, masas_i)
        masas = np.log(masas) 
        diametros = np.log(diametros)
        xlabel_ += " log"
        ylabel_ += " log"
        
    if mismo_grafico:
        plt.errorbar(masas, diametros, yerr=diametros_i, xerr=masas_i, fmt=".", color="c", label="Desviación estándar L")
    else:
        plt.errorbar(masas[:10], diametros[:10], yerr=diametros_i[:10], xerr=masas_i[:10], fmt=".", color="c", label="Desviación estándar L")
        plt.errorbar(masas[10:15], diametros[10:15], yerr=diametros_i[10:15], xerr=masas_i[10:15], fmt=".", color="m", label="Desviación estándar M")
        plt.errorbar(masas[15:20], diametros[15:20], yerr=diametros_i[15:20], xerr=masas_i[15:20], fmt=".", color="green", label="Desviación estándar P")
    
    if ajuste_lineal:
        if mismo_grafico:
            m, b = np.polyfit(masas, diametros, 1)
            y_fit = m * masas + b
            plt.plot(masas, y_fit, color="c", label=f'Ajuste lineal L: y = {m:.2f}x + {b:.2f}')
        else:
            m, b = np.polyfit(masas[:10], diametros[:10], 1)
            y_fit = m * masas[:10] + b
            plt.plot(masas[:10], y_fit, color="c", label=f'Ajuste lineal L: y = {m:.2f}x + {b:.2f}')
            
            m, b = np.polyfit(masas[10:15], diametros[10:15], 1)
            y_fit = m * masas[10:15] + b
            plt.plot(masas[10:15], y_fit, color="m", label=f'Ajuste lineal M: y = {m:.2f}x + {b:.2f}')
            
            m, b = np.polyfit(masas[15:20], diametros[15:20], 1)
            y_fit = m * masas[15:20] + b
            plt.plot(masas[15:20], y_fit, color="green", label=f'Ajuste lineal P: y = {m:.2f}x + {b:.2f}')
        
    plt.xlabel(xlabel_)
    plt.ylabel(ylabel_)
    plt.title("Masa en función del diámetro")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def main():
    graficar_promedios(diametros_()[0], 
                       masas_(), 
                       incertidumbres_diametro(diametros_()[1]), 
                       incertidumbres_masas(), 
                       escala_log=True, 
                       ajuste_lineal=True,
                       mismo_grafico=False)
    
if __name__ == "__main__":
    main()
