#===============================================================================
# COMPUTAÇÃO 1 - 2024.1 - LISTA DE EXERCÍCIOS 2
# Entregar até sexta (12-abril-2024)!
# Aluno: Bernardo Welsing Fernandes
# DRE: 124031228
#===============================================================================

# ==============================================================================
# EXERCÍCIO 1  Calcule as raízes da equação quadrática ax² + bx + c = 0, onde
# ===========  a, b e c são os coeficientes. Como sempre, utilize variáveis, e
#              não valores fixos. Para os coeficientes listados abaixo, as
#              raízes são -3 e 5.
#
#              Não é obrigatório, mas em exercícios desse tipo costuma-se usar
#              a "função externa" sqrt() para calcular raíz quadrada de um
#              número. Para usá-la, precisa da instrução abaixo com "import".

from math import sqrt
a = 2
b = -4
c = -30


 ## Condições apenas para formatação do texto
if b < 0:
    op1 = "-"
else:
    op1 = "-"

if c < 0:
    op2 = "-"
else:
    op1 = "-"

print("="*40)


print("--- bhaskara calculator --- ")

print("""\nEQUAÇÃO A SER CALCULADA: {}x² {} {}x {} {} = 0
      a = {}
      b = {}
      c = {}""".format(a, op1, abs(b), op2, abs(c), a, b, c))

### Variaveis para delta
bdelta = b**2 
cdelta = 4*a*c
delta = bdelta-cdelta

print("""   CALCULANDO DELTA
Δ = {}² - 4.{}.{}   
Δ = {} - {}
Δ = {}""".format(b, a, c, bdelta, abs(cdelta), delta))    

### variaveis bhaskara 
x1 = ((-1*b) + sqrt(delta)) / (2*a)  ### Calcula delta com operação positiva
x2 = ((-1*b) - sqrt(delta)) / (2*a)  ### calcula delta com operação negativa 



print("""   CALCULANDO BHASKARA 
x = {} ± √{} / 2.{}

x1 = {}
x2 = {}
     """.format(-1*a, delta, a, x1, x2 ))

print("="*40)

# ==============================================================================
# EXERCÍCIO 2  Usando f-strings, pesquise como alinhar textos dentro de um
# ===========  espaço fixo (que vou chamar de coluna). Mostre que entendeu
#              alinhando uma string msg nos 3 cantos de uma coluna de 16
#              caracteres. Coloque caracteres para mostrar os limites da 
#              coluna.
msg = "Stargazer"


# Para isso podemos usar as funções ljust(), center() e rjust()
# ou como fiz abaixo, o python permite dentro da f-string utilizar o ":" para formatações
# nesse caso, "<" corresponde ao ljust(), "^" corresnponde ao center() e ">" claramente, ao rjust()
print("="*40)
print("EXERCICIO 2")
print("""|{:<20}|
|{:^20}|
|{:>20}|""".format(msg, msg, msg))
print("="*40)
# A saída (texto) esperada no Terminal é:
# |Stargazer       |
# |   Stargazer    |
# |       Stargazer|


# ==============================================================================
# EXERCÍCIO 3  As funções de strings são muito úteis. Faça um resuminho das 
# ===========  funções aprendidas na última aula, com uma breve explicação do
#              que fazem, quais são seus argumentos e seus resultados
#              (o que a função retorna). Adicione exemplos "minimalistas"
#              para cada função.

#    FUNÇÃO:  str.find
# O QUE FAZ?  Procura uma string dentro de outra
#     ARG.1:  String onde procurar
#     ARG.2:  String a ser procurada
#   RETORNA:  Índice do primeiro caractere da string procurada. Retorna -1 se
#             a string procurada não foi encontrada.

#print( str.find("Aqui se procura", "acha") )
#print( str.find("Aqui se acha", "acha") )


texto = "DEIXEI O trabalho PRA CIMA DA hora E FIZ Correndo o trabalho :("

#    FUNÇÃO:  str.lower
# O QUE FAZ?  Transforma a string toda em letras minusculas
#     ARG.1:  String para ser transformada
#   RETORNA:  String em letras minusculas
print("="*40)
print("TEXTO UTILIZANDO str.lower")
print(texto.lower())



#    FUNÇÃO:  str.upper
# O QUE FAZ? Transforma toda a string em letras maiuscula 
#     ARG.1:  String a ser transformada
#     ARG.2:  
#   RETORNA:  String em letras maiusculas
print("="*40)
print("TEXTO UTILIZANDO str.upper")
print(texto.upper())

#    FUNÇÃO:  str.count
# O QUE FAZ?   conta a quantidade de um ou um conjunto de caracteres em uma string 
#     ARG.1:  String a ser contada 
#     arg.2: qual palavra na string vc quer contar
#   RETORNA:   Quantidade de strings
print("="*40)
print("Quantidade de palavras em TEXTO ")
print(texto.count("trabalho"))

#    FUNÇÃO:  str.replace
# O QUE FAZ?  altera algum valor, escolhido, da string
#     ARG.1:  valor a ser alterado
#     ARG.2:  por qual valor deve ser alterado 
#   RETORNA: A string com o texto alterado 
print("="*40)
print(texto.replace("trabalho", "dever").lower())



# ==============================================================================
# EXERCÍCIO 4  Crie um exercício (sim, você!) em que seja necessário usar o 
# ===========  passo do fatiamento para alguma coisa. Coloque também a solução.


## EXERCICIO: Crie um programa que leia qualquer nome e mostre apenas o last name dele

nome = input("Insira um nome: ")
nome = nome.split()

print("Olá, Sr(a). {} ".format(nome[-1]))
