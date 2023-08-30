from database import Database, Note
from utils import *

db = Database('banco')

# db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
# db.add(Note(title='Hidrate-se!', content='Lembrar de tomar água'))
# db.add(Note(title='Homer Simpson', content='~( 8(|)'))

notes = db.get_all()
for note in notes:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')

print("Executando comandos\n")
#db.update(Note(2,'ole','samba'))

#db.delete(1)
#db.delete(2)

notes = db.get_all()
for note in notes:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')

print(load_data())