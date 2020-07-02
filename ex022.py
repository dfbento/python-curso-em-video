# crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome coom todas as letras minusculas
# Quantas letras ao possui (sem considerar os espaços)
# quantas letras tem o primeiro nome

nome = input('Digite seu nome: ').strip()
print('Analisando seu nome...')
print('Seu nome em letras maiusculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('Seu nome possui ao todo {} letras.'.format(len(nome.replace(' ', ''))))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
