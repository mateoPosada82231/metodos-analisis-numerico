import numpy as np

# ===========================
# Función para verificar diagonal dominante
# ===========================
def verificar_diag_dom(a, n):
    """
    Verifica si la matriz A es diagonalmente dominante.
    Una matriz diagonalmente dominante ayuda a garantizar la convergencia del método.
    
    Parámetros:
        a : matriz de coeficientes
        n : número de incógnitas
    Retorna:
        True si es diagonal dominante, False si no
    """
    diag_dom = True
    for i in range(n):
        suma = 0
        diag = abs(a[i][i])
        for j in range(n):
            if i != j:
                suma += abs(a[i][j])
        if diag <= suma:
            diag_dom = False
    if diag_dom:
        print("✅ La matriz es diagonalmente dominante (bueno para convergencia).")
    else:
        print("⚠️ La matriz NO es diagonalmente dominante (el método podría no converger).")
    return diag_dom


# ===========================
# Método de Jacobi
# ===========================
def jacobi(a, b, n, x0, es, imax, x_true=None):
    """
    Resuelve el sistema Ax = b usando el método iterativo de Jacobi.
    
    Parámetros:
        a    : matriz de coeficientes (nxn)
        b    : vector de resultados
        n    : número de incógnitas
        x0   : vector inicial de aproximaciones
        es   : tolerancia de error (%) para detener la iteración
        imax : número máximo de iteraciones
        x_true: solución verdadera para calcular el error verdadero
    """

    # 1️⃣ Verificar que el sistema tiene solución única
    if np.linalg.det(a) == 0:
        print("❌ El sistema no tiene solución única (determinante = 0).")
        return None
    
    # 2️⃣ Verificar convergencia
    verificar_diag_dom(a, n)

    # 3️⃣ Inicialización de variables
    x = x0.copy()
    iteracion = 0
    ea = float("inf")
    convergidas = [False] * n
    primer_convergida_info = None

    # 4️⃣ Encabezado de tabla de iteraciones
    header_vars = "".join([f'x{i+1:<11}' for i in range(n)])
    header_errs = "".join([f'Era{i+1}(%){"":<8}' for i in range(n)])
    print(f"\n{'Iter':<6}{header_vars}{header_errs}{'Era max(%)':<12}")
    print("-" * (6 + n*24 + 12))

    # ===========================
    # 5️⃣ Bucle principal de iteraciones
    # ===========================
    while ea > es and iteracion < imax:
        x_old = x.copy()

        # 🔹 Calcular cada componente x_i usando Jacobi
        for i in range(n):
            suma = b[i]
            for j in range(n):
                if i != j:
                    suma -= a[i][j] * x_old[j]
            x[i] = suma / a[i][i]

        # 🔹 Calcular error relativo para cada componente (Error Aproximado)
        errores = [abs((x[i] - x_old[i]) / x[i]) * 100 if x[i] != 0 else 0 for i in range(n)]
        ea = max(errores)

        # 🔹 Verificar convergencia individual
        for i in range(n):
            if not convergidas[i] and errores[i] < es:
                convergidas[i] = True
                if primer_convergida_info is None:
                    primer_convergida_info = (i, iteracion + 1)

        iteracion += 1

        # 🔹 Mostrar resultados de la iteración
        fila_vars = "".join([f'{val:<12.6f}' for val in x])
        fila_errs = "".join([f'{err:<15.6f}' for err in errores])
        print(f"{iteracion:<6}{fila_vars}{fila_errs}{ea:<12.6f}")

    # 6️⃣ Mostrar resultados finales
    if primer_convergida_info:
        var_idx, it = primer_convergida_info
        print(f"\n🔔 La variable x[{var_idx+1}] fue la primera en converger en la iteración {it}.")

    if all(convergidas):
        print("✅ Todas las variables convergieron antes del máximo de iteraciones.")
    elif iteracion >= imax:
        print(f"\n⚠️ Se alcanzó el máximo de {imax} iteraciones. El método no convergió al criterio de error de {es}%.")
    else:
        print("\n⚠️ El método finalizó, pero no todas las variables alcanzaron el criterio de error individualmente.")

    print("\nResultado final:", [round(val, 6) for val in x])


# ===========================
# EJEMPLO DE USO
# ===========================

# Matriz de coeficientes (A)
# Cada fila corresponde a los coeficientes de una ecuación
a = np.array([
    [10, 2, -1],
    [-3, -6, 2],
    [1, 1, 5]
], dtype=float)

# Vector de resultados (b)
# Cada valor corresponde al lado derecho de cada ecuación
b = np.array([27, -61.5, -21.5], dtype=float)

# Número de incógnitas
n = 3

# Vector inicial de aproximaciones
# Generalmente se usa cero, pero se puede cambiar
x0 = np.zeros(n)

# Parámetros de control
es = 0.05   # tolerancia de error (%)
imax = 20   # número máximo de iteraciones

# Calcular la solución "verdadera" para comparar
x_true = np.linalg.solve(a, b)
print(f"Solución 'verdadera' (para cálculo de error): {x_true}\n")

# Llamada al método de Jacobi
jacobi(a, b, n, x0, es, imax, x_true)
