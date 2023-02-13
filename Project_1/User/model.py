from Project_1.database.database import base
from sqlalchemy import String,Integer,DateTime,Column
from Project_1.utils.models import CommomModel
from datetime import datetime
# from Project_1.Competition.model import CompetitionDb
from sqlalchemy.orm import relationship

class UserDb(base,CommomModel):
    """

    Based on UserDb class values, Database will created new table.

    """
    __tablename__ = "user"
    id = Column(Integer,primary_key = True,index=True)
    name = Column(String)
    dob = Column(String)
    gender = Column(String)
    email = Column(String)

    # competition = relationship("CompetitionDb", backref="[entries]", cascade="all, delete-orphan", passive_deletes=True, overlaps="[competition],entries")
    
