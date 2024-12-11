from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Responsavel(Base):
    __tablename__ = "responsavel"

    id = Column(Integer, primary_key=True, autoincrement=True)
    PrimeiroNomeResponsavel = Column (String(30), nullable=False)
    NomeMeioResponsavel = Column (String(30), nullable=False)
    UltimoNomeResponsavel = Column (String(30), nullable=False)
    Email = Column(String(50), unique=True, nullable=False, name="Email")
    Senha = Column(String(20), nullable=False)
    DDD = Column(String(3), nullable=False)
    NumTelefone = Column(String(13), nullable=False, name="NumTelefone")
 

    def __init__(self, PrimeiroNomeResponsavel : str, NomeMeioResponsavel : str, UltimoNomeResponsavel : str, Email: str, Senha: str, DDD: int, NumTelefone: str):
        self.PrimeiroNomeResponsavel = PrimeiroNomeResponsavel
        self.NomeMeioResponsavel =  NomeMeioResponsavel
        self.UltimoNomeResponsavel = UltimoNomeResponsavel
        self.Email = Email
        self.Senha = Senha
        self.DDD = DDD
        self.NumTelefone = NumTelefone
