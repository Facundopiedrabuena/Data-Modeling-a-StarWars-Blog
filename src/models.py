import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Username = Column(String(250), nullable=False)
    Firstname = Column(String(250), nullable=False)
    Lastname = Column(String(250), nullable=False)



class favPlanetas(Base):
    __tablename__ = 'favPlanetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favId = Column(Integer, ForeignKey('Planetas.id'))
    Usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    Usuario = relationship(Usuario)

class Planetas(Base):
    __tablename__ = 'Planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    diametro = Column(String(250))
    gravity = Column(String(250))
    terreno = Column(String(250))
    post_code = Column(String(250), nullable=False)
    
    Usuario = relationship(favPlanetas)

class favPerson(Base):
    __tablename__ = 'favPerson'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favId = Column(Integer, ForeignKey('Personajes.id'))
    Usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    Usuario = relationship(Usuario)

class Personajes(Base):
    __tablename__ = 'Personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    altura = Column(String(250))
    masa = Column(String(250))
    genero = Column(String(250))
    name = Column(String(250))
    post_code = Column(String(250), nullable=False)
    
    Usuario = relationship(favPlanetas)
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')