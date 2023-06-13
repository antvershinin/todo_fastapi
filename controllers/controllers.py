from database import db
from models.models import Todo
from schemas.schemas import Todo_edit, Todo_add

def get_todos():
    todos = db.query(Todo).all()
    db.close()
    return todos

def add_todo(body:Todo_add):
    todo_new = Todo(text=body.text, completed=False)
    db.add(todo_new)
    db.commit()
    db.refresh(todo_new)
    db.close()
    return todo_new

def delete_todo(id):
    todo = db.query(Todo).get(id)
    db.delete(todo)
    db.commit()
    db.close()
    return todo

def edit_todo(id: int, body: Todo_edit):
    todo = db.query(Todo).get(id)
    todo.text = body.text
    todo.completed = body.completed
    db.commit()
    db.refresh(todo)
    db.close()
    return todo

def delete_all():
    todos = db.query(Todo).delete()
    db.commit()
    db.close() 
    return todos

def complete_all(completed : bool):
    todos = db.query(Todo).update(
        {"completed" : completed}
    )
    db.commit()
    todos = db.query(Todo).all()
    db.close()
    return todos