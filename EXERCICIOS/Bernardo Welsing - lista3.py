#===============================================================================
# COMPUTAÇÃO 1 - 2024.1 - LISTA DE EXERCÍCIOS 3
# Entregar até sexta (22-abril-2024)!
# Aluno: Bernardo Welsing Fernandes
# DRE:124031228

# ==============================================================================
# EXERCÍCIO 1  
# ===========
# Faça um programa que, dado o ano de nascimento de uma pessoa, calcule sua
# idade (aproximadamente). Crie expressões booleanas para determinar a faixa
# etária em que ela se encontra, sempre guardando o resultado na memória do
# computador. Não use if-elif-else ou input! A primeira expressão é dada como
# exemplo.

age = int(input("Qual sua idade"))
ano_nascimento = 2003

# a) Bebê: de 0 a 3 anos de idade.
eh_bebe = age >= 0 and age <= 3

# b) Criança: de 4 a 10 anos de idade.
eh_crianca = age >= 4 and age <= 10

# c) Adolescente: de 11 a 18 anos de idade.
eh_adolescente = age >= 11 and age <= 18

# d) Adulta: de 19 a 60 anos de idade.
eh_adulto = age>= 19 and age <= 60

# e) Idosa: acima de 61 anos.
eh_idoso = age >= 61



# ==============================================================================
# EXERCÍCIO 2
# ===========
# Crie expressões booleanas para saber se o aluno foi aprovado direto, em
# recuperação, ou reprovado por nota ou falta. Para saber como calcular as
# médias parcial e final, dê uma olhada no Plano de Curso. Lembrando que
# o aluno reprova se tiver acima de 7 faltas. Se quiser usar if-elif-else
# para imprimir o desfecho da história, use o resultado que guardou nas
# variáveis (Resumo 4 pág.5).

P1 = 10.0
P2 = 10.0
PF = 0.0
T1 = 10.0
T2 = 10.0
R  = 10.0
faltas = 7

MP = 60/100 * (P1 + P2 / 2) + 30/100 * (T1+T2/2) + 10/100 * R

if MP < 3 or faltas > 7:
    print("Você esta reprovado")
    
elif MP >= 3 and MP < 7:
    print("Você precisa fazer uma Prova Final para saber sua nota final")
    MF = MP + PF/2
    print ("Sua média final e", MF)
    
else:
    print("APROVADO!")

# ==============================================================================
# EXERCÍCIO 3
# ===========
# Fazendo o passo a passo, mostre porque as seguintes expressões imprimem
# True ou False no Terminal. Primeiro olhamos as comparações. Depois aplicamos
# as regrinhas dos operadores lógicos, dentro dos parênteses e depois na ordem
# de leitura. A primeira solução é dada como exemplo.

# a)
print(50/2 < 52 or ("Hello"=="Kitty" and "Kitty"!="kitty") and True)
# 50/2 < 52 == 25 < 52 => True
# "Hello"=="Kitty" => False
# "Kitty"!="kitty" => True
# Avaliamos primeiro dentro dos parênteses:
# True or (False and True) and True => True or False and True
# E depois na ordem de leitura:
# True or False and True => True and True => True

# b)
print(((10>5 or 3<7) and (True or False and not False)))

# 10 > 5 == true / 3 < 7 == true / or (true + false) = true, or (true + true) = true
#   AND = (true + false) = false / (true + true) = true

# True or False = true 
# NOT = ao contrário / not = true

# c)
print(not (8 / 2 == 4) and ("Python"!="python" or True))

# 8 / 2 = 4 (true), not (true) = false
#   AND = (true + false) = false / (true + true) = true
# Python != python (true) or True = True
#   AND = False + True = False

# d)
print(not ((12 - 6) == 6) and not (15 % 4 > 1))

# 12 - 6 = 6, 6 = 6 (true)
# not True (False)
# 15 % 4 = 3
# 3 > 1 = True
# not True (False)
# False + False = False


# e)
print(not (5 * 2 < 12) or (7 / 2 == 3.5) or ("OpenAI" == "openai"))

# 5 * 2 = 10 < 12 (True)
# not true = false
# 7 / 2 = true
# OpenAI = openai (False)
# not True or True or False
# False or True or False = True



# ==============================================================================
# EXERCÍCIO 4
# ===========
# Uma financiadora oferece empréstimos para pessoas físicas. O cálculo da taxa
# de juros anuais é feito de acordo com a seguinte fórmula:
#
#     taxa de juros = 1.8 + fator * 0.2
#
# onde o fator é o fator de risco do cliente, que é calculado de acordo com as
# tabelas 1 e 2:
#
#   Tabela 1: Fator de Risco (1ª parte)
#
#   | Idade            | Fator |
#   |------------------|-------|
#   | de 18 a 30 anos  |   3   |
#   | de 31 a 50 anos  |   6   |
#   | de 51 a 60 anos  |   9   |
#   | acima de 60 anos |   12  |
#
#   Tabela 2: Fator de Risco (2ª parte)
#
#   |  Patrimônio     |       Fator       |
#   |-----------------|-------------------|
#   | até R$ 50 mil   | fator = fator - 2 |
#   | até R$ 200 mil  | fator = fator - 1 |
#   | até R$ 1 milhão | fator = fator + 1 |
#   | acima disso     | fator = fator + 2 |
#
# Faça um programa que leia (input) a idade do cliente e o valor do empréstimo,
# e então calcule a taxa de juros. Imprima o valor com 2 casas decimais.
# Por exemplo:
#    para idade = 35, obtemos fator = 6
#    para o valor = 200000, corrigimos por fator = fator - 1 = 5
#    Assim, taxa de juros será 2.80% ao ano.


fR1 = int(input("Qual sua idade?"))
fR2 = float(input("Qual seu patrimônio"))
fator = 0

#=========================FATOR 1===========================

if fR1 >= 18 and fR1 <= 30:
    fator += 3
    print ("Seu fator idade é 3")

elif fR1 >= 31 and fR1 <= 50:
    fator += 6
    print ("Seu fator idade é 6")

elif fR1 >= 51 and fR1 <= 60:
    fator += 9
    print ("Seu fator idade é 9")

elif fR1 >= 60:
    fator += 12
    print ("Seu fator idade é 12")

else:
    print ("IDADE INSUFICIENTE PARA EMPRESTIMO")

#=========================FATOR 2===========================

if fR2 <= 50000:
    fator -= 2
    print ("Seu segundo fator é -2")

elif fR2 <= 50001 and fR2 <= 200000:
    fator -= 1
    print ("Seu segundo fator é -1")

elif fR2 <= 200001 and fR2 <= 1000000:
    fator += 1
    print ("Seu segundo fator é +1")

else:
    fator += 2
    print ("Seu segundo fator é +2")
    


taxa_de_juros = 1.8 + fator * 0.2

float(print("Taxa de JUROS ANUAIS de seu empréstimo é:", taxa_de_juros))


# ==============================================================================
# EXERCÍCIO 5
# ===========
# Crie um programa que use o seguinte código:  in "AEIOUaeiou"

msg = "AEIOUaeiou"

if "AEIOUaeiou" in msg:
    print ("Existe aeiou em minúsculo e em maíusculo na string")

else:
    print ("Não existem vogais na string")

# ==============================================================================
# EXERCÍCIO 6 (Não vale ponto)
# ============================
# Implemente o programa dado pelo fluxograma em anexo. Note que a resposta à
# pergunta "Você bebeu? " deve ser comparada com "sim", para poder se usada com
# o if.

# ==============================================================================
# EXERCÍCIO 7 (Não vale ponto)
# ============================
# String ainda tem mais funções! Aqui vai mais umas:
#   - str.isnumeric(s) retorna True se todos os caracteres são dígitos.
#   - str.isalpha(s) retorna True se todos os caracteres são do alfabeto.
#   - str.alnum(s) retorna True se os caracteres são alfa-numéricos.
# Isso exclui, é claro, outros símbolos, como espaço.
# Crie um jogo para adivinhar um número aleatório entre 1 e 10.
# Se o jogador digitar algo diferente de números, o programa deve responder:
# "Apenas números espertinho!"



