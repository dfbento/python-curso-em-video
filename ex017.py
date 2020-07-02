# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triagulo retangulo, calcule e mostre o comprimento da hipotenusa.

catOp = float(input('Digite o comprimento do cateto oposto: '))
catAdj = float(input('Digite o comprimento do cateto adjacente: '))
hipo = ((catOp ** 2) + (catAdj ** 2)) ** (1/2)

print('O triagulo retangulo com cateto oposto {} e cateto adjacente {} possui uma hipotenusa de {:.2f}.'.format(catOp, catAdj, hipo))
