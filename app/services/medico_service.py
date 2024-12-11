from models.medico_models import Medico
from repositories.medico_repository import MedicoRepository

class MedicoService:
    def __init__(self, repository: MedicoRepository) -> None:
        self.repository = repository

    def criar_medico(self) :
        try:
            CRM = input("Digite o CRM do médico: ")
            PrimeiroNomeMedico = input("Digite o primeiro nome do médico: ")
            NomeMeioMedico = input("Digite seu nome do meio do médico (opcional): ")
            UltimoNomeMedico = input("Digite seu último nome do médico: ")
            Especializacao = input("Digite a especialidade do médico: ")

            medico = Medico(CRM = CRM, PrimeiroNomeMedico = PrimeiroNomeMedico, NomeMeioMedico = NomeMeioMedico, UltimoNomeMedico = UltimoNomeMedico, Especializacao = Especializacao)

            cadastro = self.repository.pesquisar_medico_por_crm(CRM = medico.CRM)
            if cadastro:
                print("Médico já cadastrado! Tente novamente")
                return

            self.repository.criar_medico(medico)
            print("Médico criado com sucesso")
        except TypeError as e:
            print(f"Erro ao salvar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def deletar_medico(self):
        try:
            CRM = input("Digite o CRM do médico que deseja deletar: ")

            cadastro = self.repository.pesquisar_medico_por_crm(CRM)
            if cadastro:
                self.repository.deletar_medico(cadastro)
                print("Médico deletado com sucesso")
                return
           
            print("Médico não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def atualizar_medico(self):
        try:
            CRM = input("Digite o CRM do médico que deseja atualizar: ")

            cadastro = self.repository.pesquisar_medico_por_crm(CRM)
            if cadastro:
                cadastro.PrimeiroNomeMedico = input("Digite o primeiro nome do médico: ")
                cadastro.NomeMeioMedico = input("Digite seu nome do meio do médico (opcional): ")
                cadastro.UltimoNomeMedico = input("Digite seu último nome do médico: ")
                cadastro.Especializacao = input("Digite a especialidade do médico: ")
 
                self.repository.atualizar_medico(cadastro)
                print("Médico atualizado com sucesso")
                return
            
            print("Médico não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def pesquisar_medico(self):
        try:
            crm = input("Digite o CRM do médico que deseja pesquisar: ")

            cadastro = self.repository.pesquisar_medico_por_crm(crm)
            if cadastro:
                print("Dados do Médico: ")
                print(f"\n CRM: {cadastro.CRM} | Nome: {cadastro.PrimeiroNomeMedico} | Sobrenome: {cadastro.UltimoNomeMedico} | Especialidade: {cadastro.Especializacao}")
                return
            
            print("Médico não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    def listar_todos_medicos(self):
        return self.repository.listar_todos_medicos()