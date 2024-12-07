from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import declarative_base
from config.database import db
from datetime import date

Base = declarative_base()

class Paciente(Base):
    __tablename__ = "paciente"

    cpf = Column(Integer, primary_key=True)
    ciptea = Column(String(50))
    primeiroNome = Column(String(20))
    nomeMeio = Column(String(20))
    ultimoNome = Column(String(20))
    dataNascimento = Column(Date)

    primeiroNomePai = Column(String(20))
    nomeMeioPai = Column(String(20))
    ultimoNomePai = Column(String(20))

    primeiroNomeMae = Column(String(20))
    nomeMeioMae = Column(String(20))
    ultimoNomeMae = Column(String(20))

    numero = Column(Integer(30))
    complemento = Column(String(50))
    cidade = Column(String(50))
    cep = Column(String(50))
    estado = Column(String(50))
    logradouro = Column(String(50))

    def __init__(self, cpf: str, ciptea: str, primeiroNome: str, nomeMeio: str, ultimoNome: str, dataNascimento: date,
        primeiroNomePai: str, nomeMeioPai: str, ultimoNomePai: str, primeiroNomeMae: str, nomeMeioMae: str, ultimoNomeMae: str,
        numero: int, complemento: str, cidade: str, cep: str, estado: str, logradouro: str
    ):
        self.cpf = cpf
        self.ciptea = ciptea
        self.primeiroNome = primeiroNome
        self.nomeMeio = nomeMeio
        self.ultimoNome = ultimoNome
        self.dataNascimento = dataNascimento

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
        
    
Base.metadata.create_all(bind=db)