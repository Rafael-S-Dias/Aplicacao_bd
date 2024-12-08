from models.consultas_models import Consultas
from sqlalchemy.orm import Session

class ConsultasRepository: 
    def __init__(self, session: Session):
        self.session = session

    def criar_consultas(self, consultas: Consultas):
        self.session.add(consultas)
        self.session.commit()
        self.session.refresh(consultas)

    def atualizar_consultas(self, consultas: Consultas):
        self.session.commit()
        self.session.refresh(consultas)

    def pesquisar_consultas_por_id(self,id:int):
        return self.session.query(Consultas).filter_by(id = id).first()

    def deletar_consultas(self, consultas):
        self.session.delete(consultas)
        self.session.commit()

    def listar_todos_consultass(self):
        return self.session.query(Consultas).all()