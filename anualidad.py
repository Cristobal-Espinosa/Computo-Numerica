import numpy as np
from cargar_datos import precios, years, meses

def redondear_cifras_significativas(numeros, cifras):
    factor = 10 ** (cifras - 1 - np.floor(np.log10(np.abs(numeros))))
    redondeo = np.round(numeros * factor) / factor
    return redondeo

years = [2022, 2023, 2024, 2025]
indices_enero = [0, 12, 24, 36]
indices_diciembre = [11, 23, 35, 47]

resultados = []

for i in range(4):
    year = years[i]
    idx_enero = indices_enero[i]
    idx_dic = indices_diciembre[i]

    precio_enero = precios[idx_enero]
    precio_dic = precios[idx_dic]

    precio_enero_aprox = redondear_cifras_significativas(precio_enero, 2)
    precio_dic_aprox = redondear_cifras_significativas(precio_dic, 2)

    variacion = precio_dic_aprox - precio_enero_aprox

    error_enero = abs(precio_enero - precio_enero_aprox)
    error_dic = abs(precio_dic - precio_dic_aprox)

    error_variacion = error_enero + error_dic

    error_relativo = (error_variacion / abs(variacion)) * 100

    resultados.append((year, precio_enero_aprox, precio_dic_aprox, variacion, error_variacion, error_relativo))

    print("Año:", year)
    print("Precio enero aprox:", precio_enero_aprox, "+/-", round(error_enero, 2))
    print("Precio diciembre aprox:", precio_dic_aprox, "+/-", round(error_dic, 2))
    print("Variacion:", round(variacion, 2), "+/-", round(error_variacion, 2))
    print("Error relativo:", round(error_relativo, 4))


resultados_ordenados = sorted(resultados, key=lambda x: x[5])

print("\nRANKING DE CONFIABILIDAD (menor a mayor error relativo)")

for r in resultados_ordenados:
    print("Año:", r[0], " Variacion:", round(r[3], 2), " Error relativo:", round(r[5], 4))