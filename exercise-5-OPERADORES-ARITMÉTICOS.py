# OPERADORES ARITMÉTICOS
# adição = +
# subtração = -
# multiplicação = *
# divisão = /
# potência = **
# divisão inteira = //
# resto da divisão (módulo) = %

# ORDEM DE PROCEDÊNCIA
# 1º: ()
# 2º: **
# 3º: *, /, //, %
# 4º: +, -

# quebra de linha: \n | para seguir na mesma linha: end=''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {} \n O produto {} \n A divisão {}' .format(s, m ,d))
print('Divisão inteira {} \n A potência {}' .format(di, e))