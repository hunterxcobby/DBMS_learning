#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_schema import User
from create_schema import engine

Session = sessionmaker()
Session.configure(bind=engine)  # once engine is available

# Instantiate a Session object
session = Session()

# ed_user = User(name="Sandy", fullname="Sandy Afeawo", nickname="curdy jasoer", age=21)
# session.add(ed_user)

# session.add_all([
#     User(name= "Kelvin", age=21, nickname ="Chronicles", fullname = "Kelvin Asare Bosompem"),
#     User(name= "Rosemond", age=19 , nickname ="Ameley", fullname = "Rosemond Ameley Okai"),
#     User(name= "Precious", age=33 , nickname = "Dzifah", fullname = "Precious Dzifah Krah"),
#     User(name= "Nasia", age= 120, nickname = "Nasia", fullname = "Nasia Korkor Offei Tetteh"),
#     User(name= "Julie", age=21, nickname ="Julie", fullname = "Juliana Gati")
# ])

# def __repr__(self):
#     return f"<User(id={self.id}, name='{self.name}', fullname='{self.fullname}', nickname='{self.nickname}')>"

# our_user = session.query(User).filter_by(name='Nasia').first()
# our_user.age = 22

# if our_user:
#     print(f"User found: {our_user}")
# else:
#     print("User not found.")

"""ROLL BACK """
# our_user = session.query(User).filter_by(name='Sandy').first()
# our_user.name = 'Sandra'
# fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
# session.add(fake_user)

# session.query(User).filter(User.name.in_(['Sandra', 'fakeuser'])).all()

# session.rollback()
# session.commit()

# print(session.dirty)
# print(session.new)

