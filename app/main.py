import os
import time
from services.consultas_service import ConsultasService
from services.medico_service import MedicoService
from services.paciente_service import PacienteService
from services.responsavel_service import ResponsavelService
from services.retirada_service import RetiradaService
from repositories.consultas_repository import ConsultasRepository
from repositories.medico_repository import MedicoRepository
from repositories.paciente_repository import PacienteRepository
from repositories.responsavel_repository import ResponsavelRepository
from repositories.retirada_repository import RetiradaRepository
from config.database import Session
# from datetime import datetime

os.system("cls || clear")

def main():
    session = Session()

    consultas_repository = ConsultasRepository(session)
    medico_repository = MedicoRepository(session)
    paciente_repository = PacienteRepository(session)
    reponsavel_repository = ResponsavelRepository(session)
    retirada_repository = RetiradaRepository(session)

    consultas_service = ConsultasService(consultas_repository)
    medico_service = MedicoService(medico_repository)
    paciente_service = PacienteService(paciente_repository)
    responsavel_service = ResponsavelService(reponsavel_repository)
    retirada_service = RetiradaService(retirada_repository)


    def gerenciar_responsavel():
        while True:
            print("1 - Adicionar responsavel \n2 - Pesquisar um reponsavel \n3 - Atualizar dados de um reponsavel \
                    \n4 - Excluir um reponsavel \n5 - Exibir todos os reponsaveis cadastrados \n0 - Sair")
                
            try:
                opcao = int(input("\nSelecione a opção desejada: "))
            except ValueError:
                os.system("cls || clear")
                print("Comando inválido! Por favor, insira um número inteiro.")
                time.sleep(2)
                continue
            

            match opcao:
                case 1:
                    os.system("cls || clear")
                    responsavel_service.criar_responsavel()
                    time.sleep(2)
                case 2:
                    os.system("cls || clear")
                    responsavel_service.pesquisar_responsavel()
                    time.sleep(2)
                case 3:
                    os.system("cls || clear")
                    responsavel_service.atualizar_responsavel()
                    time.sleep(2)
                case 4: 
                    os.system("cls || clear")
                    responsavel_service.deletar_responsavel()
                    time.sleep(2)
                case 5: 
                    os.system("cls || clear")
                    print("\nListando todos os responsaveis: ")
                    responsaveis = responsavel_service.listar_todos_responsaveis()

                    for responsavel in responsaveis:
                        print(f"Id: {responsavel.id} | Email: {responsavel.email} | DDD: {responsavel.ddd}| Telefone: {responsavel.telefone}") 
                        time.sleep(2)
                case 0:
                    os.system("cls || clear")
                    print("Encerrando programa...")
                    time.sleep(2)
                    print("PROGRAMA FINALIZADO!")
                    return  
                case _:
                    os.system("cls || clear")
                    print("Opção inválida! Por favor, selecione uma opção válida.")
                    time.sleep(2)

    def gerenciar_paciente():
        while True:
            print("1 - Adicionar paciente \n2 - Pesquisar um paciente \n3 - Atualizar dados de um paciente \
                    \n4 - Excluir um paciente \n5 - Exibir todos os pacientes cadastrados \n0 - Sair")
                
            try:
                opcao = int(input("\nSelecione a opção desejada: "))
            except ValueError:
                os.system("cls || clear")
                print("Comando inválido! Por favor, insira um número inteiro.")
                time.sleep(2)
                continue
            

            match opcao:
                case 1:
                    os.system("cls || clear")
                    paciente_service.criar_paciente()
                    time.sleep(2)
                case 2:
                    os.system("cls || clear")
                    paciente_service.pesquisar_paciente()
                    time.sleep(2)
                case 3:
                    os.system("cls || clear")
                    paciente_service.atualizar_paciente()
                    time.sleep(2)
                case 4: 
                    os.system("cls || clear")
                    paciente_service.deletar_paciente()
                    time.sleep(2)
                case 5: 
                    os.system("cls || clear")
                    print("\nListando todos os pacientes: ")
                    pacientes = paciente_service.listar_todos_pacientes()

                    for paciente in pacientes:
                        print(f" CPF: {paciente.cpf} | CIPTEA: {paciente.ciptea} | Nome: {paciente.primeiroNome} | Sobrenome: {paciente.ultimoNome}") 
                        time.sleep(2)
                case 0:
                    os.system("cls || clear")
                    print("Encerrando programa...")
                    time.sleep(2)
                    print("PROGRAMA FINALIZADO!")
                    return  
                case _:
                    os.system("cls || clear")
                    print("Opção inválida! Por favor, selecione uma opção válida.")
                    time.sleep(2)

    def gerenciar_consultas():
        while True:
            print("1 - Adicionar consultas \n2 - Pesquisar um consultas \n3 - Atualizar dados de um consultas \
                    \n4 - Excluir um consultas \n5 - Exibir todos os consultas cadastrados \n0 - Sair")
                
            try:
                opcao = int(input("\nSelecione a opção desejada: "))
            except ValueError:
                os.system("cls || clear")
                print("Comando inválido! Por favor, insira um número inteiro.")
                time.sleep(2)
                continue
            

            match opcao:
                case 1:
                    os.system("cls || clear")
                    consultas_service.criar_consultas()
                    time.sleep(2)
                case 2:
                    os.system("cls || clear")
                    consultas_service.pesquisar_consultas()
                    time.sleep(2)
                case 3:
                    os.system("cls || clear")
                    consultas_service.atualizar_consultas()
                    time.sleep(2)
                case 4: 
                    os.system("cls || clear")
                    consultas_service.deletar_consultas()
                    time.sleep(2)
                case 5: 
                    os.system("cls || clear")
                    print("\nListando todos os consultas: ")
                    consultas = consultas_service.listar_todas_consultas()

                    for consultas in consultas:
                        print(f" Data: {consultas.data} | Local: {consultas.local} | Sala: {consultas.sala} | Horario: {consultas.horario}") 
                        time.sleep(2)
                case 0:
                    os.system("cls || clear")
                    print("Encerrando programa...")
                    time.sleep(2)
                    print("PROGRAMA FINALIZADO!")
                    return  
                case _:
                    os.system("cls || clear")
                    print("Opção inválida! Por favor, selecione uma opção válida.")
                    time.sleep(2)

    def gerenciar_retiradas():
        while True:
            print("1 - Adicionar retirada \n2 - Pesquisar um retirada \n3 - Atualizar dados de um retirada \
                    \n4 - Excluir um retirada \n5 - Exibir todos os retiradas cadastrados \n0 - Sair")
                
            try:
                opcao = int(input("\nSelecione a opção desejada: "))
            except ValueError:
                os.system("cls || clear")
                print("Comando inválido! Por favor, insira um número inteiro.")
                time.sleep(2)
                continue
            

            match opcao:
                case 1:
                    os.system("cls || clear")
                    retirada_service.criar_retirada()
                    time.sleep(2)
                case 2:
                    os.system("cls || clear")
                    retirada_service.pesquisar_retirada()
                    time.sleep(2)
                case 3:
                    os.system("cls || clear")
                    retirada_service.atualizar_retirada()
                    time.sleep(2)
                case 4: 
                    os.system("cls || clear")
                    retirada_service.deletar_retirada()
                    time.sleep(2)
                case 5: 
                    os.system("cls || clear")
                    print("\nListando todos os retiradas: ")
                    retiradas = retirada_service.listar_todas_retiradas()

                    for retirada in retiradas:
                        print(f"Data: {retirada.data} | Local: {retirada.local} | Sala: {retirada.sala} | Receita: {retirada.receita}") 
                        time.sleep(2)
                case 0:
                    os.system("cls || clear")
                    print("Encerrando programa...")
                    time.sleep(2)
                    print("PROGRAMA FINALIZADO!")
                    return  
                case _:
                    os.system("cls || clear")
                    print("Opção inválida! Por favor, selecione uma opção válida.")
                    time.sleep(2)

    def gerenciar_medicos():
        while True:
            print("1 - Adicionar medico \n2 - Pesquisar um medico \n3 - Atualizar dados de um medico \
                    \n4 - Excluir um medico \n5 - Exibir todos os medicos cadastrados \n0 - Sair")
                
            try:
                opcao = int(input("\nSelecione a opção desejada: "))
            except ValueError:
                os.system("cls || clear")
                print("Comando inválido! Por favor, insira um número inteiro.")
                time.sleep(2)
                continue
            

            match opcao:
                case 1:
                    os.system("cls || clear")
                    medico_service.criar_medico()
                    time.sleep(2)
                case 2:
                    os.system("cls || clear")
                    medico_service.pesquisar_medico()
                    time.sleep(2)
                case 3:
                    os.system("cls || clear")
                    medico_service.atualizar_medico()
                    time.sleep(2)
                case 4: 
                    os.system("cls || clear")
                    medico_service.deletar_medico()
                    time.sleep(2)
                case 5: 
                    os.system("cls || clear")
                    print("\nListando todos os medicos: ")
                    medicos = medico_service.listar_todos_medicos()

                    for medico in medicos:
                        print(f" CRM: {medico.crm} | Nome: {medico.primeiroNome} | Sobrenome: {medico.ultimoNome} | Especialidade: {medico.especialiadade}") 
                        time.sleep(2)
                case 0:
                    os.system("cls || clear")
                    print("Encerrando programa...")
                    time.sleep(2)
                    print("PROGRAMA FINALIZADO!")
                    return  
                case _:
                    os.system("cls || clear")
                    print("Opção inválida! Por favor, selecione uma opção válida.")
                    time.sleep(2)


    def menu():
        while True:
            print("======== NUZA =========")
            print("BEM VINDO!")
            while True:
                email = input("Digite seu e-mail: ")
                senha = input("Digite sua senha: ")

                responsavel = responsavel_service.login_responsavel(email, senha)
                if responsavel:
                    print(f"Login bem-sucedido! Bem-vindo, {responsavel.email}.")
                    break
                else:
                    print("Credenciais inválidas. Tente novamente.")


            print("1 - Gerenciar responsaveis \n2 - Gerenciar pacientes \n3 - Gerenciar consultas \n4 - Gerenciar retiradas \
                  \n5 - Gerenciar médicos \n0 - Sair")
            
            try:
                opcao = int(input("\nSelecione a opção desejada: "))
            except ValueError:
                os.system("cls || clear")
                print("Comando inválido! Por favor, insira um número inteiro.")
                time.sleep(2)
                continue

            match opcao:
                case 1:
                    os.system("cls || clear")
                    gerenciar_responsavel()
                    time.sleep(2)
                case 2:
                    os.system("cls || clear")
                    gerenciar_paciente()
                    time.sleep(2)
                case 3:
                    os.system("cls || clear")
                    gerenciar_consultas()
                    time.sleep(2)
                case 4: 
                    os.system("cls || clear")
                    gerenciar_retiradas()
                    time.sleep(2)
                case 5: 
                    os.system("cls || clear")
                    gerenciar_medicos()
                    time.sleep(2)
                case 0:
                    os.system("cls || clear")
                    print("Encerrando programa...")
                    time.sleep(2)
                    print("PROGRAMA FINALIZADO!")
                    return  
                case _:
                    os.system("cls || clear")
                    print("Opção inválida! Por favor, selecione uma opção válida.")
                    time.sleep(2)
            


    menu()

if __name__ == "__main__":
        main()