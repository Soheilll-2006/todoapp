from fastapi import APIRouter, Depends, HTTPException , Path
import models
from database import SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
from starlette import status
from pydantic import BaseModel , Field

ROUTER = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DB_DEPENDENCY = Annotated[Session, Depends(get_db)]

class TodoRequest(BaseModel):
    title: str = Field(min_length= 3)
    description: str = Field(min_length= 5)
    completed: bool
    priority: int = Field(ge=0, le=6)


@ROUTER.get("/" , status_code= status.HTTP_200_OK)
async def read_all(db: DB_DEPENDENCY):
    return db.query(models.todo).all()


@ROUTER.get("/todo/{todo_id}" , status_code= status.HTTP_200_OK)
async def readbyid(db : DB_DEPENDENCY , todo_id : int = Path(gt=0)):
    todoresponsebyid= db.query(models.todo).filter(models.todo.id == todo_id).first()
    if todoresponsebyid is not None :
        return todoresponsebyid
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    
@ROUTER.post("/create_todo",status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoRequest, db: DB_DEPENDENCY):
    new_todo = models.todo(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@ROUTER.put("/update_todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo( todo: TodoRequest, db: DB_DEPENDENCY , todo_id: int = Path(gt=0) ):
    existing_todo = db.query(models.todo).filter(models.todo.id == todo_id).first()
    if existing_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    existing_todo.title = todo.title
    existing_todo.description = todo.description
    existing_todo.completed = todo.completed
    existing_todo.priority = todo.priority
    db.commit()
    return {"message": "Todo updated successfully"}

@ROUTER.delete("/delete_todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int, db: DB_DEPENDENCY):
    existing_todo = db.query(models.todo).filter(models.todo.id == todo_id).first()
    if existing_todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    db.delete(existing_todo)
    db.commit()
    return {"message": "Todo deleted successfully"}

@ROUTER.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok"} 