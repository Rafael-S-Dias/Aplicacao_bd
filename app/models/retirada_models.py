from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.database import db
from datetime import date

Base = declarative_base()

class Retiradas(Base):
    __tablename__ = "retiradas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date)
    local = Column(String(20))
    receita = Column(String(50)) 


    def __init__(self, data: str, local: str, receita: str):
        self.data = data
        self.local = local
        self.receita = receita

    
Base.metadata.create_all(bind=db)