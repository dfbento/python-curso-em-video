# faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número inteiro qualquer: '))
ant = n - 1
suc = n + 1
print('O número digitado {} possui como antecessor o {} e como sucessor o {}.'.format(n, ant, suc))
