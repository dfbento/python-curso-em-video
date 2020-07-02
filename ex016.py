# crie um programa que leia um numero real qualquer pelo teclado e mostre na tela
# sua porção inteira.

from math import trunc
num = float(input('Digite um número qualquer: '))
print('O número digitado {} possui como parte inteira o número: {}.'.format(num, trunc(num)))
