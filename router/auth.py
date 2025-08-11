from typing import Annotated
from fastapi import FastAPI , APIRouter
from fastapi.params import Depends
from pydantic import BaseModel
from database import SessionLocal
from models import users
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette import status
from fastapi import HTTPException, Path
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role : str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DB_DEPENDENCY = Annotated[Session, Depends(get_db)]


def authenticate_user(db, email: str, password: str):
    user = db.query(users).filter(users.email == email).first()
    if not user :
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return True

router = APIRouter()
@router.post("/" , status_code=200)

async def create_user(user: CreateUserRequest , db: DB_DEPENDENCY):
    create_user_model = users(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        role=user.role,
        hashed_password=bcrypt_context.hash(user.password),
        is_active=True,
    )
    db.add(create_user_model)
    db.commit()
    db.refresh(create_user_model)
    return {"message": "User created successfully", "user": create_user_model}

@router.post("token")
async def login(db: DB_DEPENDENCY, form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"SUCCESSFUL LOGIN"}