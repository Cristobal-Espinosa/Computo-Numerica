import os
import numpy as np

carpeta = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(carpeta, "..", "data", "dolar_observado_sii_2022_2025.csv")

datos = np.genfromtxt(ruta_csv, delimiter=",", skip_header=1, dtype=None, encoding="utf-8")

years = datos["f0"]
meses = datos["f1"]
numeros_mes = datos["f2"]
precios = datos["f3"]

#print("Precios originales:")
#print(precios)