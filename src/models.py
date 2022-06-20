import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)

    favorites = relationship('Favorites', backref='user', lazy=True)
    

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250),ForeignKey('user.id'))
    planet_id = Column(String(250),ForeignKey('planet.id'))
    characters_id = Column(String(250),ForeignKey('characters.id'))
    vehicle_id = Column(Integer,ForeignKey('vehicle.id'))



class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    eyes = Column(String(250), nullable=False, unique=True)
    hair = Column(String(250), nullable=False, unique=True)
    planet_id = Column(String(250),ForeignKey('planet.id'))
    vehicle_id = Column(Integer,ForeignKey('vehicle.id'))

    favorites_user = relationship('Favorites', backref='user', lazy=True)
    

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    climate = Column(String(250), nullable=False, unique=True)
    population = Column(String(250), nullable=False, unique=True)

    favorites_planet = relationship('Favorites', backref='planet', lazy=True)
    favorites_character_planet = relationship('Characters', backref='planet', lazy=True)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    passengers = Column(String(250), nullable=False, unique=True)
    cargo_capacity = Column(String(250), nullable=False, unique=True)

    favorites_vehice = relationship('Favorites', backref='vehicle', lazy=True)
    favorites_character_planet = relationship('Characters', backref='vehicle', lazy=True)
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')