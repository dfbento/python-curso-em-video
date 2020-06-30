# faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto? R$'))
desc = preco * 5 / 100
novoPreco = preco - desc
print('O produto que custava R${:.2f}, na promoção com desconto de 5% custa R${:.2f}.'.format(preco, novoPreco))
