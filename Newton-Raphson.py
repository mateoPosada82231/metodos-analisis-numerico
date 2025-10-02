# -*- coding: utf-8 -*-
"""
Implementación simplificada del Método de Newton-Raphson en Python

Ahora la derivada se calcula automáticamente con sympy

Definir la función, valor inicial y tolerancia en las siguientes líneas:
f = lambda x: x**3 + x - 1  # <-- Cambia aquí tu función
x0 = 1.0                    # <-- Cambia aquí tu valor inicial
error = 1e-6                # <-- Cambia aquí tu tolerancia
"""
import math

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify, exp


# Definir la función usando sympy.exp para compatibilidad con sympy
definir_funcion = lambda x: x**3 - 3*x**2*exp(-x)+3*x*exp(-2*x)-exp(-3*x)  # <-- Cambia aquí tu función
x0 = 1.0  # <-- Cambia aquí tu valor inicial
error = 1e-8  # <-- Cambia aquí tu tolerancia
max_iter = 100


# Derivada automática con sympy
def obtener_derivada(func):
    x = symbols('x')
    f_expr = func(x)
    f_prime_expr = diff(f_expr, x)
    f_prime = lambdify(x, f_prime_expr, 'numpy')
    return f_prime


# Convertir la función a formato evaluable por numpy
f = lambdify(symbols('x'), definir_funcion(symbols('x')), 'numpy')
f_prime = obtener_derivada(definir_funcion)


def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    x_current = x0
    historial = []
    ea = 100  # Error aproximado inicial

    for i in range(max_iter):
        x_old = x_current

        f_prime_val = f_prime(x_old)
        if abs(f_prime_val) < 1e-12:
            print("La derivada es muy pequeña o cero. El método no convergerá.")
            break

        x_current = x_old - f(x_old) / f_prime_val

        ea = abs((x_current - x_old) / x_current) * 100 if x_current != 0 else 0

        historial.append({'iter': i + 1, 'x': x_current, 'fx': f(x_current), 'ea': ea})

        if ea < tol:
            break

    raiz_final = x_current

    print(f"\n{'Iter':<5}{'x':<20}{'f(x)':<15}{'Err. Aprox.(%)':<20}{'Err. Verd.(%)':<20}")
    print("-" * 85)

    if raiz_final is not None:
        for item in historial:
            et = abs((raiz_final - item['x']) / raiz_final) * 100 if raiz_final != 0 else 0
            print(f"{item['iter']:<5}{item['x']:<20.10f}{item['fx']:<15.4e}{item['ea']:<20.10f}{et:<20.10f}")

    if ea <= tol:
        print(f"\n✓ Raíz encontrada: x = {raiz_final:.8f} en {len(historial)} iteraciones")
        print(f"✓ Error aproximado final: {ea:.10f}%")
        print(f"✓ Verificación: f(x) = {f(raiz_final):.2e}")
    else:
        print(f"\n❌ No se alcanzó la convergencia en {max_iter} iteraciones.")

    return raiz_final


# Ejecutar el método
if __name__ == "__main__":
    print("Método de Newton-Raphson - Derivada Automática")
    print("=" * 50)
    newton_raphson(f, f_prime, x0, tol=error, max_iter=max_iter)
