from Project_1.database.database import get_db
from fastapi import APIRouter, Depends, status
from Project_1.User.schema import *
from sqlalchemy.orm import Session
from typing import List
from Project_1.Competition.schema import CreateCompetition, Competitions, response, UpdateCompetitions
from Project_1.Competition.model import CompetitionDb
from Project_1.User.model import UserDb

competition = APIRouter()


# getting all information about competition
@competition.get("/competition", response_model=List[CreateCompetition], status_code=status.HTTP_200_OK)
def all_competition(db:Session = Depends(get_db)) -> dict:
    """Provide all the information value to competition


    Returns:
        dict: return dict type value
    """

    dbCompetition = db.query(CompetitionDb).all()
    return dbCompetition

# getting information of particular competition

@competition.get("/competition/{name}",  status_code= status.HTTP_200_OK)
def competition_by_name(name, db:Session = Depends(get_db)):
    list_for_storing_da = []
    data = []
    """ provide specific value from database using competition name

    Args:
        name (_type_): give name of competition
    Returns:
        dict: return dict type value
    """

    dbCompetition = db.query(CompetitionDb).filter(CompetitionDb.c_name==name).all()

    if dbCompetition is None:
        return {"{} is not valid competition".format(name)}
    
    return data

#Add competition in database

@competition.post("/competition", response_model= CreateCompetition, status_code= status.HTTP_200_OK)
def add_competition(request: Competitions , db:Session = Depends(get_db)) -> dict:
    """ To add new competition in database

    Args:
        request (Competitions): contains parameter for add competition

    Returns:
        dict: return dict type value
    """

    newCompetition = CompetitionDb(c_name = request.c_name ,description = request.description ,use_ID = request.use_ID, Region = request.Region, 
                                    language = request.language)
    
    db.add(newCompetition)
    db.commit()
    db.refresh(newCompetition)

    return newCompetition

#Update competition by id
@competition.put("/competition/{id}", status_code= status.HTTP_200_OK)
def update_competition(id, request : UpdateCompetitions, db:Session = Depends(get_db)) -> dict:
    """ Update competition detail 

    Args:
        id (_type_): provide id for update values

    Returns:
        dict : return dict type value
    """

    findCompetition = db.query(CompetitionDb).filter(CompetitionDb.id == id).first()

    if findCompetition is not None:
        for attr in ['c_name', 'Region', 'language']:
            value = getattr(request, attr)
            if value is not None:
                setattr(findCompetition, attr, value)
    db.commit()
    return {"message": "updated"}


#Delete competition

@competition.delete("/delete_competition/{id}", status_code= status.HTTP_200_OK)
def delete_competition(id:int ,db:Session = Depends(get_db)) -> dict:
    """Delete competition from database

    Args:
        id (int): provide id for deleting competition
        
    Returns:
        dict: return dict type value
    """
    findPerson = db.query(CompetitionDb).filter(CompetitionDb.id==id).first()

    if findPerson is not None:
        
        db.delete(findPerson)
        db.commit()
        return {"message" : "deleted"}
    
    else:
        return {"error" : " id {} does not exist".format(id)}