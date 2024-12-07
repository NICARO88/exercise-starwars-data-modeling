import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

# Tabla de Usuarios
class User(Base): 
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)  # Identificador único
    email = Column(String(120), unique=True, nullable=False)  # Correo electrónico
    password = Column(String(80), nullable=False)  # Contraseña
    first_name = Column(String(80))  # Nombre del usuario
    last_name = Column(String(80))  # Apellido del usuario
    favorites = relationship('Favorite', back_populates='user')  # Relación uno-a-muchos con favoritos

# Tabla de Favoritos
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)  # Identificador único del favorito
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # Relación con usuario
    swapi_type = Column(String(20), nullable=False)  # Tipo de favorito: 'planet', 'character', 'vehicle', 'starship'
    swapi_id = Column(Integer, nullable=False)  # ID único del recurso en SWAPI
    user = relationship('User', back_populates='favorites')  # Relación con el usuario

# Tabla de Planetas
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)  # Identificador único
    name = Column(String(80), nullable=False)  # Nombre del planeta
    climate = Column(String(120))  # Clima del planeta
    terrain = Column(String(120))  # Tipo de terreno
    population = Column(String(50))  # Población
    url = Column(String(255), nullable=False)  # URL del recurso en SWAPI
    residents = relationship('Character', back_populates='planet')  # Relación uno-a-muchos con personajes

# Tabla de Personajes
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)  # Identificador único
    name = Column(String(80), nullable=False)  # Nombre del personaje
    gender = Column(String(20))  # Género
    birth_year = Column(String(20))  # Año de nacimiento
    url = Column(String(255), nullable=False)  # URL del recurso en SWAPI
    planet_id = Column(Integer, ForeignKey('planet.id'))  # Clave foránea hacia Planet
    planet = relationship('Planet', back_populates='residents')  # Relación N a 1 con planetas

# Tabla de Vehículos
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)  # Identificador único
    name = Column(String(80), nullable=False)  # Nombre del vehículo
    model = Column(String(120))  # Modelo
    vehicle_class = Column(String(50))  # Clase del vehículo
    url = Column(String(255), nullable=False)  # URL del recurso en SWAPI

# Tabla de Naves Espaciales
class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)  # Identificador único
    name = Column(String(80), nullable=False)  # Nombre de la nave
    model = Column(String(120))  # Modelo
    starship_class = Column(String(50))  # Clase de la nave
    url = Column(String(255), nullable=False)  # URL del recurso en SWAPI

## Generar el Diagrama UML
try:
    render_er(Base, 'diagram.png')
    print("¡Diagrama generado con éxito!")
except Exception as e:
    print("Error al generar el diagrama:", e)

