import os
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from datetime import datetime
from eralchemy2 import render_er

Base = declarative_base()

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    nombre = Column(String(120), nullable=False)
    apellido = Column(String(120), nullable=False)
    favoritos = relationship("Favorito", backref="usuario")

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    descripcion = Column(String(250))
    especie = Column(String(50))
    genero = Column(String(50))
    favoritos = relationship("Favorito", backref="personaje")

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    clima = Column(String(120))
    poblacion = Column(Integer)
    favoritos = relationship("Favorito", backref="planeta")

def to_dict(self):
    return {
        "id": self.id,
        "nombre": self.nombre,
        "clima": self.clima,
        "terreno": self.terreno,
        "poblacion": self.poblacion
    }


engine = create_engine('sqlite:///starwars_blog.db')
Base.metadata.create_all(engine)


try:
    render_er(Base, 'diagram.png')
    print("Diagrama generado correctamente.")
except Exception as e:
    print("Ocurrió un error al generar el diagrama:", e)