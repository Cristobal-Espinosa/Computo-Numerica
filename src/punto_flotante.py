import numpy as np
import matplotlib.pyplot as plt
from cargar_datos import precios, years, meses


def redondear_cifras_significativas(numeros, cifras):
    factor = 10 ** (cifras - 1 - np.floor(np.log10(np.abs(numeros))))
    redondeo = np.round(numeros * factor) / factor
    return redondeo

valor = 1000.76

valor_2cifras = redondear_cifras_significativas(valor, 2)
valor_3cifras = redondear_cifras_significativas(valor, 3)

error_2cifras = abs(valor - valor_2cifras)
error_3cifras = abs(valor - valor_3cifras)

print("REPRESENTACION CON MANTISA CORTA")
print("Valor original:", valor)
print("2 cifras significativas:", valor_2cifras, " error:", round(error_2cifras, 2))
print("3 cifras significativas:", valor_3cifras, " error:", round(error_3cifras, 2))

monto = 1000000

dolares_ciclo = monto / precios
vuelta_ciclo = dolares_ciclo * precios
deriva = vuelta_ciclo - monto

print("\nIDA Y VUELTA")
print("Deriva por mes (deberia ser 0):")
print(deriva)
print("\nDeriva maxima:", np.max(np.abs(deriva)))

plt.figure(figsize=(10, 4))
plt.plot(deriva, marker="o")
plt.title("Deriva de la ida y vuelta en punto flotante")
plt.xlabel("Mes (indice)")
plt.ylabel("Deriva (pesos)")
plt.grid(True)
plt.savefig("graficos/deriva_ida_vuelta.png")
plt.close()

dif_float32 = np.float32(874.67) - np.float32(875.66)
dif_float64 = np.float64(874.67) - np.float64(875.66)

print("\nCANCELACION EN LA MAQUINA")
print("874.67 - 875.66 en float32:", dif_float32)
print("874.67 - 875.66 en float64:", dif_float64)
print("Diferencia entre ambos:", abs(float(dif_float32) - float(dif_float64)))