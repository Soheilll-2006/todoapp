from fastapi import FastAPI, APIRouter
import models
from database import engine
from router import auth , todos

app = FastAPI()
models.base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth")
app.include_router(todos.ROUTER, prefix="/todos")
