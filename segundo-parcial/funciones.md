# Funciones — Segundo parcial

Documentación de las 32 funciones de `funciones.py`, para Teoría de la Información y la Comunicación.

## Convenciones

- **A**: entrada del canal. **B**: salida del canal.
- `probabilidades_a_priori[i]` representa P(aᵢ).
- `matriz_canal[i][j]` representa P(bⱼ | aᵢ): **filas = entradas, columnas = salidas**.
- Los alfabetos se ordenan según la primera aparición de cada símbolo, no alfabéticamente.
- Las funciones del canal usan logaritmos en base 2 y expresan las entropías en bits y la capacidad en bits por uso del canal. `informacion` y `calcular_entropia` permiten cambiar la base con `r`. El rendimiento y la redundancia son cocientes sin unidades.
- Para codificación, cada probabilidad debe corresponder a la palabra ubicada en la misma posición. `r` es el tamaño del alfabeto del código, no la cantidad de símbolos de la fuente. En un código binario, `r = 2`.
- Se conservan los nombres de tu código: **ruido = H(A | B)** y **pérdida = H(B | A)**. Conviene identificar siempre la fórmula, porque estos nombres pueden variar entre materiales.
- Salvo validaciones puntuales, las funciones suponen matrices rectangulares, no vacías, con probabilidades válidas y filas que suman 1. El vector a priori debe tener una probabilidad por entrada y sumar 1.

## Índice de funciones

1. `mostrar_matriz`
2. `informacion`
3. `calcular_entropia`
4. `rendimiento`
5. `redundancia`
6. `obtener_longitudes`
7. `calcular_longitud_media`
8. `obtener_probabilidades_a_priori`
9. `obtener_matriz_canal`
10. `obtener_probabilidades_salida`
11. `obtener_matriz_a_posteriori`
12. `obtener_matriz_simultaneos`
13. `obtener_entropia_a_priori`
14. `obtener_entropias_a_posteriori`
15. `obtener_ruido`
16. `obtener_perdida`
17. `obtener_informacion_mutua`
18. `obtener_entropia_afin`
19. `verifica_sin_ruido`
20. `verifica_determinante`
21. `obtener_matriz_canal_compuesto`
22. `verificar_reduccion_suficiente`
23. `obtener_canal_determinista`
24. `obtener_canal_reducido`
25. `verifica_uniforme`
26. `obtener_capacidad`
27. `estimar_capacidad_canal_binario`
28. `obtener_probabilidad_error`
29. `obtener_extension`
30. `obtener_codigo_huffman`
31. `tasa_compresion`
32. `extension_verifica_Shannon`

## 1. `mostrar_matriz(matriz)`

**Recibe:** una matriz de valores numéricos.

**Hace:** imprime cada fila en una línea, separando los valores con dos espacios y mostrando tres decimales.

**Devuelve:** `None`; sirve para mostrar resultados. El formato no modifica los valores de la matriz original.

## 2. `informacion(P, r=2)`

**Recibe:** una lista de probabilidades `P` y la base del logaritmo `r` (2 por defecto).

**Hace:** calcula la información individual o autoinformación de cada suceso: `Iᵢ = log_r(1 / pᵢ)`.

**Devuelve:** una lista de números, uno por probabilidad, en el mismo orden.

**Ejemplo:** `informacion([0.5, 0.25, 0.25])` devuelve `[1.0, 2.0, 2.0]` bits. Un suceso menos probable aporta más información al ocurrir.

**Detalle del código:** para `p = 0` devuelve 0 como recurso de implementación para calcular entropías sin dividir por cero. No significa que la autoinformación teórica de un suceso imposible sea cero: esta diverge cuando p tiende a cero. El código tampoco rechaza probabilidades negativas; deben evitarse. Usar una base de codificación entera `r >= 2`.

## 3. `calcular_entropia(P, r=2)`

**Recibe:** una distribución de probabilidades y la base `r`.

**Hace:** obtiene las informaciones individuales y calcula su promedio ponderado: `H_r = Σᵢ pᵢ · log_r(1 / pᵢ)`.

**Devuelve:** un número con la entropía. En base 2 se expresa en bits.

**Ejemplo:** `calcular_entropia([0.5, 0.25, 0.25])` devuelve 1.5 bits.

Con `r = 2` calcula lo mismo que `obtener_entropia_a_priori`. Sirve para probabilidades originales, de una extensión, de salida o de cualquier distribución válida. No valida que las probabilidades sumen 1.

## 4. `rendimiento(probabilidades, codificacion, r=2)`

**Recibe:** las probabilidades, las palabras de código en el orden correspondiente y el tamaño del alfabeto de codificación `r`.

**Hace:** calcula `η = H_r / L`, donde L es la longitud media del código.

**Devuelve:** un cociente sin unidades. Para expresarlo como porcentaje, multiplicarlo por 100.

**Ejemplo:** `rendimiento([0.5, 0.25, 0.25], ['0', '10', '11'])` devuelve 1.0: el código alcanza un rendimiento del 100 %.

Para una extensión se deben pasar tanto las probabilidades de los bloques como sus códigos. No se deben combinar probabilidades originales con códigos de una extensión. Si L = 0, se produce una división por cero. No valida que el código sea unívoco.

## 5. `redundancia(probabilidades, codificacion, r=2)`

**Recibe:** los mismos parámetros que `rendimiento`.

**Hace:** calcula `R = 1 - η`.

**Devuelve:** la redundancia relativa, un número sin unidades. Se multiplica por 100 si se quiere expresar como porcentaje.

**Ejemplo:** si el rendimiento es 0.9528, la redundancia es aproximadamente 0.0472, es decir, 4.72 %.

Esta función mide redundancia relativa del código, no cuenta bits de paridad ni calcula la diferencia absoluta `L - H_r`.

## 6. `obtener_longitudes(codigo)`

**Recibe:** una lista de palabras de código, normalmente cadenas.

**Hace:** aplica `len` a cada palabra.

**Devuelve:** una lista con las longitudes en el mismo orden.

**Ejemplo:** `obtener_longitudes(['0', '10', '11'])` devuelve `[1, 2, 2]`.

En códigos binarios las longitudes son cantidades de bits. Si se pasan listas de símbolos de una extensión, cuenta los elementos de esas listas, no los bits del código Huffman. Por ejemplo, `len(['11', '00', '10'])` es 3; no es la longitud de su codificación óptima.

## 7. `calcular_longitud_media(codigo, probabilidades)`

**Recibe:** palabras de código y sus probabilidades, en el mismo orden.

**Hace:** calcula `L = Σᵢ pᵢ · longitud(códigoᵢ)`.

**Devuelve:** un número con la longitud media por símbolo codificado. Para códigos de bloques de orden N, se expresa por bloque; dividir por N para obtener la longitud media por símbolo original.

**Ejemplo:** `calcular_longitud_media(['0', '10', '11'], [0.5, 0.25, 0.25])` devuelve 1.5 bits por símbolo.

**Nombre actual:** en este archivo se llama `calcular_longitud_media`, no `obtener_longitud_media`. Los ejemplos previos que usen el segundo nombre deben actualizarse.

No valida las longitudes de las listas: si hay menos probabilidades que códigos puede producir `IndexError`; si sobran probabilidades, no las utiliza. Ambas listas deben tener la misma cantidad de elementos.

## 8. `obtener_probabilidades_a_priori(entrada)`

**Recibe:** una secuencia de símbolos, por ejemplo una cadena o una lista.

**Hace:** identifica los símbolos distintos y calcula sus frecuencias relativas:

`P(aᵢ) = cantidad de apariciones de aᵢ / cantidad total de símbolos`

**Devuelve:** `(alfabeto, probabilidades)`, dos listas con posiciones correspondientes.

**Ejemplo:** para `"ABAA"`, devuelve `(['A', 'B'], [0.75, 0.25])`.

Si la entrada está vacía, devuelve dos listas vacías.

## 9. `obtener_matriz_canal(entrada, salida)`

**Recibe:** dos secuencias de igual longitud. Los símbolos ubicados en la misma posición forman un par transmitido-recibido.

**Hace:** cuenta cada par entrada-salida y divide cada fila por la cantidad de apariciones del símbolo de entrada correspondiente:

`P(bⱼ | aᵢ) = cantidad de pares (aᵢ, bⱼ) / cantidad de apariciones de aᵢ`

**Devuelve:** `(alfabeto_entrada, alfabeto_salida, matriz)`.

**Ejemplo:** para entrada `"AABB"` y salida `"XYXX"`, los alfabetos son `['A', 'B']` y `['X', 'Y']`, y la matriz es `[[0.5, 0.5], [1.0, 0.0]]`.

**Validación:** lanza `ValueError` si las longitudes son distintas. Estima el canal a partir de las observaciones suministradas.

## 10. `obtener_probabilidades_salida(probabilidades_a_priori, matriz_canal)`

**Recibe:** P(A) y la matriz P(B | A).

**Hace:** calcula la probabilidad total de cada salida, considerando todas las entradas que pueden producirla:

`P(bⱼ) = Σᵢ P(aᵢ) · P(bⱼ | aᵢ)`

**Devuelve:** una lista con P(B), en el orden de las columnas del canal.

## 11. `obtener_matriz_a_posteriori(probabilidades_a_priori, matriz_canal)`

**Recibe:** P(A) y P(B | A).

**Hace:** aplica Bayes para conocer la probabilidad de cada entrada después de observar una salida:

`P(aᵢ | bⱼ) = P(aᵢ) · P(bⱼ | aᵢ) / P(bⱼ)`

**Devuelve:** una matriz del mismo tamaño que la del canal, donde la posición `[i][j]` contiene P(aᵢ | bⱼ).

**Atención:** conserva filas de entradas y columnas de salidas. Por eso, ahora cada **columna** de probabilidad de salida positiva suma 1. Si P(bⱼ) = 0, deja la columna en cero para evitar dividir por cero; la distribución condicionada a esa salida imposible no está definida.

## 12. `obtener_matriz_simultaneos(probabilidades_a_priori, matriz_canal)`

**Recibe:** P(A) y P(B | A).

**Hace:** calcula la probabilidad conjunta de que se transmita aᵢ y se reciba bⱼ:

`P(aᵢ, bⱼ) = P(aᵢ) · P(bⱼ | aᵢ)`

**Devuelve:** la matriz conjunta P(A, B).

La suma de toda la matriz es 1. Las sumas por fila dan P(A) y las sumas por columna dan P(B).

## 13. `obtener_entropia_a_priori(probabilidades_a_priori)`

**Recibe:** una lista de probabilidades.

**Hace:** calcula la incertidumbre promedio de esa distribución:

`H(A) = Σᵢ P(aᵢ) · log₂(1 / P(aᵢ))`

**Devuelve:** un número con la entropía en bits.

Omite probabilidades nulas, cuya contribución a la entropía es cero. Aunque el nombre diga “a priori”, también sirve para calcular H(B) si se le pasa P(B), o la entropía de una fila del canal.

## 14. `obtener_entropias_a_posteriori(probabilidades_a_priori, matriz_canal)`

**Recibe:** P(A) y P(B | A).

**Hace:** calcula cuánta incertidumbre queda sobre la entrada para cada salida particular:

`H(A | bⱼ) = Σᵢ P(aᵢ | bⱼ) · log₂(1 / P(aᵢ | bⱼ))`

**Devuelve:** una lista, con una entropía por salida.

**Diferencia importante:** devuelve los valores individuales H(A | bⱼ), todavía sin promediarlos. Para salidas imposibles devuelve cero por la convención usada en la matriz a posteriori.

## 15. `obtener_ruido(probabilidades_a_priori, matriz_canal)`

**Recibe:** P(A) y P(B | A).

**Hace:** promedia las entropías a posteriori usando las probabilidades de salida:

`H(A | B) = Σⱼ P(bⱼ) · H(A | bⱼ)`

**Devuelve:** un número con la incertidumbre promedio que queda sobre la entrada después de conocer la salida.

Si vale cero, cada salida posible permite identificar la entrada, para la distribución a priori considerada.

## 16. `obtener_perdida(probabilidades_a_priori, matriz_canal)`

**Recibe:** P(A) y P(B | A).

**Hace:** calcula la entropía de cada fila del canal y la pondera por la probabilidad de su entrada:

`H(B | A) = Σᵢ P(aᵢ) · H(B | aᵢ)`

**Devuelve:** un número con la incertidumbre promedio sobre la salida cuando se conoce la entrada.

Si cada entrada produce una única salida, vale cero.

## 17. `obtener_informacion_mutua(probabilidades_a_priori, matriz_canal)`

**Recibe:** P(A) y P(B | A).

**Hace:** resta a la incertidumbre inicial de la entrada la incertidumbre que queda después de conocer la salida:

`I(A; B) = H(A) - H(A | B)`

**Devuelve:** la información mutua en bits: cuánto informa, en promedio, la salida sobre la entrada.

También se cumple `I(A; B) = H(B) - H(B | A)` y `I(A; B) = I(B; A)`.

## 18. `obtener_entropia_afin(probabilidades_a_priori, matriz_canal)`

**Recibe:** P(A) y P(B | A).

**Hace:** calcula la entropía conjunta mediante:

`H(A, B) = H(A) + H(B | A)`

**Devuelve:** la incertidumbre asociada al par entrada-salida, en bits.

También puede obtenerse como `H(B) + H(A | B)` o aplicando la fórmula de entropía a todas las probabilidades conjuntas.

## 19. `verifica_sin_ruido(matriz_canal)`

**Recibe:** la matriz del canal.

**Hace:** verifica que cada columna tenga, como máximo, un valor positivo. Así, una salida posible no puede provenir de dos entradas distintas.

**Devuelve:** `True` si cumple la condición; `False` si alguna columna tiene más de un valor positivo.

**Ejemplo:** `[[0.5, 0.5, 0], [0, 0, 1]]` devuelve `True`. La primera entrada puede generar dos salidas, pero ninguna se confunde con las de la segunda.

Admite columnas totalmente nulas, que representan salidas imposibles. No comprueba la validez general de la matriz.

## 20. `verifica_determinante(matriz_canal)`

**Recibe:** la matriz del canal.

**Hace:** verifica que cada fila tenga, como máximo, un valor positivo. En una matriz válida, esto significa que cada entrada produce una única salida con probabilidad 1.

**Devuelve:** `True` si cumple la condición; `False` en caso contrario.

**Ejemplo:** `[[1, 0], [1, 0], [0, 1]]` devuelve `True`. Distintas entradas pueden producir la misma salida.

**Atención:** el nombre se refiere a un canal determinista; no calcula el determinante algebraico de la matriz. Tampoco rechaza filas nulas, aunque no sean distribuciones válidas.

## 21. `obtener_matriz_canal_compuesto(matriz_canal_1, matriz_canal_2)`

**Recibe:** las matrices de dos canales en cascada: A → B y B → C.

**Hace:** multiplica las matrices para obtener el canal equivalente A → C:

`P(cₖ | aᵢ) = Σⱼ P(bⱼ | aᵢ) · P(cₖ | bⱼ)`

**Devuelve:** una matriz con las entradas del primer canal y las salidas del segundo.

**Validación:** lanza `ValueError` si el número de columnas de la primera matriz no coincide con el número de filas de la segunda.

Los símbolos intermedios deben estar en el mismo orden en ambas matrices. La función verifica las dimensiones, pero no conoce las etiquetas de los símbolos.

## 22. `verificar_reduccion_suficiente(matriz_canal, columna_1, columna_2)`

**Recibe:** la matriz del canal y los índices de dos columnas diferentes, contando desde cero.

**Hace:** comprueba si ambas salidas pueden agruparse sin perder información sobre la entrada. Para ello divide cada columna por su suma y compara las columnas normalizadas. La condición equivale a que sean proporcionales.

**Devuelve:** `True` si permite agruparlas; `False` si no.

Si alguna columna es nula, devuelve `True`, porque esa salida es imposible. Las comparaciones usan `math.isclose` con `abs_tol=1e-10` y la tolerancia relativa predeterminada.

**Validación:** lanza `ValueError` si un índice está fuera de rango o se selecciona la misma columna dos veces.

## 23. `obtener_canal_determinista(matriz_canal, columna_1, columna_2)`

**Recibe:** una matriz y dos índices de columnas que permitan una reducción suficiente.

**Hace:** construye el canal determinista B → C que agrupa esas dos salidas en una. Cada salida original se asigna a exactamente una salida nueva mediante un 1.

**Devuelve:** una matriz de tamaño `m × (m - 1)`, donde `m` es la cantidad de salidas originales.

Conserva la posición de la columna de menor índice y elimina la de mayor índice, desplazando las posteriores.

**Atención:** devuelve el canal de agrupación, no el canal original ya reducido. Para obtener este último se compone la matriz original con la devuelta.

**Validación:** lanza `ValueError` si la reducción no es suficiente o los índices son inválidos.

## 24. `obtener_canal_reducido(matriz_canal)`

**Recibe:** la matriz del canal original.

**Hace:** busca pares de columnas que admitan reducción suficiente; agrupa el primer par encontrado y vuelve a buscar sobre la nueva matriz. Repite hasta que no pueda agrupar más.

**Devuelve:** la matriz reducida, con la misma cantidad de entradas y una cantidad de salidas menor o igual que la original.

Al agrupar columnas, sus probabilidades se suman fila por fila. Con proporcionalidad exacta se conserva la información mutua para cualquier distribución de entrada; en el código las comparaciones admiten tolerancia numérica.

Trabaja sobre una copia, por lo que no modifica la matriz original. No devuelve las etiquetas de las salidas agrupadas.

## 25. `verifica_uniforme(matriz_canal)`

**Recibe:** la matriz del canal.

**Hace:** ordena los valores de cada fila y verifica que todas contengan los mismos valores, aunque estén en distinto orden.

**Devuelve:** `True` si todas las filas son permutaciones de la primera, dentro de la tolerancia numérica; `False` si no.

**Ejemplo:** `[[0.8, 0.2], [0.2, 0.8]]` devuelve `True`.

Usa la definición de uniforme basada en filas permutadas. No comprueba las sumas de columnas ni que se pueda obtener una distribución uniforme de salida.

## 26. `obtener_capacidad(probabilidades_a_priori, matriz_canal)`

**Recibe:** un vector a priori y la matriz del canal. **La implementación actual no utiliza el vector a priori.**

**Objetivo:** calcular la máxima información mutua alcanzable al variar la distribución de entrada:

`C = máximo de I(A; B) sobre todas las distribuciones P(A)`

**Hace actualmente:** evalúa estos casos en orden:

| Condición | Resultado del código |
| --- | --- |
| Canal sin ruido | `log₂(cantidad_entradas)` |
| Canal determinista | `log₂(cantidad_salidas)` |
| Filas permutadas | `log₂(cantidad_salidas) - entropía de la primera fila` |
| Ninguno de los anteriores | `0` |

**Devuelve:** un número, pero no todos los casos están resueltos correctamente o por completo.

**Limitaciones a tener presentes:**

- El último `0` es un resultado provisional: no significa que el canal realmente tenga capacidad cero. La estimación binaria no se llama automáticamente.
- Para un canal determinista, la fórmula correcta cuenta las salidas **alcanzables**. Si hay columnas nulas, contar todas las columnas puede sobreestimar la capacidad.
- Que las filas sean permutaciones garantiza que sus entropías sean iguales, pero no garantiza que la salida pueda ser uniforme. La fórmula `log₂(m) - H(fila)` requiere que alguna distribución de entrada produzca esa salida uniforme. Tener, además, sumas de columnas iguales es una condición suficiente.

Por ejemplo, `[[0.8, 0.2], [0.8, 0.2]]` pasa `verifica_uniforme`, pero sus filas idénticas hacen que la salida no informe sobre la entrada: su capacidad real es 0. La fórmula usada en esta rama daría un valor positivo.

## 27. `estimar_capacidad_canal_binario(matriz_canal, paso=0.0001)`

**Recibe:** una matriz con exactamente dos entradas y un paso de búsqueda. Puede tener dos o más salidas.

**Hace:** recorre distribuciones de entrada `[p, 1-p]`, desde p = 0 hasta p = 1, calcula la información mutua de cada una y guarda la mayor.

**Devuelve:** `(capacidad, mejor_probabilidad)`.

- `capacidad`: mayor información mutua encontrada, como aproximación a la capacidad real.
- `mejor_probabilidad`: valor de p para la primera entrada. La segunda tiene probabilidad `1-p`.

Con el paso predeterminado evalúa 10 001 distribuciones. Un paso más pequeño explora más puntos y requiere más cálculos. Incluye p = 1 aunque el paso no divida exactamente a 1.

**Validación:** lanza `ValueError` si no hay exactamente dos entradas o si no se cumple `0 < paso <= 1`.

En caso de empate exacto conserva el primer valor encontrado. La aproximación puede no coincidir con el máximo exacto si este cae entre dos puntos evaluados.

## 28. `obtener_probabilidad_error(probabilidades_a_priori, matriz_canal)`

**Recibe:** P(A) y P(B | A).

**Hace:** para cada salida elige la entrada con mayor probabilidad conjunta P(aᵢ, bⱼ). Suma esas probabilidades de acierto y resta el resultado de 1:

`P(error) = 1 - Σⱼ máximoᵢ [P(aᵢ) · P(bⱼ | aᵢ)]`

**Devuelve:** la probabilidad total de error de esa regla de decisión.

**Interpretación:** para una salida de probabilidad positiva, maximizar la conjunta equivale a maximizar P(aᵢ | bⱼ), porque el denominador de Bayes es el mismo para todas las entradas candidatas. Es la regla de **máximo a posteriori (MAP)** y minimiza la probabilidad de error.

No es, en general, máxima verosimilitud: esa otra regla maximiza solamente P(bⱼ | aᵢ). Coinciden cuando las entradas son equiprobables. La función devuelve la probabilidad de error, no las decisiones elegidas para cada salida.

## 29. `obtener_extension(alfabeto, probabilidades, orden)`

**Recibe:** el alfabeto original, sus probabilidades y el orden de extensión N.

**Hace:** genera todas las secuencias posibles de N símbolos y calcula cada probabilidad como el producto de las probabilidades individuales. Supone una fuente sin memoria.

**Devuelve:** `(extension, probabilidades_extension)`. La extensión es una lista de listas; cada lista interna representa un bloque de N símbolos.

**Ejemplo:**

```python
extension, p_ext = obtener_extension(['A', 'B'], [0.75, 0.25], 2)
# extension: [['A', 'A'], ['A', 'B'], ['B', 'A'], ['B', 'B']]
# p_ext: [0.5625, 0.1875, 0.1875, 0.0625]
```

Si el alfabeto tiene m símbolos, genera `m ** N` bloques. La entropía de los bloques es `H_r(S^N) = N · H_r(S)` bajo la hipótesis de independencia.

**Atención:** genera bloques de la fuente, no sus códigos comprimidos. Para codificarlos, pasar las probabilidades devueltas a `obtener_codigo_huffman`.

Usar un orden entero positivo. El código no lo valida: para 0 o un entero negativo devuelve `([[]], [1])`; un valor no entero no es aceptado por `range`. Para órdenes grandes, la cantidad de bloques crece rápidamente.

## 30. `obtener_codigo_huffman(probabilidades)`

**Recibe:** la lista de probabilidades de los símbolos que se desea codificar. También puede recibir las probabilidades de una extensión.

**Hace:** construye un código Huffman binario. Busca los dos grupos menos probables, antepone 0 a los códigos de uno y 1 a los del otro, suma sus probabilidades y repite hasta unir todos los grupos.

**Devuelve:** una lista de cadenas binarias en el mismo orden que las probabilidades originales.

**Ejemplo:** con `[0.5, 0.25, 0.25]`, esta implementación devuelve `['0', '10', '11']`.

Huffman obtiene un código prefijo de longitud media mínima para las probabilidades proporcionadas. Los empates pueden dar otros códigos igualmente óptimos. Esta implementación usa listas y bucles; no requiere `heapq` ni otros imports.

**Casos particulares:** para una lista vacía devuelve `[]`; para un único símbolo devuelve `['']`, una palabra vacía. En este último caso L = 0 y las funciones de rendimiento y redundancia dividen por cero. Para el uso habitual, proporcionar al menos dos símbolos con probabilidades válidas.

## 31. `tasa_compresion(mensaje, codificado)`

**Recibe:** dos secuencias cuyas longitudes representan los tamaños original y comprimido.

**Hace:** calcula `TC = len(mensaje) / len(codificado)`.

**Devuelve:** la razón entre ambos tamaños. Con unidades compatibles, un valor mayor que 1 indica reducción del tamaño; 1 indica igual tamaño y un valor menor que 1 indica expansión.

**Ejemplo:** dos cadenas binarias de 16 y 10 bits dan `TC = 1.6`.

**Importante:** ambas longitudes deben medirse en la misma unidad. Si `mensaje` es texto y `codificado` es una cadena de ceros y unos, la función cuenta caracteres originales frente a bits codificados, y ese cociente no es la tasa de compresión en bits. Primero hay que calcular el tamaño original en bits según su representación (por ejemplo 7 bits por carácter ASCII estándar, u 8 si se incluye paridad). Si `codificado` está vacío, produce división por cero.

## 32. `extension_verifica_Shannon(probabilidades, palabras_codigo, N=1)`

**Recibiría:** las probabilidades de la fuente original, las palabras de código de la extensión de orden N y ese orden. Para N = 1 se pasan las palabras del código original.

**Objetivo:** comprobar la cota de codificación de fuente, expresada por símbolo original:

`H_r(S) <= L_N / N < H_r(S) + 1 / N`

**Procedimiento previsto:** calcular la entropía original en base r, generar las probabilidades de los bloques de orden N, calcular su longitud media y dividirla por N.

**Resultado previsto:** `True` o `False`. Esto solo comprueba una desigualdad numérica para el código proporcionado: no demuestra que sea unívoco ni óptimo. El teorema garantiza la existencia de un código con esa cota para una fuente sin memoria; no obliga a cualquier código a satisfacerla.

El orden de `palabras_codigo` debe coincidir con el de los bloques generados por `obtener_extension`. Para m símbolos originales se pasan m probabilidades y `m ** N` palabras de código. Usar `r = 2` para códigos Huffman generados por este archivo.


## Ejemplo de uso conjunto

```python
import funciones

p_a = [0.5, 0.5]
canal = [[0.9, 0.1], [0.1, 0.9]]

p_b = funciones.obtener_probabilidades_salida(p_a, canal)
posteriori = funciones.obtener_matriz_a_posteriori(p_a, canal)
conjunta = funciones.obtener_matriz_simultaneos(p_a, canal)

h_a = funciones.obtener_entropia_a_priori(p_a)
h_b = funciones.obtener_entropia_a_priori(p_b)
h_a_dado_b = funciones.obtener_ruido(p_a, canal)
h_b_dado_a = funciones.obtener_perdida(p_a, canal)
informacion = funciones.obtener_informacion_mutua(p_a, canal)
h_conjunta = funciones.obtener_entropia_afin(p_a, canal)

capacidad, mejor_p = funciones.estimar_capacidad_canal_binario(canal)
error = funciones.obtener_probabilidad_error(p_a, canal)
```

Para este ejemplo: P(B) = `[0.5, 0.5]`; H(A) = H(B) = 1 bit; ambas entropías condicionales son aproximadamente 0.469 bits; I(A; B) y la capacidad son aproximadamente 0.531 bits; H(A, B) es aproximadamente 1.469 bits y la probabilidad de error es 0.1.


## Ejemplo completo: codificación y extensión

Ejecutar después de corregir el bloque final del módulo como se indica arriba. Si este ejemplo está en otro archivo, `funciones.py` debe estar disponible para importar.

```python
import funciones

mensaje_bits = '1100111001111001'
mensaje = [mensaje_bits[i:i + 2] for i in range(0, len(mensaje_bits), 2)]
alfabeto, p = funciones.obtener_probabilidades_a_priori(mensaje)

# En este ejercicio los símbolos identificadores son las palabras originales.
h = funciones.calcular_entropia(p)
l = funciones.calcular_longitud_media(alfabeto, p)
eta = funciones.rendimiento(p, alfabeto)
red = funciones.redundancia(p, alfabeto)

extension, p_ext = funciones.obtener_extension(alfabeto, p, 3)
codigo_ext = funciones.obtener_codigo_huffman(p_ext)
h_ext = funciones.calcular_entropia(p_ext)
l_ext = funciones.calcular_longitud_media(codigo_ext, p_ext)
eta_ext = funciones.rendimiento(p_ext, codigo_ext)
red_ext = funciones.redundancia(p_ext, codigo_ext)
cumple = funciones.extension_verifica_Shannon(p, codigo_ext, 3)

print(f'Original: H={h:.4f}, L={l:.4f}, eta={eta:.4f}, R={red:.4f}')
print(f'Extensión: H={h_ext:.4f}, L={l_ext:.4f}, eta={eta_ext:.4f}, R={red_ext:.4f}')
print('Longitud por símbolo original:', l_ext / 3)
print('Cumple la cota de Shannon:', cumple)
```

Resultados: original H = 1.9056, L = 2.0000, η = 0.9528 y R = 0.0472. Extensión H = 5.7169 bits/bloque, L = 5.7578 bits/bloque, η = 0.9929 y R = 0.0071. La longitud por símbolo original es 1.9193 bits y la cota devuelve `True`.

## Ejemplo completo: distribución óptima y métricas del canal

```python
import funciones

canal = [[0.0, 0.0, 1.0], [0.4, 0.4, 0.2]]
capacidad, p_0 = funciones.estimar_capacidad_canal_binario(canal)
p = [p_0, 1 - p_0]

print('Probabilidades óptimas:', p)
print('Capacidad:', capacidad)
print('Equivocación H(A/B):', funciones.obtener_ruido(p, canal))
print('Pérdida H(B/A):', funciones.obtener_perdida(p, canal))
print('Información mutua:', funciones.obtener_informacion_mutua(p, canal))
print('Probabilidad de error MAP:', funciones.obtener_probabilidad_error(p, canal))
print('Canal reducido:', funciones.obtener_canal_reducido(canal))
```

Resultados aproximados: P(0) = 0.5643, P(1) = 0.4357, capacidad = 0.6182 bits/uso, H(A/B) = 0.3698 bits, H(B/A) = 0.6631 bits e información mutua = 0.6182 bits. El canal reducido es `[[0.0, 1.0], [0.8, 0.2]]`, porque se agrupan las primeras dos salidas proporcionales. Esa agrupación conserva información, pero no asigna por sí sola los bits decididos de entrada.

## Funciones que no están incluidas

Este archivo no contiene una función de detección/corrección por paridad cruzada ni una de conversión de matrices de paridad a ASCII. El bloque usado para ese ejercicio en la conversación es código aparte. Tampoco hay una función que devuelva la decisión para cada salida: `obtener_probabilidad_error` solo devuelve el error total.
