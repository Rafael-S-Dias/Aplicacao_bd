from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import declarative_base
from datetime import date
# from config.database import db

Base = declarative_base()

class Paciente(Base):
    __tablename__ = "paciente"

    cpf = Column(Integer, primary_key=True)
    ciptea = Column(String(50))
    dataNascimento = Column(Date)
    primeiroNome = Column(String(20))
    nomeMeio = Column(String(20))
    ultimoNome = Column(String(20))

    primeiroNomePai = Column(String(20))
    nomeMeioPai = Column(String(20))
    ultimoNomePai = Column(String(20))

    primeiroNomeMae = Column(String(20))
    nomeMeioMae = Column(String(20))
    ultimoNomeMae = Column(String(20))

    numero = Column(String(50))
    complemento = Column(String(50))
    cidade = Column(String(50))
    cep = Column(String(50))
    estado = Column(String(50))
    logradouro = Column(String(50))

    def __init__(self, cpf: str, ciptea: str, dataNascimento: date, primeiroNome: str, nomeMeio: str, ultimoNome: str, 
        primeiroNomePai: str, nomeMeioPai: str, ultimoNomePai: str, primeiroNomeMae: str, nomeMeioMae: str, ultimoNomeMae: str,
        numero: str, complemento: str, cidade: str, cep: str, estado: str, logradouro: str
    ):
        self.cpf = cpf
        self.ciptea = ciptea
        self.dataNascimento = dataNascimento
        self.primeiroNome = primeiroNome
        self.nomeMeio = nomeMeio
        self.ultimoNome = ultimoNome

        self.primeiroNomePai = primeiroNomePai
        self.nomeMeioPai = nomeMeioPai
        self.ultimoNomePai = ultimoNomePai

        self.primeiroNomeMae = primeiroNomeMae
        self.nomeMeioMae = nomeMeioMae
        self.ultimoNomeMae = ultimoNomeMae       

        self.numero = numero
        self.complemento = complemento
        self.cidade = cidade
        self.cep = cep
        self.estado = estado
        self.logradouro = logradouro
        
    
# Base.metadata.create_all(bind=db)