Métodos implementados
Bisección (Biseccion.py, Biseccion2.py)
Tipo: Intervalo cerrado.
Qué muestra: Iteraciones, tablas de resultados, errores.
Validaciones: Cambio de signo en el intervalo, cálculo de errores.
Aclaraciones: Requiere un intervalo [a, b] donde la función cambia de signo. Se calcula el 
error verdadero (Et) si se conoce la raíz exacta y el error aproximado (Ea) entre iteraciones.

Gauss-Seidel (Gauss-seidel.py)
Tipo: Iterativo.
Qué muestra: Soluciones del sistema, tablas de iteraciones, errores.
Validaciones: Convergencia del método, cálculo de errores.
Aclaraciones: Método para sistemas de ecuaciones lineales. Se calcula Ea entre iteraciones.

Punto Fijo (itPuntoFijo.py)
Tipo: Intervalo abierto.
Qué muestra: Iteraciones, tablas de resultados, errores.
Validaciones: Convergencia del método, cálculo de errores.
Aclaraciones: Solo requiere un valor inicial. Se calcula Et si se conoce la raíz y Ea entre iteraciones.

Jacobi (Jacobi.py)
Tipo: Iterativo.
Qué muestra: Soluciones del sistema, tablas de iteraciones, errores.
Validaciones: Convergencia del método, cálculo de errores.
Aclaraciones: Método para sistemas de ecuaciones lineales. Se calcula Ea entre iteraciones.

Newton-Raphson (Newton-Raphson.py)
Tipo: Intervalo abierto.
Qué muestra: Iteraciones, tablas de resultados, errores.
Validaciones: Verifica la derivada, cálculo de errores.
Aclaraciones: Solo requiere un valor inicial. Se calcula Et si se conoce la raíz y Ea entre iteraciones.
Aclaraciones generales
Et: Error verdadero (si se conoce la raíz exacta).
Ea: Error aproximado (entre iteraciones).
Intervalo cerrado: Requiere [a, b] y cambio de signo.
Intervalo abierto: Solo requiere un valor inicial.

**Fórmulas de errores:**

- Error verdadero \(Et\): \(Et = x_{verdadero} - x_{aproximado}\)
- Error relativo verdadero \(E_{rt}\): \(E_{rt} = \frac{|x_{verdadero} - x_{aproximado}|}{|x_{verdadero}|}\)
- Error aproximado \(Ea\): \(Ea = x_{actual} - x_{anterior}\)
- Error relativo aproximado \(E_{ra}\): \(E_{ra} = \frac{|x_{actual} - x_{anterior}|}{|x_{actual}|}\)