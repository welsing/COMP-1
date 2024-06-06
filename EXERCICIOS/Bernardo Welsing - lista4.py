#===============================================================================
# COMPUTAÇÃO 1 - 2024.1 - LISTA DE EXERCÍCIOS 4
# Entregar até sexta (26-abril-2024)!
# Aluno: Bernardo Welsing Fernandes
# DRE: 124031228
#
# ==============================================================================
# EXERCÍCIO 1  
# ===========
# O matemático Fibonacci criou uma sequência para descrever o crescimento de uma
# população de abelhas (fabricação de velas com cera de abelhas era muito comum
# em sua cidade). A população em cada mês era a soma dos dois meses anteriores.
# Os primeiros números da sequência são esses:
fibo = [1, 1, 2, 3, 5, 8, 13, 21, 34]
# Na lista fibo, adicione a previsão para os próximos quatro meses utilizando
# somente indexação com índices negativos. Imprima a população final e a
# quantidade de meses decorridos. Para os apressados: não é para usar
# estruturas de repetição, os exercícios aqui servem para verificar suas bases
# em programação.

print("PESQUISA CIENTIFICA PARA PREVISÃO DA POPULAÇÃO DE ABELHAS NO CAMPO ")
print("Atualmente temos dados dos ultimos {} meses,\n com as respectivas populações {}".format(len(fibo), fibo))

soma = fibo[-2] + fibo[-1]
fibo.append(soma)
soma = fibo[-2] + fibo[-1]
fibo.append(soma)
soma = fibo[-2] + fibo[-1]
fibo.append(soma)
soma = fibo[-2] + fibo[-1]
fibo.append(soma)

print("PASSARAM 4 MESES ")

print("MESES DECORRIDOS: {}".format(len(fibo)))
print("POPULAÇÃO TOTAL ATUAL DE ABELHAS: {}".format(fibo[-1]))

print(fibo)


# ==============================================================================
# EXERCÍCIO 2
# ===========
# Implemente um programa para o seguinte algoritmo:
#
# 1.  Perguntar a data de nascimento da pessoa. Por exemplo: 1/1/1999.
# 2.  Usar str.split para separar a resposta do input pelo caractere /.
# 3.  SE a lista gerada tiver comprimento diferente de 3:
# 3a.    Imprima na tela "Formato incorreto!"
# 4.  CASO CONTRÁRIO:
# 4a.    Use "desempacotamento" da lista para obter o dia, mes e ano.
# 4b.    Converta o mes para inteiro (o resultado de split é uma lista
#           de strings).
# 4c.    Use mes-1 para obter o nome do mês através da lista fornecida abaixo.
#           O nome do mês será colocado de volta na lista, no lugar do número.
# 4d.    Use str.join para juntar novamente a lista numa string,
#           com separador " de ".
# 4e.    Imprima o resultado. Para o exemplo acima, seria 1 de janeiro de 1999.
#
# Em caso de dúvida, você pode testar os comandos no Shell do Python.
# Teste por exemplo >>> str.split("1/1/1999", "/")


meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

data = input("DATA DE NASCIMENTO [00/00/0000]: ").split("/")
#data = str.split(data, "/")
mes = meses[int(data[1])-1]
data[1]= mes
if len(data) != 3:
    print("FORMATO INCORRETO!")
else:
    data = str.join(" de ", data)
    print(data)
    

# ==============================================================================
# EXERCÍCIO 3
# ===========
# As listas abaixo contém o nome de alguns corredores do kart e o tempo de
# volta de cada um, na mesma ordem. Por exemplo, o tempo de Mario é 36.2 seg,
# ambos no índice 1 de cada lista. Escreva um código para mostrar os corredores
# que fizeram o melhor e pior tempos de volta, assim como os respectivos tempos,
# usando min(), max() e list.index().


corredores = ['Bowser', 'Mario', 'Luigi', 'Peach', 'Yoshi', 'Toad']
tempos = [42.7, 36.2, 57.2, 29.5, 35.4, 29.9]

melhor = min(tempos)
pior = max(tempos)
print("O corredor {} fez a melhor volta em {} seg.".format(corredores[list.index(tempos, melhor)], melhor))
print("O corredor {} fez a melhor volta em {} seg.".format(corredores[list.index(tempos, pior)], pior))


# ==============================================================================
# EXERCÍCIO 4
# ===========
# Crie uma lista pequena, depois faça "uma cópia" com atribuição simples, i.e.
# lista2 = lista1. Modifique um dos itens da cópia e imprima as duas listas.
# Nossa intenção era alterar apenas a cópia.
# Relate o ocorrido. Repita o
# procedimento pegando uma fatia da lista inteira (do início ao fim).
# Funcionou?
#
# O que aconteceu foi um erro de semântica (nos expressamos de forma errada).
# O código não tinha nenhum erro de sintaxe, portanto o Python fez exatamente
# aquilo que pedimos: criar uma nova "referência" para a mesma lista. Mas
# porquê o Python não copiou a lista com lista2 = lista1 ? Por que gasta-se
# tempo de processamento e memória para fazer cópias. É mais comum criar
# referências para que outras partes do programa possam calcular coisas
# como média e desvio padrão.

lista1 = ["string", 0.5, 2]
#lista2 = lista1
## Primeiro não funcionou pois as listas estão assiciadas.

lista2 = lista1[:]
lista2[1] = "agora é string tb"

print(lista1)
print(lista2)




