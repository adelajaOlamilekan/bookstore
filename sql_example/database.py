from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import create_engine, DateTime, func

DATABASE_URL = "sqlite:///./test.db"

class Base(DeclarativeBase):
  pass

class User(Base):
  __tablename__="users"
  id: Mapped[int] = mapped_column(primary_key=True)
  email: Mapped[str] = mapped_column(unique=True)
  name: Mapped[str]
  created_at: Mapped[str] = mapped_column(DateTime(timezone=True), default=func.now())
  updated_at: Mapped[str] = mapped_column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SesssionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
  db = SesssionLocal()

  try:
    yield db
  finally:
    # db.close()
    pass