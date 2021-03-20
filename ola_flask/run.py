from flask import Flask
app = Flask(__name__)

# Crindo um decorador
@app.route("/<numero>", methods=['GET','POST'])

# Criando a primeira rota
def ola(numero):
    return 'Olá, mundo! {}'.format(numero)

# Defindo a chamada desse próprio modulo
if __name__=="__main__":
    app.run(debug=True)
