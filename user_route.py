from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
# from sql_example.database import User, get_db
from nosql_example.database import user_collection
from models import UserBody, UserResponse, UserUpdate
from sqlalchemy.exc import IntegrityError

router = APIRouter()

class ResourceExistsError(Exception):

  def __init__(self, message:str, error_code:int):
    self.message, self.error_code  = message, error_code
    super().__init__(self.message, self.error_code)

# @router.get("/users/")
# def read_users(db: Session = Depends(get_db)):
#   users = db.query(User).all()
#   return users

# @router.post("/user", response_model=UserResponse)
# def add_new_user(
#   user:UserBody,
#   db:Session = Depends(get_db)
# ):
#   new_user = User(
#     name=user.name,
#     email=user.email
#   ) 

#   try:
#     db.add(new_user)
#     db.commit()
#   except IntegrityError:
#     raise ResourceExistsError(message="User Exists Already", error_code=status.HTTP_409_CONFLICT)
  
#   db.refresh(new_user) 
  
#   return new_user

# @router.get("/user")
# def get_user(
#   user_id: int,
#   db: Session = Depends(get_db)
# ):
#   user = db.query(User).filter(User.id==user_id).first()

#   if user is None:
#     raise HTTPException(
#       status_code=status.HTTP_404_NOT_FOUND,
#       detail="User not found"
#     )

#   return user

# @router.patch("/user/{user_id}", response_model=UserResponse)
# def update_user(
#   user_id: int,
#   user: UserUpdate,
#   db: Session = Depends(get_db)
# ):
#   db_user = db.query(User).filter(User.id==user_id).first()

#   if db_user is None:
#     raise HTTPException(
#       status_code=status.HTTP_404_NOT_FOUND,
#       detail="User Not Found"
#     )
#   # print(user.model_dump(exclude_unset=True))
#   for key, value in user.model_dump(exclude_unset=True).items():
#     setattr(db_user, key, value)

#   try:
#     db.commit()
#   except IntegrityError:
#     raise ResourceExistsError(message="User exists already", error_code=status.HTTP_409_CONFLICT)
#   db.refresh(db_user)

#   return db_user

# @router.delete("/user")
# def delete_user(
#   user_id: int, db:Session=Depends(get_db)
# ):
#   db_user = db.query(User).filter(User.id==user_id).first()

#   if db_user is None:
#     raise HTTPException(
#       status_code=status.HTTP_404_NOT_FOUND,
#       detail="User not found"
#     )
  
#   db.delete(db_user)
#   db.commit()
#   return {"detail": "user deleted"}


@router.get("/users")
def read_users():
  return [user for user in user_collection.find()]