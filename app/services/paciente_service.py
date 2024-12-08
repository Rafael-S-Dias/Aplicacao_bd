from models.paciente_models import Paciente
from repositories.paciente_repository import PacienteRepository
from datetime import datetime

class ResponsavelService:
    def __init__(self, repository: ResponsavelRepository) -> None:
        self.repository = repository

    def criar_responsavel(self) :
            try:
                cpf = input("Digite seu CPF: ")
                email = input("Digite seu e-mail: ")
                data_nascimento = input("Digite sua data de nascimento (DD-MM-AAAA): ")
                primeiro_nome = input("Digite seu primeiro nome: ")
                nome_meio = input("Digite seu nome do meio (opcional): ")
                ultimo_nome = input("Digite seu último nome: ")

                try:
                    data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y").date()
                except ValueError:
                    print("Data de nascimento inválida! Use o formato DD-MM-AAAA.")
                    return

                responsavel = Responsavel( cpf=cpf, email=email, dataNascimento=data_nascimento, primeiroNome=primeiro_nome, nomeMeio=nome_meio, ultimoNome=ultimo_nome )

                cadastro = self.repository.pesquisar_responsavel_por_email(email=responsavel.email)
                if cadastro:
                    print("Usuário já cadastrado")
                    return

                self.repository.criar_responsavel(responsavel)
                print("Responsavel criado com sucesso")
            except TypeError as e:
                print(f"Erro ao salvar o arquivo: {e}")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")

        def deletar_responsavel(self):
            try:
                email = input("Digite o email do usuário que deseja deletar: ")

                cadastro = self.repository.pesquisar_responsavel_por_email(email)
                if cadastro:
                    self.repository.deletar_responsavel(cadastro)
                    print("Usuário deletado com sucesso")
                    return
            
                print("Usuário não encontrado")
            except TypeError as e:
                print(f"Erro ao deletar o arquivo: {e}")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")

        def atualizar_responsavel(self):
            try:
                email = input("Digite o email do usuário que deseja atualizar: ")

                cadastro = self.repository.pesquisar_responsavel_por_email(email)
                if cadastro:
                    cadastro.nome = input("Digite o novo nome: ")
                    cadastro.email = input("Digite o novo e-mail: ")
                    cadastro.senha = input("Digite a nova senha: ")
                    
                    self.repository.atualizar_responsavel(cadastro)
                    print("Usuário atualizado com sucesso")
                    return
                
                print("Usuário não encontrado")
            except TypeError as e:
                print(f"Erro ao deletar o arquivo: {e}")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")

        def pesquisar_responsavel(self):
            try:
                email = input("Digite o email do usuário que deseja pesquisar: ")

                cadastro = self.repository.pesquisar_responsavel_por_email(email)
                if cadastro:
                    print("Dados do usuário: ")
                    print(f"\n Id: {cadastro.id} | Nome: {cadastro.nome} | Email: {cadastro.email}")
                    return
                
                print("Usuário não encontrado")
            except TypeError as e:
                print(f"Erro ao deletar o arquivo: {e}")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")


        def listar_todos_responsaveis(self):
            return self.repository.listar_todos_responsaveis()