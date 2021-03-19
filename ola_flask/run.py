from flask import Flask

app = Flask(__name__)

# Crindo um decorador
# Podemos passar parâmetros `<numero>`
# Essa é uma forma que temos de pegar um parâmetro atráves da URI
# Podemos declarar o tipo do parâmetro que será passado. Ex: `<int:numero>` - Inteiro
@app.route("/<numero>", methods=['GET','POST'])

# Criando a primeira rota
def ola(numero):
    return 'Olá, mundo! {}'.format(numero)

# Defindo a chamada desse próprio modulo
if __name__=="__main__":
    # Adicionando o modo `debug=True` a aplicação reinicia a cada alteração
    # Em produção o modo `debug=False` senão ele apresentará toda a trilha do erro
    app.run(debug=True)

# Ao rodarmos, a aplicação será aberta no navegador
# Obs.: O navegador utiliza por padrão o método GET.