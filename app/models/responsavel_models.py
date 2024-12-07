from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.database import db

Base = declarative_base()

class Responsavel(Base):
    __tablename__ = "responsavel"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50))
    senha = Column(String(20))
    ddd = Column(Integer(3))
    telefone = Column(Integer(17))


    def __init__(self, email: str, senha: str, ddd: int, telefone: str):
        self.email = email
        self.senha = senha
        self.ddd = ddd
        self.telefone = telefone))

    
Base.metadata.create_all(bind=db)