# implementação prática da estrutura de dados Pilha (Stack)
# strutura organizacional de uma playlist 

class Faixa:
    def __init__(self, music: str) -> None:
        self.music = music
        self.next = None

class Playlist:
    def __init__(self) -> None:
        self.__current_song = None
    
    def append_to_playlist(self, song_name: str) -> None:
        # criar o objeto novo nó para alocar na pilha
        nova_faixa = Faixa(song_name)

        # esse nó deve apontar para o valor atual presente na pilha
        nova_faixa.next = self.__current_song # ou seja, ele vai apontar para o head

        # esse novo nó vai se tornar a nova cabeça da pilha
        self.__current_song = nova_faixa
    
    def excluir_faixa(self) -> None:
        # verificar se a pilha está vazia
        if self.__current_song is None:
            return None
        
        faixa_excluida = self.__current_song
        self.__current_song = self.__current_song.next

        return faixa_excluida.value
    
    def procurar_faixa(self, song_name: str):
        faixa_atual = self.__current_song
        index: int = 1

        if self.__current_song is None:
            print("Lista Vazia")
            return

        while faixa_atual and faixa_atual.music != song_name:
            faixa_atual = faixa_atual.next
            index += 1
        
        if faixa_atual is None:
            print("Faixa não encontrada")
            return
        
        print('+------------------------+')
        print(f'+ [{index}] {faixa_atual.music}\t +')
        print('+------------------------+')
    
    def latest_sond_added(self):
        self.procurar_faixa(self.__current_song.music)
    
    def visualizar_playlist(self) -> None:
        faixa_atual = self.__current_song
        index: int = 1

        print('Sua Playlist')

        if faixa_atual is None:
            print('Playlist vazia')
            return
        
        while faixa_atual:
            print('+------------------------+')
            print(f'+ [{index}] {faixa_atual.music}\t +')
            print('+------------------------+')

            faixa_atual = faixa_atual.next
            index += 1
        
        print()
    
if __name__ == '__main__':
    minha_playlist = Playlist()

    minha_playlist.append_to_playlist("It's just me, myself and I")
    minha_playlist.append_to_playlist("Papa Americano")
    minha_playlist.append_to_playlist("Stolen Dance")
    minha_playlist.append_to_playlist("Snowman")
    minha_playlist.append_to_playlist("Heart Afire")
    minha_playlist.append_to_playlist("Feel Good")

    minha_playlist.visualizar_playlist()

    #minha_playlist.procurar_faixa('Heart Afire')

    minha_playlist.latest_sond_added()