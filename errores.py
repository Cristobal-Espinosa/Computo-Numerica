import numpy as np
from cargar_datos import precios, years, meses

def redondear_cifras_significativas(numeros, cifras):
    
    factor = 10 ** (cifras - 1 - np.floor(np.log10(np.abs(numeros))))
    
    return np.round(numeros * factor) / factor

precios_aproximados = redondear_cifras_significativas(precios, 2)

error_absoluto = np.abs(precios - precios_aproximados)

error_relativo = (error_absoluto / precios) * 100


print("Precios originales:")
print(precios)

print("\nPrecios aproximados a 2 cifras significativas:")
print(precios_aproximados)

print("\nError absoluto:")
print(error_absoluto)

print("\nError relativo (%):")
print(error_relativo)

indice_mayor_error = np.argmax(error_relativo)

print("\n--- MAYOR ERROR RELATIVO ---")

print("Año:", years[indice_mayor_error])
print("Mes:", meses[indice_mayor_error])
print("Precio original:", precios[indice_mayor_error])
print("Precio aproximado:", precios_aproximados[indice_mayor_error])
print("Error absoluto:", round(error_absoluto[indice_mayor_error], 2))
print("Error relativo (%):", round(error_relativo[indice_mayor_error], 4))


indice_minimo = np.argmin(precios)
indice_maximo = np.argmax(precios)

print("\n--- PRECIO MÍNIMO ---")
print("Año:", years[indice_minimo])
print("Mes:", meses[indice_minimo])
print("Precio:", precios[indice_minimo])

print("\n--- PRECIO MÁXIMO ---")
print("Año:", years[indice_maximo])
print("Mes:", meses[indice_maximo])
print("Precio:", precios[indice_maximo])

monto_inicial = 1000000

precio_compra = precios[indice_minimo]
precio_venta = precios[indice_maximo]

# Cantidad de dólares comprados
dolares_comprados = monto_inicial / precio_compra

# Pesos obtenidos al vender
pesos_finales = dolares_comprados * precio_venta

# Ganancia
ganancia = pesos_finales - monto_inicial

# Rentabilidad
rentabilidad = (ganancia / monto_inicial) * 100


print("\n--- SIMULACIÓN COMPRA Y VENTA ---")

print("Monto inicial:", monto_inicial)

print("\nCompra:")
print("Año:", years[indice_minimo])
print("Mes:", meses[indice_minimo])
print("Precio de compra:", precio_compra)

print("\nVenta:")
print("Año:", years[indice_maximo])
print("Mes:", meses[indice_maximo])
print("Precio de venta:", precio_venta)

print("\nDólares comprados:", round(dolares_comprados, 2))
print("Pesos finales:", round(pesos_finales, 2))
print("Ganancia:", round(ganancia, 2))
print("Rentabilidad (%):", round(rentabilidad, 2))


# Precios aproximados correspondientes a la compra y venta

precio_compra_aprox = precios_aproximados[indice_minimo]
precio_venta_aprox = precios_aproximados[indice_maximo]


# Cantidad de dólares usando precios aproximados

dolares_aprox = monto_inicial / precio_compra_aprox


# Pesos finales usando precios aproximados

pesos_finales_aprox = dolares_aprox * precio_venta_aprox


# Ganancia usando precios aproximados

ganancia_aprox = pesos_finales_aprox - monto_inicial


# Rentabilidad usando precios aproximados

rentabilidad_aprox = (ganancia_aprox / monto_inicial) * 100


print("\n--- SIMULACIÓN CON PRECIOS APROXIMADOS ---")

print("Precio de compra aproximado:", precio_compra_aprox)
print("Precio de venta aproximado:", precio_venta_aprox)

print("Dólares comprados:", round(dolares_aprox, 2))
print("Pesos finales:", round(pesos_finales_aprox, 2))
print("Ganancia:", round(ganancia_aprox, 2))
print("Rentabilidad (%):", round(rentabilidad_aprox, 2))

# Diferencia entre la ganancia real y la aproximada

error_ganancia_absoluto = abs(ganancia - ganancia_aprox)

error_ganancia_relativo = (
    error_ganancia_absoluto / abs(ganancia)
) * 100


# Diferencia en la rentabilidad

error_rentabilidad = abs(rentabilidad - rentabilidad_aprox)


print("\n--- ERROR PRODUCIDO POR LA APROXIMACIÓN ---")

print("Ganancia real:", round(ganancia, 2))
print("Ganancia aproximada:", round(ganancia_aprox, 2))

print("\nError absoluto en la ganancia:",
      round(error_ganancia_absoluto, 2))

print("Error relativo en la ganancia (%):",
      round(error_ganancia_relativo, 4))

print("\nRentabilidad real (%):",
      round(rentabilidad, 4))

print("Rentabilidad aproximada (%):",
      round(rentabilidad_aprox, 4))

print("Diferencia en rentabilidad (puntos porcentuales):",
      round(error_rentabilidad, 4))