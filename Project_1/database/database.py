from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()


DRIVER = os.getenv("DB_DRIVER")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DB_DATABASE")


database_url = f"{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{int(PORT)}/{DATABASE}"

engine = create_engine(
    database_url
)

sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind= engine)

base = declarative_base()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()