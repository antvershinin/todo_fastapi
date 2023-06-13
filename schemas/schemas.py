from pydantic import BaseModel


class Todo_edit(BaseModel):
    text: str
    completed: bool = False


class Todo_add(BaseModel):
    text: str
    completed: bool = False

    class Config:
        orm_mode = True
