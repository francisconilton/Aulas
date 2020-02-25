#Reading and writing files.

#Problem

#GIVEN: A file containing at most 1000 lines.

#RETURN: A file containing all the even-numbered lines from the original file.
#        Assume 1-based numbering of line.

### Resolvendo: Premeiramente, eh preciso criar um arquivo de texto. Faça isso
# utilizando o comando touch no terminal dentro de uma pasta de sua escolha.

# Segundo. No PyCharm, a primeira coisa a fazer eh declarar uma variavel
# chamada caminho = iserir o caminho.

caminho = "/home/gntech/Documents/Familia/Nilton/ini5.txt"

arquivo = open(caminho, "r")

counter = 1

for linha in arquivo:
    if counter % 2 == 0:
        print(linha)
    counter = counter + 1

arquivo.close()