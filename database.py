from sqlmodel import SQLModel, create_engine, Session

# SQLite database URL (for development)
DATABASE_URL = "sqlite:///./taskmind.db"

# Create the SQLModel-compatible engine
engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL queries

# Function to initialize the database and create tables
def init_db():
    SQLModel.metadata.create_all(engine)

# Dependency to get a DB session
def get_db():
    with Session(engine) as session:
        yield session
