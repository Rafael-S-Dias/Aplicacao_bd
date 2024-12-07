from models.responsavel_models import Responsavel
from sqlalchemy.orm import Session

class ResponsavelRepository: 
    def __init__(self, session: Session):
        self.session = session

    def criar_responsavel(self, responsavel: Responsavel):
        self.session.add(responsavel)
        self.session.commit()
        self.session.refresh(responsavel)

    def atualizar_responsavel(self, responsavel: Responsavel):
        self.session.commit()
        self.session.refresh(responsavel)

    def pesquisar_responsavel_por_email(self,email:str):
        return self.session.query(Responsavel).filter_by(email = email).first()

    def deletar_responsavel(self, responsavel):
        self.session.delete(responsavel)
        self.session.commit()

    def listar_todos_responsavels(self):
        return self.session.query(Responsavel).all()