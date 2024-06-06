#===============================================================================
# COMPUTAÇÃO 1 - 2024.1 - LISTA DE EXERCÍCIOS 6
# Entregar até domingo (26-maio-2024)!
# Aluno: BERNARDO WELSING FERNANDES
# DRE: 124031228
#===============================================================================

# INSTRUÇÕES: Tenha muito cuidado agora! Gaste o tempo adequado para estudar
#             funções e assim, não ficar perdido no resto do curso! Verifique
#             duas vezes se é necessário usar return ou print, e sempre inclua
#             DOC-STRINGS! 



def barra(tamanho, caractere="*", exer=0):
    """Imprime uma barra de caracteres e o número do exercicio.
    (int, str, int) -> None
    """
    print(caractere * tamanho)
    if exer != 0: print(" "*tamanho,f">> EXERCÍCIO {exer} <<\n")


# ==============================================================================
# EXERCÍCIO 1  
# ===========
# Crie uma função chamada div_resto que receba dois números inteiros e
# retorne uma tupla com o quociente e o resto da divisão de um pelo outro. 
# Inclua Casos de Teste.

barra(20,"-=",1)
def div_resto(num1, num2):
   """Descobre valores do quociente e resto de uma razão.
   (int, int) -> tuple(quociente, resto)"""
   valores = (num1/num2, num1%num2)
   return valores

# CASOS DE TESTE 
print(div_resto(6, 2)) # 3 e 0
print(div_resto(5, 2)) # 2.5 e 1
print(div_resto(15, 3)) # 5 e 0



# ==============================================================================
# EXERCÍCIO 2
# ===========
# Em várias ocasiões precisamos escrever um algoritmo para saber se um 
# caractere é uma vogal ou não. Que tal colocar esse algoritmo dentro de uma 
# função eh_vogal? Os Casos de Teste com os valores esperado estão abaixo.

barra(20, "-=",2)
def eh_vogal(letter):
   """Verifica se um caractere é uma vogal.
   (str) -> bool"""
   
   letter = letter.lower().strip()
   if letter in "aeiouáéíóúâêîôûàèìòùã": return True 
   else: return False

# CASOS DE TESTE
print( eh_vogal(' c') ) # False
print( eh_vogal('!') ) # False
print( eh_vogal(' É') ) # True
print( eh_vogal('o') ) # True
print( eh_vogal('à') ) # True
print( eh_vogal(' K    ') ) # False
print( eh_vogal('9') ) # False


# ==============================================================================
# EXERCÍCIO 3
# ===========
# Escreva uma função chamada eh_primo que receba como argumento um  número
# inteiro e retorne True caso o número seja primo, ou False caso contrário
# (o tipo retornado é bool). Seu código deve conter Casos de Teste com print(),
# para mostrar o resultado no Terminal, e o resultado esperado em comentários.
#
# Agoritmo: Determinar se um número é primo.
# ---------------------------------------------------------
# 1. Seja num o argumento da função
# 2. Se num <= 1, retorna False
# 3. Inicializar j = 2
# 4. Enquanto j for menor que num:
# 4a.   Se o resto da divisão de num por j for 0:             
# 4ai.     Retorna False
# 4b.   Incrementa j
# 5. Retorna True
# ---------------------------------------------------------

barra(20,"-=",3)
def eh_primo(num):
   """Verifica se o algarismo é um número PRIMO.
   (int) -> str"""
   for i in range(num-1, 1, -1):
      if num%i == 0:
         return "NÃO É PRIMO"              # Eu achei o laço FOR muito mais útil nesse caso, espero que não me puna por isso.
   return "É PRIMO"

        
print(eh_primo(1)) # É PRIMO
print(eh_primo(5)) # é primo
print(eh_primo(9)) # não é primo
print(eh_primo(17)) # é primo
print(eh_primo(11)) # é primo
print(eh_primo(16)) # não é primo



# ==============================================================================
# EXERCÍCIO 4
# ===========
# a) Pontos ou vetores podem ser representados por uma tupla (x, y). 
#    Escreva uma função, chamada soma_vet, que recebe duas tuplas 
#    chamadas ponto1 e ponto2 e retorna outra tupla com a soma de 
#    coordenadas. Isto é, (x1, y1) + (x2, y2) => (x1+x2, y1+y2).
#
# b) Escreva a função prod_esc que recebe dois vetores e retorna o produto 
#    escalar delas (um float). Isto é, (x1, y1) ● (x2, y2) => x1*x2 + y1*y2.
#
# c) Continuando com operações vetoriais, escreva a função det, que 
#    calcula o determinante de dois vetores. Isto é, 
#    (x1, y1) × (x2, y2) => x1*y2 - x2*y1.
barra(20,"-=", 4)


def soma_vet(ponto1, ponto2):
   """Realiza a soma de dois vetores
   (tuple, tuple) -> tuple"""
   newTuple = (ponto1[0]+ponto2[0], ponto2[1]+ponto1[1])
   return newTuple


def prod_esc(ponto1, ponto2):
   """Realiza a multiplicação escalar de dois vetores
   (tuple, tuple) -> float"""
   newTuple = ((ponto1[0]*ponto2[0]) + (ponto2[1]*ponto1[1]))
   return newTuple


def det(ponto1, ponto2):
   """Calcula o determinantes de dois vetores
   (tuple, tuple) -> float"""
   newTuple = ((ponto1[0]*ponto2[1]) - (ponto1[1]*ponto2[0]))
   return newTuple


# CASOS DE TESTE
v1 = (1.0, -5.0)
v2 = (3.0, 6.0)
print(soma_vet(v1, v2))  # Esperado: (4.0, 1.0)
print( prod_esc(v1, v2) )  # Esperado: -27.0
print( det(v1, v2) )       # Esperado: 21.0


# ==============================================================================
# EXERCÍCIO 5
# ===========
# Escreva uma função que mostre na tela as seguintes informações sobre um 
# triângulo retângulo: cateto adjacente, cateto oposto, hipotenusa, perímetro 
# e área. Por exemplo, ao chamar a função com argumentos 3 e 4, obtemos:
#    cateto adjacente: 3
#    cateto oposto: 4
#    hipotenusa: 5.00
#    perímetro: 12.00
#    área: 6.00
#
# Um número com duas decimais pode ser impresso utilizando o formatador :.2f
# Para calcular a hipotenusa dentro da função, utilize a função já definida
# nesta aula. Quero dizer que, uma das linhas da sua função deve ser:
#    h = hipotenusa(a, b).
#
# Inclua o caso de teste descrito acima.
#

barra(20,"-=", 5)

import math

def hipotenusa(a, b):
   """Retorna a hipotenusa de um triângulo retângulo.
      (float, float) -> float
   """
   h = math.sqrt(a**2 + b**2)
   return h

def perimetro(a, b, c):
   """Retorna o perímetro de um triângulo retângulo.
      (float, float, float) -> float
   """
   return a + b + c

def areaTriangle(a, b):
   """Retorna a área de um triângulo retângulo.
      (float, float) -> float
   """
   return (a*b)/2

def show_Triangle_Data(cateto1, cateto2):
   print(f"""#    cateto adjacente: {cateto1}
#    cateto oposto: {cateto2}
#    hipotenusa: {hipotenusa(cateto1, cateto2)}
#    perímetro: {perimetro(cateto1, cateto2, hipotenusa(cateto1, cateto2))}
#    área: {areaTriangle(cateto1, cateto2)}""")


# CASOS DE TESTE 
show_Triangle_Data(3, 4)


# RESULTADO ESPERADO:
#    cateto adjacente: 3
#    cateto oposto: 4
#    hipotenusa: 5.00
#    perímetro: 12.00
#    área: 6.00

barra(20, "-=")