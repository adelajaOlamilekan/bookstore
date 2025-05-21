from pydantic import BaseModel, Field, EmailStr, field_validator
from datetime import datetime
from typing import Optional
from exceptions import ValueExceptionError
from fastapi import status

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
  age: int

  @field_validator("age")
  def validate_age(cls, value):
    if value < 18 or value > 100:
      raise ValueExceptionError(message= "Age must be between 18 and 100", 
                                error_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return value
  
class UserResponse(UserBody):
  id: str

class UserUpdate(UserBody):
  email: Optional[EmailStr] = None
  name: Optional[str] = None
