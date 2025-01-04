from random import randint
import os
import platform

class Core:
    def __init__(self, name: str, cash: float) -> None:
        self.name = name
        self.cash = cash
        self.ponter = None

class CentralBaseInstructions:
    def __init__(self):
        self.current_data = None
    
    def add_new_user_info(self, user_name: str, user_cash: float) -> None:
        new_data = Core(user_name, user_cash)

        if self.current_data is None:
            self.current_data = new_data
            return

        new_data.ponter = self.current_data
        self.current_data = new_data
    
    def search_data(self, id: str) -> None:
        current_data = self.current_data
        current_id = 1

        if self.current_data is None:
            print('Sem dados de usuários.')
            return
        
        while current_data and current_data.name != id:
            current_data = current_data.ponter
            current_id += 1

        if current_data is None:
            print('usuário não encontrado.')
            return
        
        print(f'+------------USER ID {current_id}-------------+')
        print(f'+USER NAME: {current_data.name}\t\t   +')
        print(f'+AVAILABLE CASH: R${current_data.cash}\t\t   +')
        print(f'+----------------------------------+')

    
    def del_user_data(self):
        current_data = self.current_data
        previous_data = None

        if self.current_data is None:
            print('Erro! Nenhum registro para remover.')
            return
        
        while current_data and current_data.ponter:
            previous_data = current_data

            current_data = current_data.ponter
        
        previous_data.ponter = current_data.ponter

        print('DADO MAIS RECENTE EXCLUIDO')

    def show_information(self):
        current_id: int = 1
        current_data = self.current_data

        if self.current_data is None:
            print('Nenhum usuário cadastrado no sistema')
            return
        
        while current_data:
            print(f'+------------USER ID {current_id}-------------+')
            print(f'+USER NAME: {current_data.name}\t\t   +')
            print(f'+AVAILABLE CASH: R${current_data.cash}\t\t   +')
            print(f'+----------------------------------+')

            current_data = current_data.ponter
            current_id += 1

def clear_terminal(system_name: str):
    if system_name == 'Windows':
        os.system('cls')
        return
    
    os.system('clear')

def help_display():
    print('COMMAND TABLE')
    print(f'+----------------------------------+')
    print(f'+ Show User Data (1)\t\t   +')
    print(f'+ Remove Latest Data (2)\t   +')
    print(f'+ Search User Data (3)\t\t   +')
    print(f'+ Open Help Bar (4)\t\t   +')
    print(f'+ Quit Program (5)\t\t   +')
    print(f'+ Clear Terminal (6)\t\t   +')
    print(f'+ Add New Info (7)\t\t   +')
    print(f'+----------------------------------+')

if __name__ == '__main__':
    main_system = CentralBaseInstructions()
    users_test: tuple = ('guilherme', 'joão', 'carlos', 'mesquita')
    user_cash_test: list = [randint(2000, 5000) for i in range(len(users_test))]
    system_type = platform.system()
    current_user_cash: int = 0

    for user in users_test:
            main_system.add_new_user_info(user, user_cash_test[current_user_cash])

            current_user_cash += 1
    
    help_display()

    while True:

        try:
            admin_command: int = int(input('>> '))

            match admin_command:
                case 1:
                    clear_terminal(system_type)
                    main_system.show_information()
                case 2:
                    clear_terminal(system_type)
                    main_system.del_user_data()
                case 3:
                    clear_terminal(system_type)
                    user_id: str = input('Digite o Nome do usuário: ')
                    main_system.search_data(user_id)
                case 4:
                    help_display()
                case 5:
                    print('Programa encerrado')
                    break
                case 6:
                    clear_terminal(system_type)
                case 7:
                    user_name: str = input('Digite o nome: ')
                    user_cash: float = float(input('Digite o saldo: '))

                    main_system.add_new_user_info(user_name, user_cash)
                case _:
                    print('Comando inválido')
                    continue
        except ValueError:
            print('Comando não reconhecido. Tente Novamente')
            continue
