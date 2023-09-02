from utils import load_data, load_template, add_anotacao, build_response
from database import Database, Note
import urllib.parse as up

def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
       
        for chave_valor in corpo.split("&"):
            spaces = chave_valor.split("=")
            if spaces[0] == "titulo":
                params["titulo"] = up.unquote_plus(spaces[1])
            if spaces[0] == "detalhes":
                params["detalhes"] = up.unquote_plus(spaces[1])
        add_anotacao(params)
        return build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template('components/note.html')
    notes_li = [note_template.format(title=note.title, details=note.content, note_id=note.id) for note in load_data()]
    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))

def deleta(id):
    db = Database('banco')
    db.delete(int(id))
    return build_response(code=303, reason='See Other', headers='Location: /')

def update(request, id):
    db = Database('banco')
    note = db.get_note(int(id))
    
    if request.startswith('POST'):
        request = request.replace('\r', '')
        
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}

        for chave_valor in corpo.split("&"):
            spaces = chave_valor.split("=")
            if spaces[0] == "titulo":
                params["titulo"] = up.unquote_plus(spaces[1])
            if spaces[0] == "detalhes":
                params["detalhes"] = up.unquote_plus(spaces[1])
        
        note = Note(id, params['titulo'], params['detalhes'])
        db.update(note)
        note_template = load_template('components/note.html')
        notes_li = [note_template.format(title=note.title, details=note.content, note_id=note.id) for note in load_data()]

        notes = '\n'.join(notes_li)

        return build_response(body=load_template('index.html').format(notes=notes), code=303, reason='See Other', headers='Location: /')
    
    return build_response(body=load_template('update.html').format(titulo=note.title, detalhes=note.content))