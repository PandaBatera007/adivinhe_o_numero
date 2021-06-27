from random import randint
import sys
import time
from os import system

def efeito(frase):
	for i in list(frase):
		print(i, end='')

		sys.stdout.flush()
		time.sleep(0.05)
	print()
	return


def chute():

	efeito('Agora vamos jogar um game de advinhação')
	efeito('Irei sortear um numero de 0 a 10, e Você deve adivinhar qual é!')

	input('tecle <Enter> para continuar...')
	
	gerando_numero()


def gerando_numero():
	system('clear')

	numero = randint(0, 11)
	
	efeito('Estou gerando o Número... hummm... pronto!')
	print('Sua vez...')
	
	while True:
		chute_1 = None
		
		while not isinstance(chute_1, int):
			try:
				chute_1 = int(input('Digite o seu palpite: >>> '))
		
			except ValueError as err:
				print('''Você não digitou um número, assim a brincadeira não funciona
tente novamente''')
				print()

		if chute_1 == numero:
			print('PARABÉNS!')
			print('')
			efeito('é admirável sua intuição! ')
			print()
			break
		
		else: 
			print('Errou...')
			efeito('Tenta de novo!')
			print()
			
			if chute_1 > numero:
				print('Uma dica: O número é MENOR!!!')
				print()
				
			
			else:
				print('Uma dica: O número é MAIOR!')
				print()
	
	while True:			
		mais_uma_vez = input('Deseja jogar mais uma vez? ').lower()
		
		if mais_uma_vez == 'nao' or mais_uma_vez == 'n' or mais_uma_vez == 'não':
			print()
			efeito('Que Pena, gostei de jogar com você! até mais...')
			break
		
		elif mais_uma_vez == 'sim' or mais_uma_vez == 's':
			print()
			print('Certo!!!')
			gerando_numero()
			break
		
		else:
			print('opção inválida, tente novamente!')
chute()