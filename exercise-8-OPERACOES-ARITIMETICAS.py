a = int(input('digite um número:'))
a1 = int(input('digite mais um:'))
a2 = a + a1
print('a soma de {} e {} vale: {}.' .format(a, a1, a2))

b = int(input('me dê mais um número:'))
b1 = int(input('agora me dê outro:'))
b2 = b - b1
print('a subtração de {} e {} é: {}.' .format(b, b1, b2))

c = float(input('agora vamos multiplicar, me dê um número, ele pode ser "quebrado":'))
c1 = float(input('me dê mais um:'))
c2 = c * c1
print('a multiplicação entre {} e {} vale: {}.' .format(c, c1, c2)) 

d = int(input('me diga um número:'))
d1 = int(input('me diga outro:'))
d2 = d ** d1
print('a potenciação entre {} e {} vale: {}.' .format(d, d1, d2))

z = a2 + b2 + c2 * d2
print('a soma e multiplicação de todos os resultados vale: {}' .format(z))