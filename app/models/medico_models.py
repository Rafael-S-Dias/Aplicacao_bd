from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Medico(Base):
    __tablename__ = "medico"

    CRM = Column(String(15), unique=True, primary_key=True, nullable=False)
    PrimeiroNomeMedico = Column(String(20), nullable=False)
    NomeMeioMedico = Column(String(20), nullable=False)
    UltimoNomeMedico = Column(String(20), nullable=False)
    Especializacao = Column(String(20), nullable=False)

    def __init__(self, CRM: str, PrimeiroNomeMedico: str, NomeMeioMedico: str, UltimoNomeMedico: str, Especializacao: str):
        self.CRM = CRM
        self.PrimeiroNomeMedico = PrimeiroNomeMedico
        self.NomeMeioMedico = NomeMeioMedico
        self.UltimoNomeMedico = UltimoNomeMedico
        self.Especializacao = Especializacao