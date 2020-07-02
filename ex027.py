# Faça um programa que leia um nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
# Ex: David Fernandes Bento
# Primeiro: David
# Ultimo: Bento
nome = input('Digite seu nome completo: ').strip()
print('Muito prazer {}'.format(nome))
separa = nome.split()
print('O seu primeiro nome é: {}.'.format(separa[0]))
print('O seu ultimo nome é: {}.'.format(separa[len(separa) - 1]))
