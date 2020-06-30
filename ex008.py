# escreva um valor em metros e o exiba convertido em centímetros e milímetros

dist = float(input('Digite uma distancia em metros: '))
km = dist / 1000
hm = dist / 100
dam = dist / 10
dm = dist * 10
cm = dist * 100
mm = dist * 1000

print('A medida de {} metros corresponde a: '.format(dist))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))
