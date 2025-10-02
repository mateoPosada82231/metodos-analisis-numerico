import math

def f(x):
    return x**3 - 3*x**2*math.exp(-x)+3*x*math.exp(-2*x)-math.exp(-3*x)

# Valores iniciales
xl = 0      # límite inferior
xu = 1      # límite superior
es = 1e-20   # tolerancia (%)
imax = 15   # número máximo de iteraciones

# Verificar si existe raíz en el intervalo
if f(xl) * f(xu) > 0:
    print("⚠️ No hay raíz en el intervalo dado")
else:
    xr = xl
    ea = 100
    itr = 0
    fl = f(xl)

    print(f"{'Iter':<5}{'xl':<10}{'xu':<10}{'xr':<12}{'f(xr)':<12}{'ea (%)':<10}")
    print("-"*60)

    while (itr < imax and ea > es):
        xrold = xr
        xr = (xl + xu) / 2
        fr = f(xr)
        itr += 1

        if xr != 0 and itr > 1:   # evitar cálculo de error en la primera iteración
            ea = abs((xr - xrold) / xr) * 100

        # Mostrar valores de la iteración
        print(f"{itr:<5}{xl:<10.5f}{xu:<10.5f}{xr:<12.5f}{fr:<12.5f}{ea:<10.5f}")

        test = fl * fr
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
            fl = fr
        else:
            ea = 0
    print("el error que se muestra es error aproximado")
    print("\nResultado final:")
    print("Raíz aproximada =", xr)
    print("Iteraciones =", itr)
    print("Error aproximado (%) =", ea)

