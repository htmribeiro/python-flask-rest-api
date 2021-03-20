# Desenvolvimento Avançado Python com Flask e REST API

## Módulo 02 - REST API com Flask [Ambiente]

#### Agenda

* PIP

* Instalando Flask

* Criando um ambiente virtual (VirtualEnv)

* Primeira aplicação Flask

* Entendendo os decoradores

* introdução a Postman para realizar requisições HTTP

#### O que utilizaremos

* [Python 3.7](https://python.org)

* [Pycharm](https://www.jetbrains.com/pycharm/download) Community

* [Flask](https://wwww.flask.pocoo.org)

* [postman](https://www.getpostman.com/downloads/)

### PIP

* Sistema de gerenciamento de pacotes

* Utilizado para instalar e gerenciar pacotes/bibliotecas em Python

* Já vem empacotado com Python desde a versão 3.4

```code
> pip install Flask
```

### Virtualenv

* Ferramenta para criar ambientes Python isolados

* Vem integrado com o Python desde a versão 3.3

* Extremamente útil para se trabalhar com projetos que utilizam bibliotecas com versões diferentes.

>```ps
> PS D:\users\hbtechcompany> python -m venv .\.virutalenvs\minha_virtualenv
> PS D:\users\hbtechcompany> .\.virtualenv\minha_virualenv\Scripts\activate
> (minha_virualenv) > PS D:\users\hbtechcompany> pip install Flask
>```

### Pycharm

* IDE para desenvolvimento Python

* Robusta e torna o desnevolvimento muito mais rápido

* Possui versão paga e versão gratuíta (community)

### Postman

* Ferramenta utilizada para realizar requisições HTTP

* Com ela é possível chamar qualquer método e também enviar parâmetros

#### Primeira aplicação Flask

Importando o pacote Flask
```py
from flask import Flask
```

```py
app = Flask(__name__)
```

Criando a primeira rota
```py
def ola():
    return "Olá, Mundo!"
```

Criando um decorador com a rota que será invocada `"/"`
```py
@app.route("/")
```

Criando o `run` para execução da aplicação.
> Para que outros modulos não invoquem essa execução iremos colocar a chamada dentro de um `if` verificando se a chamada vem desse próprio módulo **run.py** validando se é igual a `__main__` quem está invocando.
```py
if __name__=="__main__":
     app.run()
```

#### Executando a aplicação

Quando a aplicação é executada, é apresentado no terminal *localhost* que está executando `http://127.0.0.1:5000/`

Ao acessarmos essa URL, abrirá o navegador apresentando **`Olá, Mundo!`**.

![TIPS]

* Para reapresentar no navegador, qualquer alteração realizada no código precisaremos reiniciar a aplicação.
* Ou podemos utilizar o parâmetro **debug**
  * Utilizando o parâmetro como `True` a aplicação reinicia a cada alteração automaticamente
  * `app.run(debug=True)`
  * Em produção devemos desabilitar o modo `debug=False` senão ele apresentará toda a trilha do erro.

#### Utilizando o Postman para testar a rota

O Postman consegue realizar chamadas utilizando outros métodos.

Colocamos o *localhost* e enviamos a requisição.  
Com isso veremos o mesmo retorno apresentado pelo navegador.

![TIPS]

> O navegador só utiliza o método GET. Logo não conseguimos testar outros métodos diretamente nele, motivo pelo qual utilizamos o Postman.

Para efeito de testes, iremos incluir um *POST* para leitura, mesmo que pela definição da arquitetura REST, ele seja utilizado para realizar **alteração**.

```py
@app.route("/", methods=['POST'])
```

Por não existir para essa raíz um *GET*, o navegador apresentará **Method Not Allowed**.  
Porém, pelo postman conseguimos visualizar o retorno, alterando a chamada para *POST*.

Podemos definir também, que ele aceite dois métodos tanto o *GET* quanto o *POST*, para isso adicionamos em `methods`.

```py
@app.route("/", methods=['GET','POST'])
```

Com isso receberemos retorno escolhendo qualquer dos dois métodos tanto no Postman quanto no navegador.

* Podemos passar parâmetros `<numero>`.

>```py
> @app.route("/<numero>", methods=['GET','POST'])
> 
> def ola(numero):
>   return 'Olá, Mundo! {}'.format(numero) 
>```

* Essa é uma forma que temos de pegar um parâmetro atráves da URI.  
Podemos declarar o tipo do parâmetro que será passado. Ex: `<int:numero>` - Inteiro.
* No navegador adicionamos um valor após o endereço (Ex.: URI + 100) e receberemos o retorno.
* **Olá, Mundo! 100**