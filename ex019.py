# um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

nome1 = input('Informe o primeiro nome: ')
nome2 = input('Informe o segundo nome: ')
nome3 = input('Informe o terceiro nome: ')
nome4 = input('Informe o quarto nome: ')

nomes = [nome1, nome2, nome3, nome4]

print('O nome sorteado foi: {}.'.format(choice(nomes)))
