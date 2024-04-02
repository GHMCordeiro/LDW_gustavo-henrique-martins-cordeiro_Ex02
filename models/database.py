from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Livros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    autor = db.Column(db.String(150))

    def __init__(self, titulo, ano ,autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
    