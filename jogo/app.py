from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jogo/cobrinha')
def jogo_cobrinha():
    return render_template('cobrinha.html')

# @app.route('/jogo/velha')
# def jogo_velha():
#     return render_template('velha.html')

@app.route('/jogo/memoria')
def jogo_memoria():
    return render_template('memoria.html')

@app.route('/jogo/invaders')
def jogo_invaders():
    return render_template('invaders.html')

@app.route('/jogo/breakout')
def jogo_breakout():
    return render_template('breakout.html')

@app.route('/jogo/cyber-dodge')
def jogo_cyber_dodge():
    # Nova rota web estável para carregar o jogo nativamente no HTML
    return render_template('cyber_dodge.html')

# Adicione esta rota junto com as outras no seu arquivo app.py
@app.route('/jogo/mario')
def jogo_mario():
    return render_template('mario.html')


if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
