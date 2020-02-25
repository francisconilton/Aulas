# Aula 9 fala sobre list comprehension.

# List comprehension eh util quando se pretende destacar um item dentro de uma lista.

# frutas = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']
#
# lc = [x[1] for x in frutas if int(x[1])<4]
#
# print(lc)
#
# len(frutas)

### Lendo arquivos utilizando list comprehension
#Neste exemplo, o comando with open busca a informacao no arquivo conforme o
#endereco informado, e imprime no Python console.

# with open("/home/gntech/Documents/Familia/Nilton/ini5.txt", "r") as f:
#     dados = [x.rstrip('\n') for x in f.readlines()]
#     print(dados)


### Dicionario comprehension
#
# lista = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
#
# dic = {x:x}
#
# x for x in lista
#     print(lista)

################## para aula 11 ########################
# a = ["a", "b", "c"]
# b = ["e", "f", "g"]
# a.extend(b)
# print(a)
################## para aula 11 ########################
#append e extend - quando usar um e outro.

#funcao com dois argumentos:
#
# def funcao(a, b=10):
#     return a + b
#
# print(funcao(100,2))
#
# def country(pais = "Brazil"):
#   print("I am from " + pais)
# country()

