from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint

db = SQLAlchemy()

class Rota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    passageiros = db.relationship('Passageiro', backref='rota', lazy=True)

class Passageiro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    documento = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    rota_id = db.Column(db.Integer, db.ForeignKey('rota.id'), nullable=False)

    __table_args__ = (
        UniqueConstraint('nome', 'documento', name='unique_passageiro_doc'),
    )
