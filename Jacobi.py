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
def jacobi(a, b, n, x0, es, imax):
    """
    Resuelve el sistema Ax = b usando el método iterativo de Jacobi.
    
    Parámetros:
        a    : matriz de coeficientes (nxn)
        b    : vector de resultados
        n    : número de incógnitas
        x0   : vector inicial de aproximaciones
        es   : tolerancia de error (%) para detener la iteración
        imax : número máximo de iteraciones
    """

    # 1️⃣ Verificar que el sistema tiene solución única
    if np.linalg.det(a) == 0:
        print("❌ El sistema no tiene solución única (determinante = 0).")
        return None
    
    # 2️⃣ Verificar convergencia
    verificar_diag_dom(a, n)

    # 3️⃣ Inicialización de variables
    x = x0.copy()      # vector de aproximaciones inicial
    iteracion = 0
    ea = 100           # error inicial muy grande

    # 4️⃣ Encabezado de tabla de iteraciones
    print(f"\n{'Iter':<5}{'Valores de x':<40}{'Error (%)':<15}")
    print("-"*65)

    # ===========================
    # 5️⃣ Bucle principal de iteraciones
    # ===========================
    while ea > es and iteracion < imax:
        x_new = np.zeros_like(x, dtype=float)  # vector para guardar nuevos valores

        # 🔹 Calcular cada componente x_i usando Jacobi
        for i in range(n):
            suma = b[i]
            for j in range(n):
                if i != j:
                    suma -= a[i][j] * x[j]
            x_new[i] = suma / a[i][i]  # fórmula de Jacobi

        # 🔹 Calcular error relativo máximo entre iteraciones
        ea = max(abs((x_new[i] - x[i]) / x_new[i]) * 100 if x_new[i] != 0 else 0 for i in range(n))

        # 🔹 Mostrar resultados de la iteración
        print(f"{iteracion+1:<5}{str(x_new):<40}{ea:<15.6f}")

        # 🔹 Preparar vector para siguiente iteración
        x = x_new
        iteracion += 1

    # 6️⃣ Mostrar resultados finales
    print("\nResultado final:")
    print("Iteraciones:", iteracion)
    print("Vector solución aproximada:", x)
    print("Error aproximado (%):", ea)


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

# Llamada al método de Jacobi
jacobi(a, b, n, x0, es, imax)
