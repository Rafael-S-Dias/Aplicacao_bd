from models.paciente_models import Paciente
from sqlalchemy.orm import Session

class PacienteRepository: 
    def __init__(self, session: Session):
        self.session = session

    def criar_paciente(self, paciente: Paciente):
        self.session.add(paciente)
        self.session.commit()
        self.session.refresh(paciente)

    def atualizar_paciente(self, paciente: Paciente):
        self.session.commit()
        self.session.refresh(paciente)

    def pesquisar_paciente_por_cpf(self,cpf:str):
        return self.session.query(Paciente).filter_by(cpf = cpf).first()

    def deletar_paciente(self, paciente):
        self.session.delete(paciente)
        self.session.commit()

    def listar_todos_pacientes(self):
        return self.session.query(Paciente).all()