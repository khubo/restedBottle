from bottle import request, response, get, post , put, run, install
from bottle_sqlite import SQLitePlugin
from sqliteJson import *
import json

install(SQLitePlugin(dbfile='./test.db'))

@get('/todo')
def get_todo(db):
    c = db.execute('SELECT id, todo, done from Todo ')
    b = json_serializer(c)
    return {'todo' : b}

@post('/todo')
def add_todo(db):
    todo = request.json['todo']
    c = db.execute('INSERT INTO Todo(todo) values(?)', (todo,))
    return 'Todo added!'

@put('/todo')
def edit_todo(db):
    id = int(request.json['id'])
    done = 1 if request.json['done'] else 0
    print id, done
    c = db.execute('UPDATE Todo set done = ? WHERE id  = ?', (done, id))
    return 'yo'


#run the default app
run(host='localhost', port=8000, reloader=True)
