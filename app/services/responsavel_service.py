from models.responsavel_models import Responsavel
from repositories.responsavel_repository import ResponsavelRepository

class ResponsavelService:
    def __init__(self, repository: ResponsavelRepository) -> None:
        self.repository = repository

    def criar_responsavel(self) :
        try:
            email = input("Digite seu e-mail: ")
            senha = input("Defina sua senha: ")
            ddd = input("Digite seu DDD: ")
            telefone = input("Digite o número do seu telefone: ")

            responsavel = Responsavel(email = email, senha = senha, ddd =ddd, telefone = telefone)

            cadastro = self.repository.pesquisar_responsavel_por_email(email = responsavel.email)
            if cadastro:
                print("Responsavel já cadastrado! Tente novamente")
                return

            self.repository.criar_responsavel(responsavel)
            print("Responsável criado com sucesso")
        except TypeError as e:
            print(f"Erro ao salvar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def deletar_responsavel(self):
        try:
            email = input("Digite o email do responsável que deseja deletar: ")

            cadastro = self.repository.pesquisar_responsavel_por_email(email)
            if cadastro:
                self.repository.deletar_responsavel(cadastro)
                print("Responsável deletado com sucesso")
                return
           
            print("Responsável não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def atualizar_responsavel(self):
        try:
            email = input("Digite o email do responsável que deseja atualizar: ")

            cadastro = self.repository.pesquisar_responsavel_por_email(email)
            if cadastro:
                cadastro.email = input("Digite o novo e-mail: ")
                cadastro.senha = input("Digite a nova senha: ")
                cadastro.ddd = input("Digite seu novo DDD: ")
                cadastro.telefone = input("Digite o número do seu novo telefone: ")

                
                self.repository.atualizar_responsavel(cadastro)
                print("Responsável atualizado com sucesso")
                return
            
            print("Responsável não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def pesquisar_responsavel(self):
        try:
            email = input("Digite o email do responsável que deseja pesquisar: ")

            cadastro = self.repository.pesquisar_responsavel_por_email(email)
            if cadastro:
                print("Dados do Responsável: ")
                print(f"\n Id: {cadastro.id} | Email: {cadastro.email} | DDD: {cadastro.ddd}| Email: {cadastro.email}")
                return
            
            print("Responsável não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    def listar_todos_responsaveis(self):
        return self.repository.listar_todos_responsaveis()