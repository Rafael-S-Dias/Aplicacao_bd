from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import declarative_base
from datetime import date

Base = declarative_base()

class Paciente(Base):
    __tablename__ = "paciente"

    CPF = Column(Integer, unique=True, primary_key=True)
    CIPTEA = Column(String(20), unique=True, nullable=False)
    DataNascimento = Column( Date, nullable=False)
    PrimeiroNomePaciente = Column(String(20), nullable=False)
    NomeMeioPaciente = Column(String(20), nullable=False)
    UltimoNomePaciente = Column(String(20), nullable=False)

    PrimeiroNomePai = Column(String(20), nullable=False)
    NomeMeioPai = Column(String(20), nullable=False)
    UltimoNomePai = Column(String(20), nullable=False)

    PrimeiroNomeMae = Column(String(20), nullable=False)
    NomeMeioMae = Column(String(20), nullable=False)
    UltimoNomeMae = Column(String(20), nullable=False)

    Logradouro = Column(String(20), nullable=False)
    Numero = Column(String(5), nullable=False)
    Bairro = Column(String(20), nullable=False)
    Complemento = Column(String(20), nullable=False)
    Cidade = Column(String(20), nullable=False)
    CEP = Column(String(20), nullable=False)
    Estado = Column(String(20), nullable=False)

    def __init__(self, CPF: str, CIPTEA: str, DataNascimento: date, PrimeiroNomePaciente: str, NomeMeioPaciente: str, UltimoNomePaciente: str, 
        PrimeiroNomePai: str, NomeMeioPai: str, UltimoNomePai: str, PrimeiroNomeMae: str, NomeMeioMae: str, UltimoNomeMae: str,
        Logradouro: str, Numero: str, Bairro : str, Complemento: str, Cidade: str, CEP: str, Estado: str, 
    ):
        self.CPF = CPF
        self.CIPTEA = CIPTEA
        self.DataNascimento = DataNascimento
        self.PrimeiroNomePaciente = PrimeiroNomePaciente
        self.NomeMeioPaciente = NomeMeioPaciente
        self.UltimoNomePaciente = UltimoNomePaciente

        self.PrimeiroNomePai = PrimeiroNomePai
        self.NomeMeioPai = NomeMeioPai
        self.UltimoNomePai = UltimoNomePai

        self.PrimeiroNomeMae = PrimeiroNomeMae
        self.NomeMeioMae = NomeMeioMae
        self.UltimoNomeMae = UltimoNomeMae       

        self.Logradouro = Logradouro
        self.Numero = Numero
        self.Bairro = Bairro
        self.Complemento = Complemento
        self.Cidade = Cidade
        self.CEP = CEP
        self.Estado = Estado  
    
