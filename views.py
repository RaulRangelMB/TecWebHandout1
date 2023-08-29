from utils import load_data, load_template, add_anotacao, build_response
import urllib.parse as up

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        print("a"*100)
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split("&"):
            print(chave_valor)
            spaces = chave_valor.split("=")
            if spaces[0] == "titulo":
                params["titulo"] = up.unquote_plus(spaces[1])
            if spaces[0] == "detalhes":
                params["detalhes"] = up.unquote_plus(spaces[1])
        print(params)
        add_anotacao(params)
        return build_response(code=303, reason='See Other', headers='Location: /')

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [note_template.format(title=dados['titulo'], details=dados['detalhes']) for dados in load_data('notes.json')]
    # Método com for
    # notes_li = []
    # for dados in load_data('notes.json'):
    #     notes_li.append(NOTE_TEMPLATE.format(title=dados['titulo'], details=dados['detalhes']))
    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))