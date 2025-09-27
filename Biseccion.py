
import math

def biseccion_rapida(f, a, b, tol=1e-20, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        return None, "El intervalo no contiene una raíz o no cambia de signo", []
    historial = []
    for iter_count in range(max_iter):
        c = (a + b) * 0.5
        fc = f(c)
        error = abs(fc)
        historial.append((iter_count, a, b, c, fc, error))
        if error < tol or abs(b - a) * 0.5 < tol:
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
print("Raíz:", raiz, "\nN. Iteraciones:", iteraciones)
print("Historial (iter, a, b, c, f(c), error):")
for h in historial:
    print(h)
