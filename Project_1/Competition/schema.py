from pydantic import BaseModel
from Project_1.utils.schema import CommonSchemas
from typing import Optional, Union

# Class for database
class Competitions(BaseModel, CommonSchemas):
    c_name : str
    description: str
    Region: str
    language: str
    use_ID : int

    class Config:
        orm_mode = True

# Class for user
class CreateCompetition(BaseModel):
    id:int 
    c_name :str
    description:str
    Region: str
    language:str
    use_ID :int

    class Config:
        orm_mode = True

class UpdateCompetitions(BaseModel):
    c_name : Optional[str] = None
    Region: Optional[str] = None
    language: Optional[str] = None

    class Config:
        orm_mode = True


class Error(BaseModel):
    error: str

response = Union[CreateCompetition, Error]