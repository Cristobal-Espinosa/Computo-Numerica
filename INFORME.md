Nombres: Cristóbal Espinosa Garrido y Steven Cifuentes Luengo

Repositorio: https://github.com/Cristobal-Espinosa/Evaluacion1_CristobalEspinosa_StevenCifuentes_Computacion_Numerica.git

1.Cuándo conviene comprar (Mes más barato)

El punto más bajo de la serie se observa en los precios de febrero, mayo y junio de 2023 ($798,26; $798,64 y $799,87, respectivamente) difieren entre sí por menos de 2 pesos, un margen comparable al error de redondeo en esos mismos meses (entre 0,13 y 1,74), por lo que no es posible determinar con certeza cuál de los tres corresponde al mínimo real de la serie. Marzo, en cambio, no forma parte de esta agrupación: el salto de febrero a marzo (+11,24) y los movimientos posteriores hacia abril y mayo (-5,66 y -5,2) superan claramente el margen de error, por lo que la variación en ese tramo no puede considerarse mínima en su totalidad. Solo el paso de mayo a junio (+1,23) sí corresponde a una variación despreciable.

2.Cuándo conviene vender (Mes más caro)

El precio pico máximo se registra en enero de 2025 (aprox $1.001), configurando un máximo distinguible aunque ajustado: supera a diciembre de 2024 (aprox $982) por unos 19 pesos, diferencia que excede el error absoluto promedio (aprox 2 a 4 pesos). Sin embargo, la brecha frente a noviembre y diciembre de 2024 es acotada en comparación con la incertidumbre acumulada de los datos.

3.La mejor jugada completa
Operación: Comprar en febrero de 2023 (o en algún mes vecino dentro de la meseta de mínimos) y vender en enero de 2025. Rentabilidad estimada: Esta estrategia arroja una rentabilidad aproximada del 25,4%, correspondiente al pico máximo observado en la gráfica de rentabilidad acumulada, cuyo error asociado es reducido en términos relativos, aunque difícil de acotar con precisión visual. Evaluación: Pese a que esta cifra es numéricamente significativa y sobrepasa por amplio margen la banda de error, no constituye una recomendación sólida para proyectar a futuro, ya que corresponde a un análisis retrospectivo (backtesting). Adicionalmente, el punto inicial de compra no puede fijarse con precisión en un único mes, debido al solapamiento de los márgenes de error en la zona mínima (o "piso") del precio.

4.Tramos donde NO se puede recomendar tomar decisiones
Meses no recomendables, el tramo entre mayo y junio de 2023 (los meses de marzo y abril presentan variaciones que sí superan el margen de error, por lo que no aplica el mismo criterio de indistinguibilidad). El cambio de mayo a junio (+1,23) es marginal y queda dentro del rango de error de redondeo estimado para el período. En cambio, los tramos marzo-abril (-5,66) y abril-mayo (-5,2) se ubican levemente por sobre el límite superior del margen de error ( aprox 5 pesos), por lo que, aunque son variaciones moderadas, no corresponden a simple ruido estadístico y sí podrían reflejar un movimiento real del precio. Por lo tanto, la recomendación de cautela se limita estrictamente al tramo mayo-junio, y no al periodo marzo-junio en su conjunto.

5.Lección de método
Restar dos cantidades grandes y de magnitud similar amplifica la incertidumbre relativa del resultado, ya que el error absoluto, que permanece prácticamente constante, pasa a representar una proporción mucho mayor de una diferencia pequeña. En estos casos, la señal real queda dominada por el ruido estadístico, al punto de volverse indistinguible de él.