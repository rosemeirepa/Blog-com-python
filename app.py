from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

# Mock do banco de dados
posts = [
    {
        "title": "O meu Primeiro Post",
        "body": "Aqui é o texto do Post",
        "author": "Rose",
        "created": datetime(2022,7,25)
    },
    {
        "title": "O meu Segundo Post",
        "body": "Aqui é o texto do Post",
        "author": "Meire",
        "created": datetime(2022,7,26)
    },
]

# Criação de rota para a aplicação - Comando route tb permite a criação de uma função (o @ é uma marcação para a rota)
@app.route("/")
def index():
    return render_template("index.html", posts=posts)
