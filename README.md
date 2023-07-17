# Wikiscraper

Web scraping simples feito em Python utilizando as libs **requests** enviando uma requisição GET para a URL do Wikipédia onde fiz a raspagem e **Beautiful Soup** para seleção e formatação do html de dois parágrafos do seguinte artigo:

https://pt.wikipedia.org/wiki/Python

Os parágrafos apresentam:
* O que é a linguagem Python;
* Origem do nome da linguagem Python.

O Wikiscraper cria um arquivo .txt assim que é executado, exibindo os dois parágrafos formatados com padrão utf-8 e duas funções com regex para melhor leitura.

## Tecnologias utilizadas
Python V.: 3.11.1 || Beautiful Soup 4 V.: 4.12.2 || requests V.: 2.31.0

OBS.: É obrigatória a instalação manual do Python na versão citada acima para ser possível a criação do ambiente virtual e instalação das dependências do projeto.

- Windows 8+

https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe

- macOS 10.9+

https://www.python.org/ftp/python/3.11.1/python-3.11.1-macos11.pkg

## Configurando o ambiente virtual
* No seu terminal, navegue até a pasta raiz do projeto e execute o seguinte comando para criar um ambiente virtual:

  <code>python -m venv nome_da_virtualenv</code> (exemplo: venv)

* Rode o comando de acordo com seu sistema para ativar seu ambiente virtual:

  <code>.\nome_da_virtualenv\Scripts\activate</code> (Windows)

  <code>source nome_da_virtualenv/bin/activate</code> (Linux ou macOS)

## Instalando as dependências
* Com o ambiente virtual **ativado**, instale as dependências do projeto com o seguinte comando:

  <code>pip install -r requirements.txt</code>

## Executando o web scraping
* Execute o arquivo principal conforme abaixo:

  <code>python wikiscraper.py</code>
