from sqlmodel import SQLModel, create_engine

DATABASE_URL = "postgresql://taskuser:taskpass@localhost:5432/taskdb"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)
