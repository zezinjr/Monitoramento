from flask import Flask, render_template, request, redirect
from models import db, Passageiro, Rota

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    passageiros = Passageiro.query.all()
    rotas = Rota.query.all()

    status_counts = {
        'Embarcado': Passageiro.query.filter_by(status='Embarcado').count(),
        'Em rota': Passageiro.query.filter_by(status='Em rota').count(),
        'Desembarcado': Passageiro.query.filter_by(status='Desembarcado').count()
    }

    return render_template('index.html', passageiros=passageiros, rotas=rotas, status_counts=status_counts)

@app.route('/add', methods=['POST'])
def add_passageiro():
    nome = request.form['nome']
    documento = request.form['documento']
    status = request.form['status']
    rota_id = request.form['rota_id']
    novo = Passageiro(nome=nome, documento=documento, status=status, rota_id=rota_id)
    db.session.add(novo)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update_passageiro(id):
    passageiro = Passageiro.query.get(id)
    passageiro.status = request.form['status']
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_passageiro(id):
    passageiro = Passageiro.query.get(id)
    db.session.delete(passageiro)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
