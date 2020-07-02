# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em quem posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.

frase = input('Digite uma frase qualquer: ').strip().lower()
print('A letra "a" aparece {} vezes.'.format(frase.count('a')))
print('A primeira aparição da letra "a" é na posição {}.'.format(frase.find('a') + 1))
print('A última aparição da letra "a" é na posição {}.'.format(frase.rfind('a') + 1))
