import sqlite3

from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''


class Database:
    def __init__(self, nome):
        self.name = nome+'.db'
        self.conn = sqlite3.connect(self.name)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY,
                                                                title STRING,
                                                                content STRING NOT NULL);''')
        
    def add(self, note : Note):
        self.conn.execute("INSERT INTO note (title, content) VALUES ('{0}', '{1}');".format(note.title, note.content))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        lista = []
        for linha in cursor:
            note = Note(linha[0], linha[1], linha[2])
            lista.append(note)
        return lista
    
    def get_note(self, id):
        cursor = self.conn.execute(f"SELECT id, title, content FROM note WHERE id = {id}")
        linha = cursor.fetchone()
        return Note(linha[0], linha[1], linha[2])
    
    def update(self, entry : Note):
        cursor = self.conn.cursor()
        cursor.execute(f"UPDATE note SET title = '{entry.title}', content = '{entry.content}' WHERE id = {entry.id}")
        self.conn.commit()

    def delete(self, note_id):
        cursor = self.conn.cursor()
        cursor.execute(f"DELETE FROM note WHERE id = {note_id}")
        self.conn.commit()
