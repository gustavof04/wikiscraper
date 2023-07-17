import requests
import re
from bs4 import BeautifulSoup

def remove_brackets(text):
    """ Remove os números envolvidos em colchetes do Wikipedia.

    Args:
        text: Texto do parágrafo
    """
    pattern = r"\[.*?\]"  # regex para encontrar texto entre colchetes []
    return re.sub(pattern, "", text)

def remove_space_between_words(text):
    """ Remove espaços entre as palavras do parágrafo.

    Args:
        text: Texto do parágrafo
    """
    pattern = r"\s+"  # regex para encontrar um ou mais espaços
    return re.sub(pattern, " ", text)

url = 'https://pt.wikipedia.org/wiki/Python' # Definindo URL
response = requests.get (url) # Enviando requisição
raw_html = response.text # Html cru
parsed_html = BeautifulSoup(raw_html, 'html.parser') # Html cru convertido para um objeto Python

formatted_paragraphs = []

# Selecionando parágrafo da definição de Python
what_is_python = parsed_html.select_one('#mw-content-text > div.mw-parser-output > p:nth-child(3)')
# Formatando o parágrafo para remover os colchetes de fonte e espaços desnecessários
formatted_paragraph = remove_space_between_words(remove_brackets(what_is_python.text))
formatted_paragraphs.append(formatted_paragraph)

# Selecionando parágrafo do nome de origem da linguagem Python
name_origin = parsed_html.select_one('#mw-content-text > div.mw-parser-output > p:nth-child(6)')
# Formatando o parágrafo para remover os colchetes de fonte
formatted_paragraph = remove_brackets(name_origin.text)
formatted_paragraphs.append(formatted_paragraph)

# Concatena os parágrafos formatados em uma única string
text = '\n\n'.join(formatted_paragraphs)

# Criando um .txt para ver os parágrafos formatados
python_txt = "python.txt"

try:
    with open(python_txt, "w", encoding='utf-8') as arquivo:
        arquivo.write(text)
    print("Texto gerado com sucesso! Cheque a pasta raíz do projeto para vê-lo")
except Exception as e:
    print("Ocorreu um erro na geração do texto ou na raspagem de dados", str(e))