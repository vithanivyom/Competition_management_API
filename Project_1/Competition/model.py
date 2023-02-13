from Project_1.database.database import base
from sqlalchemy import String,Integer, Column,ForeignKey
from Project_1.utils.models import CommomModel
from Project_1.User.model import UserDb
from sqlalchemy.orm import relationship


class CompetitionDb(base,CommomModel):
    __tablename__ = "Competition"
    id = Column(Integer,primary_key = True)
    c_name = Column(String)
    description = Column(String)
    Region = Column(String)
    language = Column(String)
    use_ID = Column(Integer, ForeignKey(UserDb.id))

    # participants = relationship("EntryDb", backref= "[entry]")
    # entries = relationship("UserDb", backref="[competition]", cascade="all, delete-orphan", passive_deletes=True, overlaps="[entries],competition")