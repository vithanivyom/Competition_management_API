from Project_1.database.database import get_db
from fastapi import APIRouter, Depends, status
from Project_1.Entry.schema import *
from sqlalchemy.orm import Session
from typing import List
from Project_1.Entry.model import EntryDb
from Project_1.Competition.model import CompetitionDb
from Project_1.User.model import UserDb
from sqlalchemy import create_engine, Table, Column, Integer, MetaData, select

entry = APIRouter()


# getting all information about entry 
@entry.get("/entry", response_model=List[CreateEntry], status_code = status.HTTP_200_OK)
def all_entry(db:Session = Depends(get_db)) -> dict:
    """ Generate all entries from database

    Args:
    Returns:
        dict: return list of dict
    """

    dbEntry = db.query(EntryDb).all()

    return dbEntry


# getting information of particulat entry

@entry.get("/entry/{name}", response_model=  List[Response], status_code = status.HTTP_200_OK)
def entry_by_name(name, db:Session = Depends(get_db)):
    empty = []
    empty1 = []
    """ To generate information about particular entry.

    Args:
        name (_type_): Provide name of entry
    Returns:
        dict: return dict type value
    """
    dbEntry = db.query(EntryDb.cometition_id).filter(EntryDb.e_name==name).all()
    for i in dbEntry:
        empty.append(i[0])
    print(empty)
    dbCompetition = db.query(CompetitionDb.use_ID).filter(CompetitionDb.id.in_(empty))
    
    for i in dbCompetition:
        empty1.append(i[0])
    set(empty1)
    print(empty1)
    dbUser = db.query(UserDb).filter(UserDb.id.in_(empty1)).all()
    # print(type[dbUser])
    # query = select([UserDb]).where(UserDb.c.id.in_(select([CompetitionDb.use_ID]).where(CompetitionDb.use_ID == dbEntry)))
    if dbUser is None:
        print(0)
        return Error(error= "{} is not valid entry".format(name))
    print(1)
    return dbUser



#Add entry in database

@entry.post("/entry", response_model= CreateEntry, status_code = status.HTTP_201_CREATED)
def add_entry(request:EnetrySchema , db:Session = Depends(get_db)) -> dict:
    """ To add new entry in database

    Args:
        request (EnetrySchema): For enter detail about entry, follow EntrySchema Class

    Returns:
        dict: return dict type value
    """

    newEntry = EntryDb(cometition_id = request.cometition_id, e_name = request.e_name ,title= request.title, student_name = request.student_name)
    db.add(newEntry)
    db.commit()
    db.refresh(newEntry)

    return newEntry


#Update entry by id

@entry.put("/entry/{id}", status_code= status.HTTP_202_ACCEPTED)
def update_entry(id:int, request:UpdateEntry, db:Session = Depends(get_db)) -> dict:
    """ update entry by using id of entry

    Args:
        id (int): id of entry

    Returns:
        dict: return dict type value
    """
    findEntry = db.query(EntryDb).filter(EntryDb.id == id).first()

    if findEntry is not None:

        if request.e_name != None:
            findEntry.e_name = request.e_name
        if request.student_name != None:
            findEntry.student_name = request.student_name
        db.commit()
        return {"message" : "Updated"}
    
    else:
        return{"message": "id {} is not in database"}


# delete entry
@entry.delete("/entry/{id}", status_code= status.HTTP_200_OK)
def delete_entry(id:int ,db:Session = Depends(get_db)) -> dict:
    """ delete enetry from database using provided entry id

    Args:
        id (int): id of entry
    """

    findEntry = db.query(EntryDb).filter(EntryDb.id==id).first()

    if findEntry is not None:
        db.delete(findEntry)
        db.commit()
        return {"message" : "deleted successfully"}
    else:
        return{"message" : "id {} is does't exist"}