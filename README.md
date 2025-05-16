# 📊 Calculadora de Métodos Numéricos - IFPA

Aplicação web educacional desenvolvida com Python e Flask para o cálculo de raízes de funções matemáticas utilizando os métodos de **Bisseção** e **Newton-Raphson**.

> Projeto desenvolvido com fins acadêmicos no IFPA - Instituto Federal do Pará.

---

## ✨ Funcionalidades

- ✍️ Entrada de funções personalizadas (ex: `x**3 - x - 2`)
- 📌 Método da Bisseção
- 📌 Método de Newton-Raphson
- 📈 Geração automática de gráfico com a raiz aproximada
- 📋 Tabela de iterações
- 💻 Interface responsiva

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Flask**
- **SymPy**
- **NumPy**
- **Matplotlib**
- **HTML + CSS (puro)**

---

## 🚀 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/JoaoPedroCavalcante/calculadora-metodos-numericos.git

# Acesse a pasta
cd calculadora-metodos-numericos

# Crie e ative o ambiente virtual (Windows)
python -m venv venv
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
python run.py
```

Acesse no navegador: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📁 Estrutura do Projeto

```
calculadora-metodos/
├── app/
│   ├── utils/ → lógica dos métodos numéricos
│   ├── templates/ → páginas HTML
│   ├── static/
│   │   ├── css/ → estilos do site
│   │   └── images/ → gráficos gerados
├── run.py → inicia a aplicação
├── requirements.txt → dependências
└── README.md → este arquivo
```

---

## 👨‍💻 Autor

**João Pedro Cavalcante**  
📅 Projeto iniciado em 16/05/2025  
🔗 [github.com/JoaoPedroCavalcante](https://github.com/JoaoPedroCavalcante)

---

## 📄 Licença

Projeto de uso acadêmico e livre para fins educativos.
