from models.consultas_models import Consultas
from repositories.consultas_repository import ConsultasRepository
from datetime import datetime

class ConsultasService:
    def __init__(self, repository: ConsultasRepository) -> None:
        self.repository = repository

    def criar_consultas(self) :
        try:
            data = input("Digite a data da consulta (DD-MM-AAAA): ")
            local = input("Digite o local da consulta: ")
            sala = input("Digite a sala da consulta: ")
            horario = input("Digite o horário da consulta (HH:MM): ")

            try:
                data = datetime.strptime(data, "%d-%m-%Y").date()
                horario = datetime.strptime(horario, "%H:%M").time()
            except ValueError:
                print("Data ou horário inválidos! Use os formatos DD-MM-AAAA e HH:MM.")
                return

            consulta = Consultas(data=data, local=local, sala=sala, horario=horario)

            cadastro = self.repository.pesquisar_consultas_por_id(id = consulta.id)
            if cadastro:
                print("Consulta já cadastrada! Tente novamente")
                return

            self.repository.criar_consultas(consulta)
            print("Consulta criada com sucesso")
        except TypeError as e:
            print(f"Erro ao salvar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def deletar_consultas(self):
        try:
            id = input("Digite o ID do médico que deseja deletar: ")

            cadastro = self.repository.pesquisar_consultas_por_id(id)
            if cadastro:
                self.repository.deletar_consultas(cadastro)
                print("Consulta deletada com sucesso")
                return
           
            print("Consulta não encontrada")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def atualizar_consultas(self):
        try:
            id = input("Digite o ID da consulta que deseja atualizar: ")

            cadastro = self.repository.pesquisar_consultas_por_id(id)
            if cadastro:
                cadastro.data = input("Digite a nova data da consulta (DD-MM-AAAA): ")
                cadastro.local = input("Digite o novo local da consulta: ")
                cadastro.sala = input("Digite a nova sala da consulta: ")
                cadastro.horario = input("Digite o novo horário da consulta (HH:MM): ")
 
                self.repository.atualizar_consultas(cadastro)
                print("Consulta atualizada com sucesso")
                return
            
            print("Consulta não encontrada")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def pesquisar_consultas(self):
        try:
            id = input("Digite o ID da consulta que deseja pesquisar: ")

            cadastro = self.repository.pesquisar_consultas_por_id(id)
            if cadastro:
                print("Dados da Consulta: ")
                print(f"\n Data: {cadastro.data} | Local: {cadastro.local} | Sala: {cadastro.sala} | Horario: {cadastro.horario}")
                return
            
            print("Consulta não encontrada")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    def listar_todas_consultas(self):
        return self.repository.listar_todos_medicos()