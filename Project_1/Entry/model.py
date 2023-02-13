from Project_1.database.database import base
from Project_1.utils.models import CommomModel
from sqlalchemy import Column,Integer,String,ForeignKey
from Project_1.Competition.model import CompetitionDb
from sqlalchemy.orm import relationship

class EntryDb(base,CommomModel):
    __tablename__ = "entry"
    id = Column(Integer, primary_key = True)
    e_name = Column(String)
    title = Column(String)
    student_name = Column(String)
    cometition_id = Column(Integer,ForeignKey(CompetitionDb.id))

    # entry = relationship("CompetitionDb", backref= "[participants]", cascade="all, delete-orphan", passive_deletes=True, overlaps="[entry],participants")