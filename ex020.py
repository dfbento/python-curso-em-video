# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
nome1 = input('Informe o primeiro nome: ')
nome2 = input('Informe o segundo nome: ')
nome3 = input('Informe o terceiro nome: ')
nome4 = input('Informe o quarto nome: ')

nomes = [nome1, nome2, nome3, nome4]
shuffle(nomes)

print('A ordem de apresentação sorteada será: {}.'.format(nomes))
