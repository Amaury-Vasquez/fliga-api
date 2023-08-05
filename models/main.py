from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Date

class UserModel(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(Date)
        
class TeamModel(Base):
    __tablename__ = "teams"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    league = Column(String)
    league_type = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))