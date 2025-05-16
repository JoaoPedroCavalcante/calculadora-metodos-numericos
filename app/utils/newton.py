from sympy import symbols, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np

def metodo_newton(expressao_str, x0, tolerancia=0.0001, max_iteracoes=50):
    """
    Calcula a raiz da função usando o Método de Newton-Raphson.
    """
    x = symbols('x')
    func_expr = sympify(expressao_str)
    func_derivada = func_expr.diff(x)

    f = lambdify(x, func_expr, modules=['numpy'])
    f_derivada = lambdify(x, func_derivada, modules=['numpy'])

    iteracoes = []
    xn = x0

    for i in range(max_iteracoes):
        fxn = f(xn)
        fpxn = f_derivada(xn)
        iteracoes.append((i+1, xn, fxn, fpxn))

        if abs(fxn) < tolerancia:
            return xn, iteracoes

        if fpxn == 0:
            raise ValueError("Derivada zero! Método de Newton falhou.")

        xn = xn - fxn / fpxn

    return xn, iteracoes

def gerar_grafico_newton(funcao_str, x0, raiz, caminho_imagem):
    """
    Gera um gráfico da função perto do chute inicial e marca a raiz aproximada.
    """
    x = symbols('x')
    func_expr = sympify(funcao_str)
    f = lambdify(x, func_expr, modules=['numpy'])

    intervalo = 5  # largura do intervalo em torno de x0
    x_vals = np.linspace(x0 - intervalo, x0 + intervalo, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(8, 6))
    plt.axhline(0, color='black', linewidth=0.8)
    plt.plot(x_vals, y_vals, label=f'f(x) = {funcao_str}')
    plt.scatter(raiz, f(raiz), color='red', zorder=5, label=f'Raiz ≈ {raiz:.4f}')
    plt.title('Método de Newton-Raphson')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.savefig(caminho_imagem)
    plt.close()
