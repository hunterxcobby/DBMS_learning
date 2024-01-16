#!/usr/bin/python3
from sqlalchemy import create_engine, and_, or_
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
# for name, in session.query(User.name).filter_by(fullname='Sandy Afeawo'):
#     print(name)

# for name, in session.query(User.name).filter(User.fullname == 'Kelvin Asare Bosompem'):
#     print(name)

query = session.query(User)

"""Equal (==) Operator:"""
# result = query.filter(User.name == 'Sandy').all()
# print(result)

""" Not Equal (!=) Operator:"""
# result = query.filter(User.name != "Sandy").all()
# print(result)

""" Like Operator:"""
# result = query.filter(User.name.like('%ia%')).all()
# print(result)

"""Case-Insensitive Like Operator (ilike):"""
# result= query.filter(User.name.ilike('%sa%')).all()
# print(result)

"""In Operator:"""
# query.filter(User.name.in_(['kelvin', 'julie', 'nasia']))

# # works with query objects too:
# query.filter(User.name.in_(
#     session.query(User.name).filter(User.name.ilike('%sa%'))
# ))

# # use tuple_() for composite (multi-column) queries
# from sqlalchemy import tuple_
# result = query.filter(
#     tuple_(User.name, User.nickname).\
#     in_([('sandy', 'curdy jasper'), ('Nasia', 'Nasia')])
# )

# # Iterating over the result and printing relevant attributes
# for user in result:
#     print(f"Name: {user.name}, Nickname: {user.nickname}")

# """Not In Operator:"""
# result = query.filter(~User.name.in_(['Ed', 'Sandy', 'Kelvin'])).all()
# print(result)

""" Is Operator:
# Filter users with a name."""
# result = query.filter(User.name == None).all()
# print(result)

# # alternatively, if pep8/linters are a concern
# result = query.filter(User.name.is_(None)).all()
# print(result)

"""Is Not Operator:"""
# result = query.filter(User.name != None).all()
# print(result)

# # alternatively, if pep8/linters are a concern
# query.filter(User.name.isnot(None)).all()
# print(result)


"""AND Operator:
Use and_() or chain multiple filter conditions."""

# # Using and_()
# result = query.filter(and_(User.name == 'Kelvin', User.fullname == 'Kelvin Asare Bosompem')).all()
# print(result)
# # Using multiple filter conditions
# result = query.filter(User.name == 'ed', User.fullname == 'Ed Jones').all()
# print(result)

# # Chaining
# result = query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones').all()
# print(result)


"""OR Operator:
Use or_() for OR conditions."""
# result = query.filter(or_(User.name == 'Sandy', User.name == 'Rosemond')).all()
# print(result)

