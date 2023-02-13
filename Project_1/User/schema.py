from pydantic import BaseModel
from typing import Optional,Union


# for database
class CreateUser(BaseModel):
    name : Optional[str] = None
    dob : Optional[str] = None
    gender : Optional[str] = None
    email : Optional[str] = None
    class Config:
        orm_mode = True


#for Display user
class DisplayUser(BaseModel):
    id : int 
    name : str  
    dob : str 
    gender : str 
    email : str 

    class Config:
        orm_mode = True

# if value not foun, than for return print
class Error(BaseModel):
    error: str


Response = Union[DisplayUser, Error]