from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    origem = db.Column(db.String(100))
    destino = db.Column(db.String(100))
    passageiros = db.relationship('Passageiro', backref='rota', lazy=True)

class Passageiro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    documento = db.Column(db.String(20))
    status = db.Column(db.String(50))
    rota_id = db.Column(db.Integer, db.ForeignKey('rota.id'), nullable=True)
