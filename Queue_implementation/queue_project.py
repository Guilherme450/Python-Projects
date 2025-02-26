import queue_structure as queue # estrutura para organizar os dados
from time import sleep
from random import randint
import os

class System:
    def __init__(self):
        self.quntidade_clientes = 0
        self.queue_structure = queue.Fila()
    
    def id_pedido_maker(self):
        id_pedido = randint(100, 999)

        return id_pedido

    def adicionar_pedido(self, nome: str, quantidade: int) -> None:

        self.queue_structure.inserir_dado(nome, self.id_pedido_maker(), quantidade)

        self.quntidade_clientes += 1

    def atender_pedido(self):
        sleep(10)
        self.queue_structure.remover_dado()
    
    def acompanhar_pedidos(self):

        while self.quntidade_clientes > 0:
            sleep(1.5)
            self.queue_structure.mostrar_fila()

            self.atender_pedido()

            self.quntidade_clientes -= 1

            os.system('cls')
        
        print("Nenhum Pedido na fila.")

main = System()

main.adicionar_pedido('hamburguer', 1)
main.adicionar_pedido('Pizza de calabreza', 2)
main.adicionar_pedido('sanduiche', 1)
main.adicionar_pedido('macarronada', 2)
main.adicionar_pedido('hamburguer', 3)
main.adicionar_pedido('Pastel de frango', 1)

main.acompanhar_pedidos()