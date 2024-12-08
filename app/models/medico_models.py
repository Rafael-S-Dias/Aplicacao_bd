from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
# from config.database import db

Base = declarative_base()

class Medico(Base):
    __tablename__ = "medico"

    crm = Column(String(30), unique=True, primary_key=True)
    primeiroNome = Column(String(30), nullable=False)
    nomeMeio = Column(String(30))
    ultimoNome = Column(String(30), nullable=False)
    especialiadade = Column(String(30), nullable=False)

    def __init__(self, crm: str, primeiroNome: str, nomeMeio: str, ultimoNome: str, especialiadade: str):
        self.crm = crm
        self.primeiroNome = primeiroNome
        self.nomeMeio = nomeMeio
        self.ultimoNome = ultimoNome
        self.especialiadade = especialiadade

    
# Base.metadata.create_all(bind=db)