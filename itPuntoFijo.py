import math

def punto_fijo(g, x0, es=0.001, imax=20):
    """
    Método de punto fijo para encontrar raíces de una ecuación.

    Parámetros:
        g    : función g(x) para la iteración (debe estar definida antes de llamar la función)
        x0   : valor inicial (punto de arranque)
        es   : tolerancia de error (en %) -> condición de parada
        imax : número máximo de iteraciones permitidas

    Retorna:
        (xr, iteraciones, ea) -> raíz aproximada, número de iteraciones y error aproximado
    """

    xr = x0
    iterac = 0
    historial = []

    # Proceso iterativo para encontrar la raíz
    for i in range(imax):
        xrold = xr
        xr = g(xrold)
        ea = abs((xr - xrold) / xr) * 100 if xr != 0 else 0
        historial.append({'iter': i + 1, 'xr': xr, 'ea': ea})
        if ea < es:
            break

    raiz_final = xr

    # Encabezado de la tabla de resultados
    print(f"{'Iter':<5}{'xr':<15}{'ea (%)':<15}{'et (%)':<15}")
    print("-" * 50)

    # Calcular error verdadero y mostrar tabla
    for item in historial:
        et = abs((raiz_final - item['xr']) / raiz_final) * 100 if raiz_final != 0 else 0
        print(f"{item['iter']:<5}{item['xr']:<15.10f}{item['ea']:<15.10f}{et:<15.10f}")

    # Resultado final o mensaje de no convergencia
    if historial[-1]['ea'] <= es:
        print("\nResultado final:")
        print("Iteraciones:", len(historial))
        print("Raíz aproximada:", raiz_final)
        print("Error aproximado (%):", historial[-1]['ea'])
    else:
        print("\nEl método no convergió en", imax, "iteraciones")

    return raiz_final, len(historial), historial[-1]['ea']

# Nota importante:
# El método de punto fijo requiere transformar la ecuación f(x) = 0 en una forma equivalente x = g(x).
# Este paso NO puede realizarse automáticamente en el programa, porque existen muchas formas distintas
# de despejar g(x), y no todas garantizan convergencia.
#
# Ejemplo:
#   f(x) = 2*sin(sqrt(x)) - x = 0
# Puede reordenarse como:
#   g1(x) = 2*sin(sqrt(x))
# o también como:
#   g2(x) = (arcsin(x/2))^2
#
# El usuario debe realizar este despeje manualmente y decidir qué forma de g(x) utilizar.
# Una vez definido g(x), el programa aplicará la iteración x_{n+1} = g(x_n).

# Solo es pasar la x al otro lado de la ecuacion

# ============================
# 🔹 EJEMPLO DE USO
# ============================

# 1️⃣ Definir la función de iteración g(x)
#    Aquí el usuario debe escribir cómo queda la ecuación despejada.
#    Ejemplo: si la ecuación es f(x) = 2*sen(√x) - x = 0,
#    una forma de despejar es: x = 2*sen(√x), por tanto:
def g(x):
    return 2 * math.sin(math.sqrt(x))

# 2️⃣ Dar el valor inicial (x0)
#    El usuario debe elegir un valor de arranque cerca de la raíz.
x0 = 0.5

# 3️⃣ Definir la tolerancia (es) y el número máximo de iteraciones (imax)
#    es = 0.001 significa que el error permitido es 0.001 %
#    imax = 20 significa que no hará más de 20 iteraciones
es = 0.001
imax = 20

# 4️⃣ Llamar a la función punto_fijo()
punto_fijo(g, x0, es, imax)
