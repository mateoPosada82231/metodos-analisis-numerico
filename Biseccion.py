import math

def biseccion_rapida(f, a, b, tol=1e-20, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        return None, "El intervalo no contiene una raíz o no cambia de signo", []
    historial = []
    c_old = a  # Para error aproximado
    for iter_count in range(max_iter):
        c = (a + b) * 0.5
        fc = f(c)
        error_abs = abs(fc)

        # Error aproximado porcentual
        error_aprox = abs((c - c_old) / c) * 100 if c != 0 else 0

        historial.append([iter_count + 1, a, b, c, fc, error_abs, error_aprox, 0]) # Añadir espacio para error verdadero
        c_old = c

        if error_abs < tol or abs(b - a) * 0.5 < tol:
            return c, iter_count + 1, historial
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) * 0.5, max_iter, historial

# Ejemplo de uso
def f(x):
    return x**3 - 3*x**2*math.exp(-x)+3*x*math.exp(-2*x)-math.exp(-3*x)

raiz, iteraciones, historial = biseccion_rapida(f, 0, 1)

# Calcular error verdadero usando la raíz encontrada como valor real
if raiz is not None:
    for h in historial:
        raiz_iteracion = h[3]
        error_verdadero = abs((raiz - raiz_iteracion) / raiz) * 100 if raiz != 0 else 0
        h[7] = error_verdadero # Actualizar el valor en el historial

print("Raíz:", raiz, "\nN. Iteraciones:", iteraciones)
print("\nErrores mostrados:")
print("- Error Absoluto: abs(f(c))")
print("- Error Aproximado: Cambio porcentual entre iteraciones de 'c'.")
print("- Error Verdadero: Error porcentual respecto a la raíz final encontrada.")

print(f"\n{'Iter':<5}{'a':<12}{'b':<12}{'c (Raíz apr.)':<15}{'f(c)':<12}{'Err. Abs.':<12}{'Err. Aprox.(%)':<15}{'Err. Verd.(%)':<15}")
print("-" * 110)
for h in historial:
    print(f"{h[0]:<5}{h[1]:<12.2e}{h[2]:<12.2e}{h[3]:<15.2e}{h[4]:<12.2e}{h[5]:<12.2e}{h[6]:<15.2e}{h[7]:<15.2e}")
