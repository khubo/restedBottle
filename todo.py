from bottle import request, response, get, post , put, run

todos = [{'id': 1, 'name': 'brew coffe', 'done': False }]

@get('/todo')
def get_todo():
    return {
    'todos': todos,
    'length': len(todos)
    }

@post('/todo')
def add_todo():
    todo = request.json['todo']
    todos.append({
        'id': len(todos)+1,
        'name': todo,
        'done': False
    })
    return 'Todo added!'

@put('/todo')
def edit_todo():
    id = int(request.json['id'])
    done = request.json['done']
    todos[id-1]['done'] = done
    return 'Updated Todo'


#run the default app
run(host='localhost', port=8000, reloader=True)
