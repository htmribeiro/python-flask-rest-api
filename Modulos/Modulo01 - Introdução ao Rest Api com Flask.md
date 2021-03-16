# Desenvolvimento Avançado Python com Flask e REST API

## Módulo 01 - Introdução ao Rest Api com Flask

### O que é API?

* É um **conjuto de rotinas** para acesso a um aplicativo/software/plataforma baseado na Web
* Acrônimo de Application Programming Interface - Interface de programação de aplicativos
* APIs são importantes quando se tem a intenção de realizar integrações com outros serviços
* Com as APIs a comunicação de software fica transparente ao usuário
* APIs podem ser locais, baseada em web e baseada em programas

### O que é REST?

* É um **modelo** a ser utilizado para projetar **arquiteturas de software** baseado em comunicação via rede
* Acrônimo de Representational State Transfer - Transferência de Estado Representacional
* Foi definido por Roy Fielding em sua tese de doutorado (PhD) na UC Irvine no ano 2000
* REST projeta a ideia de que todo recurso deveria responder aos mesmos métodos

### O que é REST API?

* É uma **API** desenvolvida **utilizando os princípios da arquitetura REST**
* Um REST API é utilizado na comunicação/integração entre software através de **serviços web**
* Um REST API é **consumido** através de requisições HTTP
* REST APIs são geralmente representadas em seus **formatos** por **JSON e XML**. Também são usados páginas HTML, PDF e arquivos de imagens
* Ao implementar um REST API, **cada método deve ser responsável por um tipo diferente de ação**. Exemplo: Consulta, Alteração, Inclusão e Exclusão

### Métodos do protocolo HTTP

* **GET** - Método que solicita algum recurso ou objeto do servidor por meio da URI. (***Consulta***)
* **POST** - Método usado para envio de arquivo/dados ou formulário HTML para o servidor. (***Alteração***)
* **PUT** - Aceita criar ou modificar um objeto do servidor. (***Criação***)
* **DELETE** - Informa por meio da URI o objeto a ser deletado. (***Exclusão***)

### URL vs URN vs URI?

* **URL: Uniform Resource Locator - Localizador de Recursos Universal**
* Host que será acessado. Exemplo: globallabs.academy
* **URN: Uniform Resource Name - Nome do Recurso Universal**
* É o recurso que será identificado. Exemplo: /category/blog/
* **URI: Uniform Resource Identifier - Identificador de Recursos Universal**
* É o identificador do recurso, podendo ser uma imagem, um arquivo ou uma página. Exemplo: https://globallabs.academy/category/blog/
* **URI** une **Protocolo**(https://), **URL**(globallabs.academy) e a **URN**(/category/blog/)

### XML - Extensible Markup Language

* É uma linguagem de marcação
* Utilizada para compartilhamento de informações através de requisições HTTP

```xml
<xmlcep>
  <cep>22041-001</cep>
  <logradouro>Avenida Atlântica</logradouro>
  <complemento>de 2174 a 2634 - lado par</complemento>
  <bairro>Copacabana</bairro>
  <localidade>Rio de Janeiro</localidade>
  <uf>RJ</uf>
  <unidade/>
  <ibge>3304557</ibge>
  <gia/>
</xmlcep>
```

> ***`<parametro>valor</parametro>`***

### JSON - JavaScript Object Notation

* É um formato e troca de dados entre sistemas independentes da linguagem utilizada derivada do JavaScript
* Muitas linguagens possuem suporte nativo a JSON

```json
{
    "cep": "22041-001",
    "logradouro": "Avenida Atlântica",
    "complemento": "de 2174 a 2634 - lado par",
    "bairro": "Copacabana",
    "localidade": "Rio de Janeiro",
    "uf": "RJ",
    "unidade": "",
    "ibge": "3304557",
    "gia": ""
}
```

> ***`"parametro": "valor"`***

### Flask

* É um microframework para Python utilizado para desenvolvimento de aplicações WEB.
* É chamado de microframework porque mantém um núcleo simples, mas é estendível
* Flask não possui camada de abstração para banco de dados, validação de formulários entre outros, mas é possível estender com outras bibliotecas
* Por ser leve e simples de usar, Flask é um dos frameworks Python mais utilizados para desenvolvimento de APIs.

### Exemplo de código

```py
from flask import Flask
app = Flask(__name__)

@app.route("/") # decorador - informando qual a rota que esse método irá acessar
def hello():
    return u'Olá, mundo!'

if __name__ == "__main__":
    app.run()
```