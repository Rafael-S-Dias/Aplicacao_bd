from models.medico_models import Medico
from sqlalchemy.orm import Session

class MedicoRepository: 
    def __init__(self, session: Session):
        self.session = session

    def criar_medico(self, medico: Medico):
        self.session.add(medico)
        self.session.commit()
        self.session.refresh(medico)

    def atualizar_medico(self, medico: Medico):
        self.session.commit()
        self.session.refresh(medico)

    def pesquisar_medico_por_crm(self,CRM:str):
        return self.session.query(Medico).filter_by(CRM = CRM).first()

    def deletar_medico(self, medico):
        self.session.delete(medico)
        self.session.commit()

    def listar_todos_medicos(self):
        return self.session.query(Medico).all()