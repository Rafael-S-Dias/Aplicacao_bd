from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.database import db
from datetime import date, time

Base = declarative_base()

class Consultas(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date)
    local = Column(String(20))
    sala = Column(String(20))
    horario = Column(Time)


    def __init__(self, data: str, local: str, sala: str, horario: time):
        self.data = data
        self.local = local
        self.sala = sala
        self.horario = horario

    
Base.metadata.create_all(bind=db)