from models.paciente_models import Paciente
from repositories.paciente_repository import PacienteRepository
from datetime import datetime

class PacienteService:
    def __init__(self, repository: PacienteRepository) -> None:
        self.repository = repository

    def criar_paciente(self) :
        try:
            CPF = input("Digite seu CPF: ")
            CIPTEA = input("Digite seu CIPTEA: ")
            DataNascimento = input("Digite sua data de nascimento (DD-MM-AAAA): ")
            
            try:
                DataNascimento = datetime.strptime(DataNascimento, "%d-%m-%Y").date()
            except ValueError:
                print("Data de nascimento inválida! Use o formato DD-MM-AAAA.")
                return
            
            PrimeiroNomePaciente = input("Digite seu primeiro nome: ")
            NomeMeioPaciente = input("Digite seu nome do meio (opcional): ")
            UltimoNomePaciente = input("Digite seu último nome: ")

            PrimeiroNomePai = input("Digite o primeiro nome do pai do paciente: ")
            NomeMeioPai = input("Digite o nome do meio do pai do paciente (opcional): ")
            UltimoNomePai = input("Digite o último nome do pai do paciente: ")

            PrimeiroNomeMae = input("Digite o primeiro nome da mãe do paciente: ")
            NomeMeioMae = input("Digite o nome do meio da mãe do paciente (opcional): ")
            UltimoNomeMae = input("Digite o último nome da mãe do paciente: ")
            
            Logradouro = input("Digite o logradouro: ")
            Numero = input("Digite o número da sua rua: ")
            Bairro = input("Digite o seu bairro: ")
            Complemento = input("Digite o complemento: ")
            Cidade = input("Digite o nome da sua cidade: ")
            CEP = input("Digite seu CEP: ")
            Estado = input("Digite o seu estado: ")

            paciente = Paciente( CPF = CPF, CIPTEA = CIPTEA, DataNascimento = DataNascimento, PrimeiroNomePaciente = PrimeiroNomePaciente, NomeMeioPaciente = NomeMeioPaciente, UltimoNomePaciente = UltimoNomePaciente,
                                 PrimeiroNomePai = PrimeiroNomePai, NomeMeioPai = NomeMeioPai, UltimoNomePai = UltimoNomePai, 
                                 PrimeiroNomeMae = PrimeiroNomeMae, NomeMeioMae = NomeMeioMae, UltimoNomeMae = UltimoNomeMae,
                                 Logradouro = Logradouro, Numero = Numero, Bairro = Bairro, Complemento = Complemento, Cidade = Cidade, CEP = CEP, Estado = Estado )

            cadastro = self.repository.pesquisar_paciente_por_cpf(CPF = Paciente.CPF)
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
            CPF = input("Digite o cpf do Paciente que deseja deletar: ")

            cadastro = self.repository.pesquisar_paciente_por_cpf(CPF)
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
            CPF = input("Digite o CPF do paciente que deseja atualizar: ")

            cadastro = self.repository.pesquisar_paciente_por_cpf(CPF)
            if cadastro:
                cadastro.CIPTEA = input("Digite seu CIPTEA: ")
                cadastro.DataNascimento = input("Digite sua data de nascimento (DD-MM-AAAA): ")
                cadastro.PrimeiroNomePaciente = input("Digite o primeiro nome do paciente: ")
                cadastro.NomeMeioPaciente = input("Digite o nome do meio do paciente (opcional): ")
                cadastro.UltimoNomePaciente = input("Digite o último nome do paciente: ")

                cadastro.PrimeiroNomePai = input("Digite o primeiro nome do pai do paciente: ")
                cadastro.NomeMeioPai = input("Digite o nome do meio do pai do paciente (opcional): ")
                cadastro.UltimoNomePai = input("Digite o último nome do pai do paciente: ")

                cadastro.PrimeiroNomeMae = input("Digite o primeiro nome da mãe do paciente: ")
                cadastro.NomeMeioMae = input("Digite o nome do meio da mãe do paciente (opcional): ")
                cadastro.UltimoNomeMae = input("Digite o último nome da mãe do paciente: ")
                
                cadastro.Logradouro = input("Digite o logradouro: ")
                cadastro.Numero = input("Digite o número da sua rua: ")
                cadastro.Bairro = input("Digite o seu bairro: ")
                cadastro.Complemento = input("Digite o complemento: ")
                cadastro.Cidade = input("Digite o nome da sua cidade: ")
                cadastro.CEP = input("Digite seu CEP: ")
                cadastro.Estado = input("Digite o seu estado: ")
                
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
            CPF = input("Digite o cpf do paciente que deseja pesquisar: ")

            cadastro = self.repository.pesquisar_paciente_por_cpf(CPF)
            if cadastro:
                print("Dados do Paciente: ")
                print(f"\n CPF: {cadastro.CPF} | CIPTEA: {cadastro.CIPTEA} | Nome: {cadastro.PrimeiroNomePaciente} | Sobrenome: {cadastro.UltimoNomePaciente}")
                return
            
            print("Paciente não encontrado")
        except TypeError as e:
            print(f"Erro ao deletar o arquivo: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    def listar_todos_pacientes(self):
        return self.repository.listar_todos_pacientes()