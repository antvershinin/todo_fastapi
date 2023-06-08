from database import Base, engine, SessionLocal, Todo
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()


@app.post("/todos")
def create_todo(data=Body(), db: Session = Depends(get_db)):
    todo = Todo(text=data["text"], completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@app.put("/todos/{id}")
def edit_todo(data=Body(), db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == data["id"]).first()
    if todo == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Todo not found"}
        )
    todo.text = data["text"]
    todo.completed = data["completed"]
    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/todos/{id}")
def delete_todo(id, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if todo == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Пользователь не найден"}
        )
    db.delete(todo)
    db.commit()
    return todo


@app.delete("/todos")
def delete_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).delete()
    db.commit()
    return todos
