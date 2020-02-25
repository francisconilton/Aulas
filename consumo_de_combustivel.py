from random import randint
# gera numeros inteiros aleatorios entre, e inclusive, 10 e 25
# para representar a quantidade de combustivel no tanque do carro

comb = randint(10, 25)

# gera numeros inteiros aleatorios entre, e inclusive, 200 e 400 para representar a autonomia do veiculo, ou seja,
# quantos km ele percorre com um tanque cheio.

km = randint(200, 400)

# calcula e mostra o MPG do carro assumindo que o fabricante do carro superestimou os valores.
print("O carro pode viajar " + str(km // comb) + " km por litro.")

# mostra o numero de quilometros que o carro pode viajar com um tanque cheio.
print("O tanque do carro pode conter " + str(comb) + " litros.")

