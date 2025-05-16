from sympy import symbols, sympify, lambdify

def metodo_bissecao(expressao_str, a, b, tolerancia=0.0001, max_iteracoes=50):
    """
    Calcula a raiz da função usando o Método da Bisseção.
    """
    x = symbols('x')
    func_expr = sympify(expressao_str)  # Converte string em expressão simbólica
    f = lambdify(x, func_expr, modules=['numpy'])

    if f(a) * f(b) >= 0:
        raise ValueError("f(a) e f(b) devem ter sinais opostos (existe raiz no intervalo).")

    iteracoes = []
    for i in range(max_iteracoes):
        c = (a + b) / 2
        fc = f(c)
        iteracoes.append((i+1, a, b, c, fc))

        if abs(fc) < tolerancia or (b - a) / 2 < tolerancia:
            return c, iteracoes

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return c, iteracoes  # Retorna última aproximação se não convergir antes

import matplotlib.pyplot as plt
import numpy as np

def gerar_grafico_bissecao(funcao_str, a, b, raiz, caminho_imagem):
    """
    Gera um gráfico da função no intervalo [a, b] e marca a raiz aproximada.
    """
    x = symbols('x')
    func_expr = sympify(funcao_str)
    f = lambdify(x, func_expr, modules=['numpy'])

    x_vals = np.linspace(a, b, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(8, 6))
    plt.axhline(0, color='black', linewidth=0.8)  # linha do eixo x
    plt.plot(x_vals, y_vals, label=f'f(x) = {funcao_str}')
    plt.scatter(raiz, f(raiz), color='red', zorder=5, label=f'Raiz ≈ {raiz:.4f}')
    plt.title('Método da Bisseção')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.savefig(caminho_imagem)
    plt.close()
