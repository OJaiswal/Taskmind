from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Header, Security
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from sqlmodel import Session, select, SQLModel
from auth import hash_password, verify_password, create_access_token, get_current_user
from models import User, UserCreate, UserLogin, Task, TaskCreate
from database import get_db, engine
from auth import get_current_user

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Create tables on startup
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to TaskMind"}

# Register a user
@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.exec(select(User).where(User.username == user.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
 
    user_obj = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password)
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return {"message": "User registered successfully"}

# Login and generate JWT
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.exec(select(User).where(User.username == user.username)).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

# Create a new task (protected)
@app.post("/tasks")
def create_task(
    task: TaskCreate,
    token: Annotated[str, Depends(oauth2_scheme)],
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.exec(select(User).where(User.username == current_user)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    task_obj = Task(
        user_id=user.id,
        title=task.title,
        description=task.description,
        deadline=task.deadline,
        priority=task.priority,
        status="pending"
    )
    db.add(task_obj)
    db.commit()
    db.refresh(task_obj)
    return {"message": "Task created successfully", "task": task_obj}

# Get all tasks for the current user (protected)
@app.get("/tasks")
def get_tasks(
    token: str = Security(oauth2_scheme),
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    
    user = db.exec(select(User).where(User.username == current_user)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    tasks = db.exec(select(Task).where(Task.user_id == user.id)).all()
    return {"tasks": tasks}
