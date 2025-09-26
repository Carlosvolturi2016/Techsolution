from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-123')

# Dados dos serviços
servicos = [
    {
        'id': 1,
        'nome': 'Formatação de Notebook',
        'descricao': 'Formatação completa com instalação do sistema operacional de sua preferência, drivers e programas essenciais.',
        'preco': 'R$ 120,00',
        'tempo_estimado': '2-3 horas',
        'icone': 'bi-laptop'
    },
    {
        'id': 2,
        'nome': 'Atualização de Sistema Operacional',
        'descricao': 'Atualização segura para a versão mais recente do Windows, macOS ou Linux.',
        'preco': 'R$ 80,00',
        'tempo_estimado': '1-2 horas',
        'icone': 'bi-arrow-up-circle'
    },
    {
        'id': 3,
        'nome': 'Upgrade de Hardware',
        'descricao': 'Melhoria de desempenho com instalação de SSD, mais memória RAM ou outros componentes.',
        'preco': 'A partir de R$ 150,00',
        'tempo_estimado': 'Variável',
        'icone': 'bi-cpu'
    },
    {
        'id': 4,
        'nome': 'Limpeza e Manutenção',
        'descricao': 'Limpeza interna completa, troca de pasta térmica e verificação geral do sistema.',
        'preco': 'R$ 100,00',
        'tempo_estimado': '1-2 horas',
        'icone': 'bi-tools'
    }
]


@app.route('/')
def index():
    return render_template('index.html', servicos=servicos)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        servico_interesse = request.form.get('servico', '')
        mensagem = request.form['mensagem']

        # Em produção, você pode integrar com email ou banco de dados
        print(f"Novo contato recebido: {nome}, {email}, {telefone}")
        print(f"Serviço de interesse: {servico_interesse}")
        print(f"Mensagem: {mensagem}")

        flash('Sua mensagem foi enviada com sucesso! Entraremos em contato em breve.', 'success')
        return redirect(url_for('contato'))

    return render_template('contato.html', servicos=servicos)


@app.route('/servico/<int:servico_id>')
def servico_detalhe(servico_id):
    servico = next((s for s in servicos if s['id'] == servico_id), None)
    if servico:
        return render_template('servico_detalhe.html', servico=servico)
    else:
        flash('Serviço não encontrado.', 'error')
        return redirect(url_for('index'))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
