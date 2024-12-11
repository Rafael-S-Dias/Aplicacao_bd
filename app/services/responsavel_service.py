from models.responsavel_models import Responsavel
from repositories.responsavel_repository import ResponsavelRepository

class ResponsavelService:
    def __init__(self, repository: ResponsavelRepository) -> None:
        self.repository = repository

    def login_responsavel(self, Email: str, Senha: str):
        responsavel = self.repository.pesquisar_responsavel_por_email(Email)
        if responsavel and responsavel.Senha == Senha:
            return responsavel
        return None

    def criar_responsavel(self) :
        try:
            PrimeiroNomeResponsavel = input("Digite o primeiro nome do responsavel: ")
            NomeMeioResponsavel = input("Digite o nome do meio do responsavel: ")
            UltimoNomeResponsavel = input("Digite o ultimo nome do responsavel: ")
            Email = input("Digite seu e-mail: ")
            Senha = input("Defina sua senha: ")
            DDD = input("Digite seu DDD: ")
            NumTelefone = input("Digite o número do seu telefone: ")

            responsavel = Responsavel(PrimeiroNomeResponsavel = PrimeiroNomeResponsavel, NomeMeioResponsavel = NomeMeioResponsavel, UltimoNomeResponsavel = UltimoNomeResponsavel,  Email = Email, Senha = Senha, DDD = DDD, NumTelefone = NumTelefone)

            cadastro = self.repository.pesquisar_responsavel_por_email(Email = responsavel.Email)
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
            Email = input("Digite o email do responsável que deseja deletar: ")

            cadastro = self.repository.pesquisar_responsavel_por_email(Email)
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
            Email = input("Digite o email do responsável que deseja atualizar: ")

            cadastro = self.repository.pesquisar_responsavel_por_email(Email)
            if cadastro:
                cadastro.Email = input("Digite o novo e-mail: ")
                cadastro.Senha = input("Digite a nova senha: ")
                cadastro.DDD = input("Digite seu novo DDD: ")
                cadastro.NumTelefone = input("Digite o número do seu novo telefone: ")

                
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
            Email = input("Digite o email do responsável que deseja pesquisar: ")

            cadastro = self.repository.pesquisar_responsavel_por_email(Email)
            if cadastro:
                print("Dados do Responsável: ")
                print((f"\n Id: {cadastro.IdResponsavel} | Nome: {cadastro.PrimeiroNomeResponsavel} | Sobrenome: {cadastro.UltimoNomeResponsavel} | Email: {cadastro.Email} | DDD: {cadastro.DDD} | Telefone: {cadastro.NumTelefone}"))
                return
            
            print("Responsável não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    def listar_todos_responsaveis(self):
        return self.repository.listar_todos_responsaveis()