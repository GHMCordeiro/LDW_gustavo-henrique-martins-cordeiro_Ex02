from flask import render_template, request, redirect, url_for
from models.database import db, Livros
import urllib
import json

leitores = []
livros = []
livros_list = [{'Título' : 'Harry Potter e a pedra filosofal', 'Ano' : 1997, 'Autor' : 'J. K. Rowling'}]

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/livros', methods=['GET', 'POST'])
    def books():
        
        if request.method == 'POST':
            if request.form.get('leitor'):
                leitores.append(request.form.get('leitor'))
                
            if request.form.get('livro'):
                livros.append(request.form.get('livro'))
            
        return render_template('livros.html', leitores=leitores, livros=livros)
    
    @app.route('/cadLivros', methods=['GET', 'POST'])
    def cadBook():

        if request.method == 'POST':
            newbook = Livros(request.form.get('titulo'), request.form.get('ano'), request.form.get('autor'))
            db.session.add(newbook)
            db.session.commit()
            return redirect(url_for('cadBook'))

        else:
            livros_list = Livros.query.all()   
            return render_template('cadLivros.html', livros_list=livros_list)