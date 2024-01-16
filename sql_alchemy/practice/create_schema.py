#!/usr/bin/python3

# connect to a database
from sqlalchemy import create_engine
engine = create_engine('mysql://cobby:cobby3136@localhost/friends', echo=False)

# declare mapping
from sqlalchemy.ext.declarative import declarative_base #import declarative base
Base = declarative_base()


from sqlalchemy import Column, Integer, String, Sequence

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(100))
    nickname = Column(String(50))
    age = Column(Integer)

    def __repr__(self):
         return "\nUser : %d \n name : %s \n fullname : %s \n nickname : %s \n age : %d" % (
            self.id, self.name, self.fullname, self.nickname, self.age)
    
Base.metadata.create_all(engine)
    
