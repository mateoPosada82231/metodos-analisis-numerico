import numpy as np

# ==========================
# Verificaciones
# ==========================
def verificar_determinante(a):
    """Verifica que el determinante de A sea distinto de 0"""
    det = np.linalg.det(np.array(a))
    if abs(det) < 1e-12:  # tolerancia para redondeos numéricos
        print("❌ El determinante es 0: el sistema no tiene solución única")
        return False
    else:
        print(f"✅ Determinante distinto de 0: {det:.6f}")
        return True


def verificar_diag_dom(a,n):
    """Verifica si la matriz es diagonal dominante"""
    diag_dom = True
    for i in range(n):
        suma = sum(abs(a[i][j]) for j in range(n) if i != j)
        if abs(a[i][i]) < suma:
            diag_dom = False
    if diag_dom:
        print("✅ La matriz es diagonal dominante")
    else:
        print("⚠️ La matriz NO es diagonal dominante (puede no converger)")
    return diag_dom

# ==========================
# Propiedades equivalentes de una matriz definida positiva:
#
# 1. Todos los valores propios de A son positivos.
#    λ_i > 0   ∀ i
#
# 2. Todos los menores principales son positivos.
#    Es decir, los determinantes de las submatrices superiores izquierdas son positivos.
#
# 3. Existe la factorización de Cholesky.
#    Si A = L * L^T (con L triangular inferior), entonces A es definida positiva.
# ==========================

def verificar_def_pos(a):
    """Verifica si la matriz es definida positiva"""
    A = np.array(a)
    try:
        np.linalg.cholesky(A)
        print("✅ La matriz es definida positiva")
        return True
    except np.linalg.LinAlgError:
        print("⚠️ La matriz NO es definida positiva")
        return False


# ==========================
# Normalización de la matriz
# ==========================
def normalizar(a,b):
    """Normaliza la diagonal principal a 1"""
    n = len(a)
    a_norm = [[0]*n for _ in range(n)]
    b_norm = b[:]
    for i in range(n):
        pivote = a[i][i]
        for j in range(n):
            a_norm[i][j] = a[i][j] / pivote
        b_norm[i] = b[i] / pivote
    return a_norm, b_norm


# ==========================
# Tipos de relajación
#  Relajación subrelajada (0<ω<1):
#  Se da menos peso al valor nuevo, más al viejo → puede estabilizar el método si diverge, pero suele hacerlo más lento.
#  Sin relajación (𝜔=1):
#  Es el Gauss-Seidel normal.
#  Relajación sobrerrelajada (1<ω<2):
#  Se da más peso al valor nuevo → puede acelerar la convergencia si el sistema es adecuado, pero también puede provocar divergencia si el 
# 𝜔 elegido no es apropiado.
# Gauss-Seidel con relajación la relajacion es una técnica que se introduce para mejorar la convergencia del método iterativo cuando se resuelven sistemas de ecuaciones lineales.
# ==========================

# Por lo general se deja la relajacion en 1

def gauss_seidel(a,b,n,x,es,relajacion,imax, x_true=None):
    iteracion = 0
    ea = float("inf")
    convergidas = [False] * n  # Para rastrear la convergencia de cada variable
    primer_convergida_info = None

    # Encabezado de la tabla
    header_vars = "".join([f'x{i+1:<11}' for i in range(n)])
    header_errs = "".join([f'Era{i+1}(%){"":<8}' for i in range(n)])
    print(f"\n{'Iter':<6}{header_vars}{header_errs}{'Era max(%)':<12}")
    print("-" * (6 + n*24 + 12))


    while ea > es and iteracion < imax:
        x_old = x.copy()
        for i in range(n):
            suma = b[i]
            for j in range(n):
                if i != j:
                    suma -= a[i][j] * x[j]
            # actualización con relajación
            x[i] = relajacion*suma + (1-relajacion)*x_old[i]

        # calcular error como máximo relativo entre componentes (Error Aproximado)
        errores = [abs((x[i]-x_old[i])/x[i])*100 if x[i]!=0 else 0 for i in range(n)]
        ea = max(errores)

        # Verificar convergencia individual
        for i in range(n):
            if not convergidas[i] and errores[i] < es:
                convergidas[i] = True
                if primer_convergida_info is None:
                    primer_convergida_info = (i, iteracion + 1)

        iteracion += 1

        # Imprimir resultados de la iteración
        fila_vars = "".join([f'{val:<12.6f}' for val in x])
        fila_errs = "".join([f'{err:<15.6f}' for err in errores])
        print(f"{iteracion:<6}{fila_vars}{fila_errs}{ea:<12.6f}")

    # Imprimir mensajes de convergencia
    if primer_convergida_info:
        var_idx, it = primer_convergida_info
        print(f"\n🔔 La variable x[{var_idx+1}] fue la primera en converger en la iteración {it}.")

    if all(convergidas):
        print("✅ Todas las variables convergieron antes del máximo de iteraciones.")
    elif iteracion >= imax:
        print(f"\n⚠️ Se alcanzó el máximo de {imax} iteraciones. El método no convergió al criterio de error de {es}%.")
    else:
        # Esto puede pasar si el error máximo converge pero no todas las variables individualmente
        print("\n⚠️ El método finalizó, pero no todas las variables alcanzaron el criterio de error individualmente.")


    return x


# ==========================
# Ejemplo
# ==========================
imax = 100
es = 1e-6  # tolerancia en %
relajacion = 1  # 1 = Gauss-Seidel clásico

# Matriz A
a = [
    [10, 2, -1],
    [-3, -6, 2],
    [1, 1, 5]
]
# Vector b
b = [27, -61.5, -21.5]

n = 3  # cantidad de ecuaciones, cambiar segun el tamaño de la matriz, ej: matriz 4x4, n = 4
x0 = [0,0,0]  # valores iniciales

print("🔎 Verificando condiciones para aplicar Gauss–Seidel...\n")
ok_det = verificar_determinante(a)
ok_diag = verificar_diag_dom(a,n)
ok_def = verificar_def_pos(a)

# Condiciones mínimas: determinante ≠ 0 y (diagonal dominante o definida positiva)
if ok_det and (ok_diag or ok_def):
    print("\n✅ Se puede aplicar Gauss–Seidel\n")

    # Calcular solución "verdadera" para comparar
    x_true = np.linalg.solve(np.array(a), np.array(b))
    print(f"Solución 'verdadera' (para cálculo de error): {x_true}\n")

    a_norm, b_norm = normalizar(a,b)
    resultado = gauss_seidel(a_norm, b_norm, n, x0, es, relajacion, imax, x_true)
    print("\nResultado final:", [round(val, 6) for val in resultado])
else:
    print("\n❌ No es seguro aplicar Gauss–Seidel con esta matriz")
