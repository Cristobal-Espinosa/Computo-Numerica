import numpy as np
from cargar_datos import precios, years, meses

def redondear_cifras_significativas(numeros, cifras): 
    factor = 10 ** (cifras - 1 - np.floor(np.log10(np.abs(numeros))))
    redondeo = np.round(numeros * factor) / factor
    return redondeo

precios_aproximados = redondear_cifras_significativas(precios, 2)
print("Precios originales:")
print(precios)

print("\nPrecios aproximados a 2 cifras significativas:")
print(precios_aproximados)

error_absoluto = np.abs(precios - precios_aproximados)
print("\nError absoluto:")
print(error_absoluto)

error_relativo = (error_absoluto / precios) * 100
print("\nError relativo:")
print(error_relativo)

indice_mayor_error = np.argmax(error_relativo)

print("\nMAYOR ERROR RELATIVO")
print("Año:", years[indice_mayor_error], "/Mes:", meses[indice_mayor_error])
print("Precio original:", precios[indice_mayor_error])
print("Precio aproximado:", precios_aproximados[indice_mayor_error])
print("Error absoluto:", round(error_absoluto[indice_mayor_error], 2))
print("Error relativo:", round(error_relativo[indice_mayor_error], 4))

indice_minimo = np.argmin(precios)
indice_maximo = np.argmax(precios)

print("\nPRECIO MINIMO")
print("Año:", years[indice_minimo], "/Mes:", meses[indice_minimo], "/Precio:", precios[indice_minimo])

print("\nPRECIO MAXIMO")
print("Año:", years[indice_maximo], "/Mes:", meses[indice_maximo], "/Precio:", precios[indice_maximo])

monto_inicial = 1000000

precio_compra = precios[indice_minimo]
precio_venta = precios[indice_maximo]

dolares_comprados = monto_inicial / precio_compra

pesos_finales = dolares_comprados * precio_venta

ganancia = pesos_finales - monto_inicial

rentabilidad = (ganancia / monto_inicial) * 100


print("\nSIMULACION COMPRA Y VENTA")

print("Monto inicial:", monto_inicial)
print("\nCompra:")
print("Año:", years[indice_minimo], "/Mes:", meses[indice_minimo], "/Precio:", precio_compra)

print("\nVenta:")
print("Año:", years[indice_maximo], "/Mes:", meses[indice_maximo], "/Precio:", precio_venta)

print("\nDólares comprados:", round(dolares_comprados, 2))
print("Pesos finales:", round(pesos_finales, 2))
print("Ganancia:", round(ganancia, 2))
print("Rentabilidad:", round(rentabilidad, 2))

precio_compra_aprox = precios_aproximados[indice_minimo]
precio_venta_aprox = precios_aproximados[indice_maximo]

dolares_aprox = monto_inicial / precio_compra_aprox

pesos_finales_aprox = dolares_aprox * precio_venta_aprox

ganancia_aprox = pesos_finales_aprox - monto_inicial

rentabilidad_aprox = (ganancia_aprox / monto_inicial) * 100

print("\nSIMULACIÓN CON PRECIOS APROXIMADOS")
print("Precio de compra aproximado:", precio_compra_aprox)
print("Precio de venta aproximado:", precio_venta_aprox)
print("Dolares comprados:", round(dolares_aprox, 2))
print("Pesos finales:", round(pesos_finales_aprox, 2))
print("Ganancia:", round(ganancia_aprox, 2))
print("Rentabilidad:", round(rentabilidad_aprox, 2))

error_compra = error_relativo[indice_minimo]
error_venta = error_relativo[indice_maximo]

error_dolares_aprox = error_compra

error_pesos_finales_aprox = error_dolares_aprox + error_venta

error_pesos_finales_absoluto = (error_pesos_finales_aprox / 100) * pesos_finales_aprox

error_ganancia_absoluto = error_pesos_finales_absoluto

error_ganancia_relativo = (error_ganancia_absoluto / abs(ganancia_aprox)) * 100


print("\nERROR PROPAGADO EN LA GANANCIA")

print("Error relativo precio compra:", round(error_compra, 4))
print("Error relativo precio venta:", round(error_venta, 4))

print("\nError relativo pesos finales:", round(error_pesos_finales_aprox, 4))
print("Error absoluto pesos finales:", round(error_pesos_finales_absoluto, 2))

print("\nGanancia:", round(ganancia_aprox, 2), "+/-", round(error_ganancia_absoluto, 2))
print("Error relativo en la ganancia:", round(error_ganancia_relativo, 4))


precios_aprox_3cifras = redondear_cifras_significativas(precios, 3)

precio_dic2022 = precios_aprox_3cifras[11]
precio_dic2023 = precios_aprox_3cifras[23]

delta_p = precio_dic2023 - precio_dic2022

error_dic2022 = abs(precios[11] - precio_dic2022)
error_dic2023 = abs(precios[23] - precio_dic2023)

error_delta = error_dic2022 + error_dic2023

error_delta_relativo = (error_delta / abs(delta_p)) * 100


print("\nCANCELACION DICIEMBRE 2022 VS 2023")

print("Precio dic 2022 (3 cifras):", precio_dic2022, "+/-", round(error_dic2022, 2))
print("Precio dic 2023 (3 cifras):", precio_dic2023, "+/-", round(error_dic2023, 2))

print("\nDelta P:", round(delta_p, 2), "+/-", round(error_delta, 2))
print("Error relativo (%):", round(error_delta_relativo, 4))

if error_delta > abs(delta_p):
    print("\nEl error es mayor que la variacion, no se puede afirmar si el dolar subio o bajo")
else:
    print("\nLa variacion es mayor que el error, si se puede afirmar la tendencia")