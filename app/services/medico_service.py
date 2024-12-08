from models.medico_models import Medico
from repositories.medico_repository import MedicoRepository

class MedicoService:
    def __init__(self, repository: MedicoRepository) -> None:
        self.repository = repository

    def criar_medico(self) :
        try:
            crm = input("Digite o CRM do médico: ")
            primeiro_nome = input("Digite o primeiro nome do médico: ")
            nome_meio = input("Digite seu nome do meio do médico (opcional): ")
            ultimo_nome = input("Digite seu último nome do médico: ")
            especialidade = input("Digite a especialidade do médico: ")

            medico = Medico(crm = crm, primeiroNome = primeiro_nome, nomeMeio = nome_meio, ultimoNome = ultimo_nome, especialiadade = especialidade)

            cadastro = self.repository.pesquisar_medico_por_crm(crm = medico.crm)
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
            crm = input("Digite o CRM do médico que deseja deletar: ")

            cadastro = self.repository.pesquisar_medico_por_crm(crm)
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
            crm = input("Digite o CRM do médico que deseja atualizar: ")

            cadastro = self.repository.pesquisar_medico_por_crm(crm)
            if cadastro:
                cadastro.primeiro_nome = input("Digite o primeiro nome do médico: ")
                cadastro.nome_meio = input("Digite seu nome do meio do médico (opcional): ")
                cadastro.ultimo_nome = input("Digite seu último nome do médico: ")
                cadastro.especialidade = input("Digite a especialidade do médico: ")
 
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
                print(f"\n CRM: {cadastro.crm} | Nome: {cadastro.primeiroNome} | Sobrenome: {cadastro.ultimoNome} | Especialidade: {cadastro.especialiadade}")
                return
            
            print("Médico não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    def listar_todos_medicos(self):
        return self.repository.listar_todos_medicos()