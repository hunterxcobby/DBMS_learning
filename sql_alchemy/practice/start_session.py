#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_schema import User
from create_schema import engine

Session = sessionmaker()
Session.configure(bind=engine)  # once engine is available

# Instantiate a Session object
session = Session()

ed_user = User(name="Sandy", fullname="Sandy Afeawo", nickname="curdy jasoer", age=21)
session.add(ed_user)

# session.add_all([
#     User(name= "Kelvin", age=21, nickname ="namor the rapper", fullname = "Kelvin Asare Bosompem"),
#     User(name= "Rosemond", age=19 , nickname ="BLinkzy BLinkz", fullname = "Rosemond Ameley Okai"),
#     User(name= "Precious", age=33 , nickname = "Hey Oboshi", fullname = "Precious Dzifah Krah"),
#     User(name= "Nasia", age= 120, nickname = "Madam wo p3 sere3", fullname = "Nasia Korkor Offei Tetteh")
# ])

def __repr__(self):
    return f"<User(id={self.id}, name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}')>"

our_user = session.query(User).filter_by(name='cobby').first()
print(our_user)

session.commit()

print(session.dirty)
print(session.new)