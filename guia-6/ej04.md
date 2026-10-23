## Ejercicio 4

El canal es binario, sus entradas son equiprobables y la salida siempre coincide con la entrada.

### Probabilidades a priori

$$
P(a_0)=P(a_1)=\frac{1}{2}
$$

### Matriz del canal

Las filas representan las entradas y las columnas las salidas. Como el canal no altera los símbolos:

$$
M=
\begin{pmatrix}
P(b_0\mid a_0) & P(b_1\mid a_0)\\
P(b_0\mid a_1) & P(b_1\mid a_1)
\end{pmatrix}
=
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}
$$

### Probabilidades de salida

Aplicando el teorema de la probabilidad total:

$$
P(b_0)=P(b_0\mid a_0)P(a_0)+P(b_0\mid a_1)P(a_1)
=1\cdot\frac12+0\cdot\frac12=\frac12
$$

$$
P(b_1)=P(b_1\mid a_0)P(a_0)+P(b_1\mid a_1)P(a_1)
=0\cdot\frac12+1\cdot\frac12=\frac12
$$

Las salidas también son equiprobables.

### Probabilidades a posteriori

Aplicando la ley de Bayes:

$$
P(a_i\mid b_j)=\frac{P(b_j\mid a_i)P(a_i)}{P(b_j)}
$$

Se obtiene:

$$
P(a_0\mid b_0)=1,\qquad P(a_1\mid b_0)=0
$$

$$
P(a_0\mid b_1)=0,\qquad P(a_1\mid b_1)=1
$$

Al conocer la salida, se determina con certeza cuál fue la entrada.

### Probabilidades de eventos simultáneos

Las probabilidades conjuntas se calculan mediante:

$$
P(a_i,b_j)=P(a_i)P(b_j\mid a_i)
$$

Por lo tanto:

$$
P(a_0,b_0)=\frac12,\qquad P(a_0,b_1)=0
$$

$$
P(a_1,b_0)=0,\qquad P(a_1,b_1)=\frac12
$$

La matriz de probabilidades conjuntas, con entradas en filas y salidas en columnas, es:

$$
P(A,B)=
\begin{pmatrix}
\frac12 & 0\\
0 & \frac12
\end{pmatrix}
$$

### Análisis de los resultados

El canal transmite sin errores: solo pueden ocurrir los pares entrada-salida
$(a_0,b_0)$ y $(a_1,b_1)$, cada uno con probabilidad $1/2$.

La probabilidad de error es:

$$
P_E=P(a_0,b_1)+P(a_1,b_0)=0
$$

Antes de observar la salida, las dos entradas son igualmente probables.
Después de observarla, desaparece toda incertidumbre sobre el símbolo enviado.

La entrada y la salida no son independientes, ya que:

$$
P(a_0,b_0)=\frac12
\neq P(a_0)P(b_0)=\frac14
$$