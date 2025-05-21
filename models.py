from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional

class Book(BaseModel):
  title: str = Field(..., min_length=1, max_length=100)
  author: str = Field(..., min_length=1, max_length=50)
  year: int = Field(..., gt=1900, lt=2100)

class BookResponse(BaseModel):
  title: str
  author: str

class UserBody(BaseModel):
  name:str
  email: EmailStr

class UserResponse(BaseModel):
  name:str
  email: EmailStr
  updated_at: datetime

class UserUpdate(UserBody):
  email: Optional[EmailStr] = None
  name: Optional[str] = None
