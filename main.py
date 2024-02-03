from flask import Flask, render_template, request
lista_nomes = list()
app = Flask(__name__)

@app.route("/")
def index():
    nome = 'JOSE DELAMARE'
    idade = 28.5
    lprodutos = ['RedBull','Cerveja','Drinks']
    return render_template("index.html",nome=nome,idade=idade, lista_prod=lprodutos)

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome  = request.form.get("nome","?")
    idade = request.form.get("idade","?") 
    apelido  = request.form.get("apelido","?")
    lista_nomes.append(nome)
    return """
        <script>
            alert('Cadastrado com sucesso!');
            window.location.href='/'
        </script>
    """
@app.route("/visualizar")
def visualizar():
    render_template("visualizar.html",lista_nomes)
    

if __name__ == "__main__":
    app.run(debug=True)