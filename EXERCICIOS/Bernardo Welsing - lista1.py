#===============================================================================
# COMPUTAÇÃO 1 - 2024.1 - LISTA DE EXERCÍCIOS 1
# Entregar até quarta (3-abril-2024)!
# Aluno: Bernardo Welsing Fernandes
# DRE: 
#===============================================================================


# EXERCÍCIO 1  Desenvolva um código que, dado o valor da conta do restaurante,
# ===========  calcule a gorgeta do garçom, considerando que a gorgeta deve ser
#              15% do valor da conta.


valor_Conta = float(input("Qual total do pedido? : "))
gorgeta = ((valor_Conta*15)/100)

print("###################################")
print("       TOTAL DO PEDIDO    ")
print("                    R$:{:.2f}       ".format(valor_Conta))
print("  serviços prestado R$:{:.2f}       ".format(gorgeta))
print("              total R$:{:.2f}       ".format(valor_Conta+gorgeta))







# EXERCÍCIO 2  Crie um algoritmo que leia os raios interno e externo de uma
# ===========  coroa circular. Calcule e mostre a área da coroa circular.
#              Use o pi definido abaixo (a variável, não o número).


pi = 3.141


print("#"*30)
print("    COROA CALCULATOR 3000              (centimetros) ")
print("#"*30)

print("Qual o raio EXTERNO da coroa?")
extCoroa = float(input("                     Digite: "))
print("Qual o raio INTERNO da coroa?")
intCoroa = float(input("                     Digite: "))

area = pi*(extCoroa**2-intCoroa**2)
print(">"*30)
print("RAIO EXT.: {}cm".format(extCoroa))
print("RAIO INT.: {}cm".format(intCoroa))
print("ARÉA DA COROA: {}cm²".format(round(area, 2)))
print("<"*30)





# EXERCÍCIO 3  Escreva um programa que pergunte a quantidade de quilômetros
# ===========  percorridos de um carro alugado e a quantidade de dias pelos
#              quais ele foi alugado. Calcule o preço a pagar sabendo que a
#              diária custa R$ 60,00 com adicional de R$ 0,15 por km rodado.


km_Percorridos = float(input("KM PERCORRIDS: "))
dias_Alugados = int(input("DIAS ALUGADOS: "))

valor_Km = km_Percorridos*0.15
valor_Dias = dias_Alugados*60
tot = valor_Km+valor_Dias

print("CALCULANDO... ")
print("Kilometragem Total: {}km | {:.2f}$".format(km_Percorridos, valor_Km))
print("qtd. Dias:            {} | {:.2f}$".format(dias_Alugados, valor_Dias))
print("TOTAL A PAGAR:      {:.2f}$       ".format(tot))




# EXERCÍCIO 4  Pesquise sobre as funções abs(), min(), max() e round().
# ===========  Escreva algumas linhas de código para exemplificar cada uma.

#  round()
# Está função tem como objetivo arredondar os números para quantidade de casas decimais, e seus parametros são 
# round(<variavel>, <Quantidade de casas decimais>)

variavel = 3.14159

print("EXEMPLO round()")
print("variavel: {} \n Utilizando round(): {}".format(variavel, round(variavel, 2)))


# min()
#  Está função busca o menor valor de um conjunto


print("EXEMPLO min()")
alunos_Notas = [5.4, 3.5, 8.0, 9.0, 9.5]
print("Notas de alunos: {}".format(alunos_Notas))
print("Menor Nota: {}".format(min(alunos_Notas)))

# max()
# Ao contrario da função min(), certamente, está função mostra o maior valor de um conjunto
print("EXEMPLO min()")
alunos_Notas = [5.4, 3.5, 8.0, 9.0, 9.5]
print("Notas de alunos: {}".format(alunos_Notas))
print("Maior Nota: {}".format(max(alunos_Notas)))

# abs()
# Serve para calcular o valor absoluto de um número

n_exemplo = -33

print("Número: {} \n Utilizando abs(): {}".format(n_exemplo, abs(n_exemplo)))






