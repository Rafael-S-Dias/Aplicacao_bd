from models.retirada_models import Retirada
from sqlalchemy.orm import Session

class RetiradaRepository: 
    def __init__(self, session: Session):
        self.session = session

    def criar_retirada(self, retirada: Retirada):
        self.session.add(retirada)
        self.session.commit()
        self.session.refresh(retirada)

    def atualizar_retirada(self, retirada: Retirada):
        self.session.commit()
        self.session.refresh(retirada)

    def pesquisar_retirada_por_id(self,id:str):
        return self.session.query(Retirada).filter_by(id = id).first()

    def deletar_retirada(self, retirada):
        self.session.delete(retirada)
        self.session.commit()

    def listar_todas_retiradas(self):
        return self.session.query(Retirada).all()