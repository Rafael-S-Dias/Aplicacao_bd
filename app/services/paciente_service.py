from models.paciente_models import Paciente
from repositories.paciente_repository import PacienteRepository
from datetime import datetime

class PacienteService:
    def __init__(self, repository: PacienteRepository) -> None:
        self.repository = repository

    def criar_paciente(self) :
        try:
            cpf = input("Digite seu CPF: ")
            ciptea = input("Digite seu CIPTEA: ")
            data_nascimento = input("Digite sua data de nascimento (DD-MM-AAAA): ")
            
            try:
                data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y").date()
            except ValueError:
                print("Data de nascimento inválida! Use o formato DD-MM-AAAA.")
                return
            
            primeiro_nome = input("Digite seu primeiro nome: ")
            nome_meio = input("Digite seu nome do meio (opcional): ")
            ultimo_nome = input("Digite seu último nome: ")

            primeiro_nome_pai = input("Digite o primeiro nome do pai do paciente: ")
            nome_meio_pai = input("Digite o nome do meio do pai do paciente (opcional): ")
            ultimo_nome_pai = input("Digite o último nome do pai do paciente: ")

            primeiro_nome_mae = input("Digite o primeiro nome da mãe do paciente: ")
            nome_meio_mae = input("Digite o nome do meio da mãe do paciente (opcional): ")
            ultimo_nome_mae = input("Digite o último nome da mãe do paciente: ")
            
            numero = input("Digite o número da sua rua: ")
            complemento = input("Digite o complemento: ")
            cidade = input("Digite o nome da sua cidade: ")
            cep = input("Digite seu CEP: ")
            estado = input("Digite o seu estado: ")
            logradouro = input("Digite o logradouro: ")

            paciente = Paciente( cpf = cpf, ciptea = ciptea, dataNascimento = data_nascimento, primeiroNome = primeiro_nome, nomeMeio = nome_meio, ultimoNome = ultimo_nome,
                                 primeiroNomePa = primeiro_nome_pai, nomeMeioPai = nome_meio_pai, ultimoNomePai = ultimo_nome_pai, 
                                 primeiroNomeMae = primeiro_nome_mae, nomeMeioMae = nome_meio_mae, ultimoNomeMae = ultimo_nome_mae,
                                 numero = numero, complemento = complemento, cidade = cidade, cep = cep, estado = estado, logradouro = logradouro  )

            cadastro = self.repository.pesquisar_paciente_por_cpf(cpf = Paciente.cpf)
            if cadastro:
                print("Paciente já cadastrado! Tente novamente")
                return

            self.repository.criar_paciente(paciente)
            print("Paciente criado com sucesso")
        except TypeError as e:
            print(f"Erro ao salvar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def deletar_paciente(self):
        try:
            cpf = input("Digite o cpf do Paciente que deseja deletar: ")

            cadastro = self.repository.pesquisar_paciente_por_cpf(cpf)
            if cadastro:
                self.repository.deletar_paciente(cadastro)
                print("Paciente deletado com sucesso")
                return
        
            print("Paciente não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def atualizar_paciente(self):
        try:
            cpf = input("Digite o CPF do paciente que deseja atualizar: ")

            cadastro = self.repository.pesquisar_paciente_por_cpf(cpf)
            if cadastro:
                cadastro.ciptea = input("Digite seu CIPTEA: ")
                cadastro.data_nascimento = input("Digite sua data de nascimento (DD-MM-AAAA): ")
                cadastro.primeiro_nome = input("Digite seu primeiro nome: ")
                cadastro.nome_meio = input("Digite seu nome do meio (opcional): ")
                cadastro.ultimo_nome = input("Digite seu último nome: ")

                cadastro.primeiro_nome_pai = input("Digite o primeiro nome do pai do paciente: ")
                cadastro.nome_meio_pai = input("Digite o nome do meio do pai do paciente (opcional): ")
                cadastro.ultimo_nome_pai = input("Digite o último nome do pai do paciente: ")

                cadastro.primeiro_nome_mae = input("Digite o primeiro nome da mãe do paciente: ")
                cadastro.nome_meio_mae = input("Digite o nome do meio da mãe do paciente (opcional): ")
                cadastro.ultimo_nome_mae = input("Digite o último nome da mãe do paciente: ")
                
                cadastro.numero = input("Digite o número da sua rua: ")
                cadastro.complemento = input("Digite o complemento: ")
                cadastro.cidade = input("Digite o nome da sua cidade: ")
                cadastro.cep = input("Digite seu CEP: ")
                cadastro.estado = input("Digite o seu estado: ")
                cadastro.logradouro = input("Digite o logradouro: ")
                
                self.repository.atualizar_paciente(cadastro)
                print("Paciente atualizado com sucesso")
                return
            
            print("Paciente não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    def pesquisar_paciente(self):
        try:
            cpf = input("Digite o cpf do paciente que deseja pesquisar: ")

            cadastro = self.repository.pesquisar_paciente_por_cpf(cpf)
            if cadastro:
                print("Dados do Paciente: ")
                print(f"\n CPF: {cadastro.cpf} | CIPTEA: {cadastro.ciptea} | Nome: {cadastro.primeiroNome} | Sobrenome: {cadastro.ultimoNome}")
                return
            
            print("Paciente não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    def listar_todos_pacientes(self):
        return self.repository.listar_todos_pacientes()