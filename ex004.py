# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('####Detalhando algo digitado!####')
entrada = input('Digite algo: ')
print('O tipo primitivo de {} é: {}'.format(entrada, type(entrada)))
print('Só tem espaços? {}'.format(entrada.isspace()))
print('É um número? {}'.format(entrada.isnumeric()))
print('É alfabético? {}'.format(entrada.isalpha()))
print('É alfanúmerico? {}'.format(entrada.isalnum()))
print('Está em maiúsculo? {}'.format(entrada.isupper()))
print('Está em minúsculo? {}'.format(entrada.islower()))
print('Está capitalizado? {}'.format(entrada.istitle()))