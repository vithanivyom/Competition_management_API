from pydantic import BaseModel
from Project_1.utils.schema import CommonSchemas
from typing import Union, Optional

# for send data to database
class EnetrySchema(BaseModel,CommonSchemas):
    e_name : str
    title : str
    student_name : str
    cometition_id : int
    
    class Config:
        orm_mode = True

# Display to user
class CreateEntry(BaseModel):
    id : int
    e_name : str
    title : str
    student_name : str
    cometition_id : int

    class Config:
        orm_mode = True

class DisplayUser(BaseModel):
    id : int 
    name : str  
    dob : str 
    gender : str 
    email : str 

    class Config:
        orm_mode = True

# values which will able to updated

class UpdateEntry(BaseModel):
    e_name : Optional[str] = None
    student_name : Optional[str] = None

    class Config:
        orm_mode = True


class Error(BaseModel):
    error : str

Response = Union[ DisplayUser, Error]