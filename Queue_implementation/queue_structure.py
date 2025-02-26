# estrutura de dados Fila
# segue o conceito FIFO (First In First Out)
# Implementação por Listas Encadeadas

class Node:
    def __init__(self, nome: str, id: int, quantidade: int) -> None:
        self.nome = nome
        self.id = id
        self.quantidade = quantidade
        self.proximo = None

class Fila:
    def __init__(self):
        self.__cabeca = None
        self.__calda = None

    def inserir_dado(self, nome: str, id: int, quantidade: int) -> None:
        novo_no = Node(nome, id, quantidade)

        if self.__cabeca is None and self.__calda is None:
            self.__cabeca = novo_no
            self.__calda = novo_no

            return
        
        self.__calda.proximo = novo_no
        self.__calda = novo_no
    
    def remover_dado(self) -> None:
        if self.__cabeca is None and self.__calda is None:
            print('Não há dados armazenados na fila.')

            return
        
        deletado = self.__cabeca

        if self.__cabeca == self.__calda:
            self.__cabeca = None
            self.__calda = None
        else:
            self.__cabeca = self.__cabeca.proximo

            return deletado.nome, deletado.id, deletado.quantidade
    
    def mostrar_fila(self) -> None:
        no_atual = self.__cabeca

        while no_atual:
            print("+------------------------------+")
            print(f'+Nome do pedido: {no_atual.nome}')
            print(f'+Id do pedido: {no_atual.id}')
            print(f'+Quantidade: {no_atual.quantidade}')
            print("+------------------------------+")

            print(" ")

            no_atual = no_atual.proximo
