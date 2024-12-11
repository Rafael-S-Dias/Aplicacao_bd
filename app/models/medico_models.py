from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Medico(Base):
    __tablename__ = "medico"

    CRM = Column(String(30), unique=True, primary_key=True)
    PrimeiroNomeMedico = Column(String(30), nullable=False)
    NomeMeioMedico = Column(String(30))
    UltimoNomeMedico = Column(String(30), nullable=False)
    Especializacao = Column(String(30), nullable=False)

    def __init__(self, CRM: str, PrimeiroNomeMedico: str, NomeMeioMedico: str, UltimoNomeMedico: str, Especializacao: str):
        self.CRM = CRM
        self.PrimeiroNomeMedico = PrimeiroNomeMedico
        self.NomeMeioMedico = NomeMeioMedico
        self.UltimoNomeMedico = UltimoNomeMedico
        self.Especializacao = Especializacao