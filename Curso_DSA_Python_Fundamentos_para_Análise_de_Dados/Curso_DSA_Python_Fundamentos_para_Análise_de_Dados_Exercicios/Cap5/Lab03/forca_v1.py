# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
import os

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
O   |
    |
    |
    |
=========''', '''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

>>>>>>>>>>Hangman<<<<<<<<<<

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

>>>>>>>>>>Hangman<<<<<<<<<<

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

>>>>>>>>>>Hangman<<<<<<<<<<

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

>>>>>>>>>>Hangman<<<<<<<<<<

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

#variável global
statusjogo = True
nivel = 0
# 1.5 1 2

# Classe
class Hangman:
	# Método Construtor
	global statusjogo
	def __init__(self, word):
		self.word = word
		self.len = len(word)
		self.letters = []
		self.listhits = []
		self.listerrors =[]
		self.conta_erros = 0

	# Método para adivinhar a letra
	def guess(self, letter):
		self.letters.append(letter.upper())
		if letter.upper() in list(self.word):
			self.listhits.append(letter.upper()) if letter.upper() not in self.listhits else None	
		else:
			self.listerrors.append(letter.upper()) if letter.upper() not in self.listerrors else None


	# Método para verificar se o jogo terminou
	def hangman_over(self):
		global statusjogo, nivel
		conta_acertos = 0
		self.conta_erros = 0
		for i in self.listhits:
			conta_acertos = conta_acertos + self.word.count(i)
			if self.len <= conta_acertos:
				statusjogo = False
				self.hangman_won(True)

		for i in self.listerrors:
			if i not in list(self.word):
				self.conta_erros += 1
			if int(6 * nivel) < self.conta_erros:
				statusjogo = False 
				self.hangman_won(False)

	# Método para verificar se o jogador venceu
	def hangman_won(self, status):
		if status:
			print ('\nParabéns! Você venceu!!')
		else:
			print ('\nGame over! Você perdeu.')
			print ('A palavra era: ' + self.word.upper())		
		print ('\nFoi bom jogar com você! Agora vá estudar!\n')

	# Método para não mostrar a letra no board
	def hide_word(self):
		print("Palavra: ", end = "")
		for i in range(len(self.word)):
			if self.word[i] in self.letters:
				print(self.word[i] +" ", end = "")
			else:
				print("_ ", end = "")
				
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		global statusjogo, board, nivel
		os.system('cls')
		print(board[int(self.conta_erros/nivel)])
		print('\nlista de acertos')
		print(self.listhits)
		print('lista de Erros')
		print(self.listerrors)


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank)-1)].strip().upper()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())
	os.system('cls')
	print('\n')
	print('>>>>>>>>>>Hangman<<<<<<<<<<')
	print('\nEscolha um Nível:')
	print('\n')
	print('1 - Fácil')
	print('2 - Nédio')
	print('3 - Difícil')
	while True:
		global nivel
		nivel = input()
		if nivel == '3':
			nivel = 1
			break
		elif nivel == '2':
			nivel = 1,5
			break
		elif nivel == '1':
			nivel = 2
			break
		else:
			print('escolha uma das opções!')
			continue

	os.system('cls')
	game.hide_word()
	print(board[0])
	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while statusjogo == True:
		while True:
			letra = input('Digite uma letra: ')
			if letra.isalpha() or len(letra)>1:
				break
			else:
				print('Jogada Inválida!!!')
				continue
		game.guess(letra)
		game.hide_word()
		
		# Verifica o status do jogo
		game.print_game_status()

		# Verifica o fim do jogo
		game.hangman_over()



# Executa o programa		
if __name__ == "__main__":
	main()
