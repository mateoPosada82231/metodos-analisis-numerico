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
    x1 = x0
    print(f"Iteración 0: x = {x0:.8f}, f(x) = {f(x0):.8e}")

    for i in range(max_iter):
        # Verificar que la derivada no sea cero
        if abs(f_prime(x1)) < 1e-12:
            print("La derivada es muy pequeña o cero. El método puede no converger.")
            return None

        # Aplicar la fórmula de Newton-Raphson
        x2 = x1 - f(x1) / f_prime(x1)
        print(f"Iteración {i + 1}: x = {x2:.8f}, f(x) = {f(x2):.8e}")

        # Verificar el criterio de convergencia
        if abs(x2 - x1) <= tol:
            print(f"\n✓ Raíz encontrada: x = {x2:.8f} en {i + 1} iteraciones")
            print(f"✓ Verificación: f(x) = {f(x2):.2e}")
            return x2

        x1 = x2

    print("No se alcanzó la convergencia.")
    return None


# Ejecutar el método
if __name__ == "__main__":
    print("Método de Newton-Raphson - Derivada Automática")
    print("=" * 50)
    newton_raphson(f, f_prime, x0, tol=error, max_iter=max_iter)
