#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_schema import User
from create_schema import engine
from sqlalchemy.orm import aliased

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

"""Querying"""

"""basic query"""
# for instance in session.query(User).order_by(User.id):
#     print(instance.name, ": ", instance.fullname, " - ", instance.age, "years")

"""column query"""
# for name, fullname in session.query(User.name, User.fullname).order_by(User.name):
#     print(name, "full name is ", fullname)

"""Querying as Named Tuples:"""
# for row in session.query(User, User.name).all():
#     print(row.User, row.name)

"""Controlled Naming with label():"""
# for row in session.query(User.name.label('name_label')).all():
#     print(row.name_label)


"""Aliasing Entities with aliased():"""
# user_alias = aliased(User, name='user_alias')
# for row in session.query(user_alias, user_alias.name).all():
#     print(row.user_alias)


""" Limiting and Offsetting Results:"""
# for u in session.query(User).order_by(User.id)[1:3]:
#     print(u)

""" Filtering Results:"""
for name, in session.query(User.name).filter_by(fullname='Sandy Afeawo'):
    print(name)

for name, in session.query(User.name).filter(User.fullname == 'Kelvin Asare Bosompem'):
    print(name)