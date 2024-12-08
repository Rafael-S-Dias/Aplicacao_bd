from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
# from config.database import db

Base = declarative_base()

class Responsavel(Base):
    __tablename__ = "responsavel"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), unique=True, nullable=False)
    senha = Column(String(20), nullable=False)
    ddd = Column(Integer, nullable=False)
    telefone = Column(Integer, nullable=False)


    def __init__(self, email: str, senha: str, ddd: int, telefone: str):
        self.email = email
        self.senha = senha
        self.ddd = ddd
        self.telefone = telefone

    
# Base.metadata.create_all(bind=db)