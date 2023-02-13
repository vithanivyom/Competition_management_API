from Project_1.database.database import get_db
from fastapi import APIRouter, Depends, status
from Project_1.User.schema import *
from sqlalchemy.orm import Session
from typing import List
from Project_1.User.schema import DisplayUser, Response
from Project_1.User.model import UserDb
import sqlalchemy as sql

user = APIRouter()

# getting all information about user

@user.get("/user", response_model= List[DisplayUser], status_code= status.HTTP_200_OK)
def all_user(db:Session = Depends(get_db)) -> dict:
    """ return all the data of user which is in database

    Args:
        db (Session, optional): provide session to database for perform task

    Returns:
        dict: return dict type output
    """
    dbUser = db.query(UserDb).all()

    return dbUser


# getting information of particulat user

@user.get("/user/{id}", response_model=Response, status_code= status.HTTP_200_OK)
def user_by_id(id : int , db:Session = Depends(get_db)) -> dict:
    """ return only output of given user_id

    Args:
        id (_type_): user id
        db (Session, optional): provide session to database for perform task

    Returns:
        dict: return dict type of value
    """
    dbUser = db.query(UserDb).filter(UserDb.id==id).first()

    if dbUser is None:

        return Error(error='{} is not in database'.format(id))
    return dbUser

#Add user in database
@user.post("/user", response_model=DisplayUser, status_code=status.HTTP_200_OK)
def add_user(request:CreateUser , db:Session = Depends(get_db)) -> dict:
    """ Add new user in database
    Args:
        request (CreateUser): we need to follow format of CreateUser class, for add new user in database
        db (Session, optional): provide session to database for perform task

    Returns:
        dict: return type of function is dict
    """

    newUser = UserDb(name = request.name ,dob= request.dob, gender= request.gender, email = request.email)
    db.add(newUser)
    db.commit()

    return newUser

#Update user by id
@user.put("/user/{id}", status_code= status.HTTP_200_OK)
def update_user(id:int, request: CreateUser ,db:Session = Depends(get_db)) -> dict:
    """ update user from table by giving particular value of particular user

    Args:
        id (int): id of user
        request (CreateUser): we need to follow format of CreateUser class, for update user in database
        db (Session, optional): provide session to database for perform task

    Returns:
        dict: return type of function is dict
    """
    findPerson = db.query(UserDb).filter(UserDb.id == id).first()
    
    if findPerson is not None:

        if request.name != None:
            findPerson.name = request.name
        if request.dob != None:
            findPerson.dob = request.dob
        if request.email != None:
            findPerson.email = request.email
        db.commit()
        return {"message":"updated"}
    
    else:
        return {"error" : "id {} is not in database".format(id)}
    

#Delete user

@user.delete("/user/{id}", status_code= status.HTTP_200_OK)
def delete_user(id:int ,db:Session = Depends(get_db)) -> dict:
    """ delete user from user table

    Args:
        id (int): takes id from user for delete user in database
        db (Session, optional): provide session to database for delete given id
    Returns:
        dict: if 
    """

    findPerson = db.query(UserDb).filter(UserDb.id==id).first()

    if findPerson is not None:    
        db.delete(findPerson)
        db.commit()
        return {"message":"deleted"}
    
    else:
        return {"message" : "{} is not exist".format(id)}