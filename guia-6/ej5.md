## Ejercicio 5

Se mantiene el canal binario cuya salida siempre coincide con la entrada, pero ahora las probabilidades a priori son:

$$
P(a_0)=0.2,\qquad P(a_1)=0.8
$$

### Matriz del canal

La matriz no cambia, porque el comportamiento del canal sigue siendo el mismo. Con entradas en filas y salidas en columnas:

$$
M=
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}
$$

### Probabilidades de salida

Aplicando el teorema de la probabilidad total:

$$
P(b_0)=P(b_0\mid a_0)P(a_0)+P(b_0\mid a_1)P(a_1)
$$

$$
P(b_0)=1\cdot0.2+0\cdot0.8=0.2
$$

$$
P(b_1)=P(b_1\mid a_0)P(a_0)+P(b_1\mid a_1)P(a_1)
$$

$$
P(b_1)=0\cdot0.2+1\cdot0.8=0.8
$$

La distribución de salida coincide con la distribución de entrada.

### Probabilidades a posteriori

Aplicando la ley de Bayes:

$$
P(a_i\mid b_j)=\frac{P(b_j\mid a_i)P(a_i)}{P(b_j)}
$$

Para la salida 0:

$$
P(a_0\mid b_0)=\frac{1\cdot0.2}{0.2}=1
$$

$$
P(a_1\mid b_0)=\frac{0\cdot0.8}{0.2}=0
$$

Para la salida 1:

$$
P(a_0\mid b_1)=\frac{0\cdot0.2}{0.8}=0
$$

$$
P(a_1\mid b_1)=\frac{1\cdot0.8}{0.8}=1
$$

Al observar la salida, seguimos conociendo con certeza cuál fue la entrada.

### Probabilidades de eventos simultáneos

Utilizamos:

$$
P(a_i,b_j)=P(a_i)P(b_j\mid a_i)
$$

Por lo tanto:

$$
P(a_0,b_0)=0.2\cdot1=0.2
$$

$$
P(a_0,b_1)=0.2\cdot0=0
$$

$$
P(a_1,b_0)=0.8\cdot0=0
$$

$$
P(a_1,b_1)=0.8\cdot1=0.8
$$

La matriz conjunta, con entradas en filas y salidas en columnas, es:

$$
P(A,B)=
\begin{pmatrix}
0.2 & 0\\
0 & 0.8
\end{pmatrix}
$$

### Comparación con el ejercicio anterior

| Magnitud | Ejercicio 4 | Ejercicio 5 |
|---|---|---|
| Probabilidades de entrada | 0.5 y 0.5 | 0.2 y 0.8 |
| Probabilidades de salida | 0.5 y 0.5 | 0.2 y 0.8 |
| Matriz del canal | Identidad | Identidad |
| Probabilidades a posteriori | Certeza sobre la entrada | Certeza sobre la entrada |
| Probabilidades conjuntas de los pares (0,0) y (1,1) | 0.5 y 0.5 | 0.2 y 0.8 |
| Probabilidad de error | 0 | 0 |

Cambian las probabilidades de salida y las probabilidades conjuntas, porque ahora el símbolo 1 se envía con mayor frecuencia.

La matriz del canal y las probabilidades a posteriori no cambian: la salida sigue identificando exactamente el símbolo enviado.

La probabilidad de error continúa siendo nula:

$$
P_E=P(a_0,b_1)+P(a_1,b_0)=0
$$