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
                                                                title TEXT,
                                                                content TEXT NOT NULL);''')
        
    def add(self, note : Note):
        self.conn.execute("INSERT INTO note (title, content) VALUES ('{0}', '{1}');".format(note.title,note.content))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT title, content FROM note")
        lista = []
        for linha in cursor:
            note = Note('', linha[0], linha[1])
            lista.append(note)
        return lista
    
    def update(self, entry):
        print(entry)
        command1 = "UPDATE note SET title = '{entry.title}' WHERE id = '{entry.id}'"
        command2 = "UPDATE note SET content = '{entry.content}' WHERE id = '{entry.id}'"
        self.conn.execute(command1)
        self.conn.commit()
        self.conn.execute(command2)
        self.conn.commit()
