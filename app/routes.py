from flask import current_app as app
from flask import render_template, request, redirect, url_for
from app.utils.bissecao import metodo_bissecao, gerar_grafico_bissecao
from app.utils.newton import metodo_newton

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bissecao', methods=['GET', 'POST'])
def bissecao():
    if request.method == 'POST':
        try:
            funcao = request.form['funcao']
            a = float(request.form['a'])
            b = float(request.form['b'])
            tolerancia = float(request.form['tolerancia'])
            max_iteracoes = int(request.form['max_iteracoes'])

            raiz, iteracoes = metodo_bissecao(funcao, a, b, tolerancia, max_iteracoes)

            # 👉 Gerar gráfico após cálculo
            caminho_imagem = 'app/static/images/grafico_bissecao.png'
            gerar_grafico_bissecao(funcao, a, b, raiz, caminho_imagem)

            return render_template(
                'resultado_bissecao.html',
                raiz=raiz,
                iteracoes=iteracoes,
                funcao=funcao,
                imagem='images/grafico_bissecao.png'
            )
        except Exception as e:
            return f"Erro: {str(e)}"

    return render_template('bissecao.html')

from app.utils.newton import metodo_newton, gerar_grafico_newton

@app.route('/newton', methods=['GET', 'POST'])
def newton():
    if request.method == 'POST':
        try:
            funcao = request.form['funcao']
            x0 = float(request.form['x0'])
            tolerancia = float(request.form['tolerancia'])
            max_iteracoes = int(request.form['max_iteracoes'])

            raiz, iteracoes = metodo_newton(funcao, x0, tolerancia, max_iteracoes)

            # 👉 Novo: gerar gráfico após cálculo
            caminho_imagem = 'app/static/images/grafico_newton.png'
            gerar_grafico_newton(funcao, x0, raiz, caminho_imagem)

            return render_template(
                'resultado_newton.html',
                raiz=raiz,
                iteracoes=iteracoes,
                funcao=funcao,
                imagem='images/grafico_newton.png'
            )
        except Exception as e:
            return f"Erro: {str(e)}"

    return render_template('newton.html')

