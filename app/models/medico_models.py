from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.database import db

Base = declarative_base()

class Medico(Base):
    __tablename__ = "medico"

    crm = Column(String, primary_key=True)
    primeiroNome = primeiroNome
    nomeMeio = nomeMeio
    ultimoNome = ultimoNome
    especialiadade = especialiadade


    def __init__(self, crm: str, primeiroNome: str, nomeMeio: str, ultimoNome: str, especialiadade: str):
        self.crm = crm
        self.primeiroNome = primeiroNome
        self.nomeMeio = nomeMeio
        self.ultimoNome = ultimoNome
        self.especialiadade = especialiadade

    
Base.metadata.create_all(bind=db)