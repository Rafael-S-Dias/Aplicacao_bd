from models.retirada_models import Retirada
from repositories.retirada_repository import RetiradaRepository
from datetime import datetime

class retiradaService:
    def __init__(self, repository: RetiradaRepository) -> None:
        self.repository = repository

    def criar_retirada(self) :
        try:
            data = input("Digite a data da receita (DD-MM-AAAA): ")
            local = input("Digite o local da receita: ")
            receita = input("Digite a receita da retirada: ")

            try:
                data = datetime.strptime(data, "%d-%m-%Y").date()
                horario = datetime.strptime(horario, "%H:%M").time()
            except ValueError:
                print("Data ou horário inválidos! Use os formatos DD-MM-AAAA e HH:MM.")
                return

            receita = Retirada(data=data, local=local, receita = receita)

            cadastro = self.repository.pesquisar_retirada_por_id(id = receita.id)
            if cadastro:
                print("Retirada já cadastrada! Tente novamente")
                return

            self.repository.criar_retirada(receita)
            print("Receita criada com sucesso")
        except TypeError as e:
            print(f"Erro ao salvar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def deletar_retirada(self):
        try:
            id = input("Digite o ID da retirada que deseja deletar: ")

            cadastro = self.repository.pesquisar_retirada_por_id(id)
            if cadastro:
                self.repository.deletar_retirada(cadastro)
                print("Receita deletada com sucesso")
                return
           
            print("Receita não encontrada")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def atualizar_retirada(self):
        try:
            id = input("Digite o ID da consulta que deseja atualizar: ")

            cadastro = self.repository.pesquisar_retirada_por_id(id)
            if cadastro:
                cadastro.data = input("Digite a nova data da retirada (DD-MM-AAAA): ")
                cadastro.local = input("Digite o novo local da retirada: ")
                cadastro.sala = input("Digite a nova sala da retirada: ")
                cadastro.receita = input("Digite a nova receita da retirada: ")
 
                self.repository.atualizar_retirada(cadastro)
                print("Receita atualizada com sucesso")
                return
            
            print("Receita não encontrada")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def pesquisar_retirada(self):
        try:
            id = input("Digite o ID da consulta que deseja pesquisar: ")

            cadastro = self.repository.pesquisar_retirada_por_id(id)
            if cadastro:
                print("Dados da Receita: ")
                print(f"\n Data: {cadastro.data} | Local: {cadastro.local} | Sala: {cadastro.sala} | Receita: {cadastro.receita}")
                return
            
            print("Receita não encontrada")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    def listar_todas_retirada(self):
        return self.repository.listar_todos_medicos()