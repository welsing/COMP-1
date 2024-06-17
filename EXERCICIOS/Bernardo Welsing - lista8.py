#===============================================================================
# COMPUTAÇÃO 1 - 2024.1 - LISTA DE EXERCÍCIOS 8
# Entregar até segunda (17-junho-2024)!
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
    print("\n")
    print(caractere * tamanho)
    #if exer != 0: print(" "*tamanho,f">> EXERCÍCIO {exer} <<\n")
    if exer != 0: print(f"{f">> EXERCÍCIO {exer} <<":>{tamanho}}")
from time import sleep


# ==============================================================================
# EXERCÍCIO 3
# ===========
barra(40,"=", 3)
sleep(3)
# Contar palavras é um recurso importante para análise semântica de textos, 
# sendo usada em conjunto com técnicas de Inteligência Artificial. Construa 
# uma função que receba uma string e retorne um dicionário com o número de 
# ocorrências de cada palavra. Por exemplo:
#
#    conta_palavras("Ai se eu te pego, ai ai se eu te pego")
#    # retorna: {'ai': 3, 'se': 2, 'eu': 2, 'te': 2, 'pego': 2}
#
# Repare que não importa se a palavra está em maiúscula ou minúscula.
# Dica: Comece com um dicionário vazio e faça um laço iterando sobre
# cada palavra (usando str.split()).


texto = "Ai se eu te pego, ai ai se eu te pego!"

def conta_palavras(txt):
   """Conta as palavras de uma string \n (str) -> dict"""

   del_carct = ",!.;~]´[]{}?"
   contagem = {}
   txt = txt.lower()
   txt = txt.split()
   for word in txt:
      for char in del_carct:
        word = word.replace(char, "")
      if word in contagem:
         contagem[f'{word}'] += 1
      else:
         contagem[f'{word}'] = 1
         
   return contagem


print(f"\n[Cesar] - ALEXA! Conte quantas vezes as palavras se repetem na frase '{texto}'\n")
sleep(2)
print("[Alexa] - É claro, REALIZANDO CONTAGEM DE PALAVRAS", end="")
for i in range(4):
   print(".", end='')
   sleep(1)
print()
for word, x in conta_palavras(texto).items():
   print(f"[Alexa] - A palavra '{word}' aparece {x} vezes")
   sleep(1)

print(f"\n[Cesar] - Obrigado, agora posso dormir em paz...")


## Essa brincadeira foi nas melhores das intenções...    ;)   


# ==============================================================================
# EXERCÍCIO 1  
# ===========
barra(40, "=", 1)
# O dicionário a seguir guarda as vendas de cada vendedor de uma loja de sapatos
# nos três primeiros meses do ano:
vendas = {
   "Amilton": [3550.00, 2780.00, 4100.00],
   "Jefferson": [3760.00, 3300.00, 3810.00],
   "Eliane": [3460.00, 2580.00, 4050.00],
   "Gerusa": [4540.00, 1780.00, 4590.00]
}
# Escreva uma função que receba um dicionário desse tipo e mostre a média de
# vendas de cada vendedor (não esqueça do nome também). Para iterar no
# dicionário, utilize a função dict.items().

def media_vendas(dicio):
    """Cria uma tabela de média de valores de chaves de um certo dicionario.\n (dict) -> None"""

    print(f"{"VENDEDOR":<15}  {"MÉDIA DE VENDAS":<15} {"PERIODO":>10}")
    for nome, venda in dicio.items():
        media = sum(venda) / len(venda)
        print(f"{nome:<15}  R${media:<15.2f} {f"{len(venda)} meses":>8}")


media_vendas(vendas)

# ==============================================================================
# EXERCÍCIO 2
# ===========
barra(40, "=", 2)
# Escreva uma função que converta números inteiros entre 0 e 999 para algarismos
# romanos, usando os três dicionários abaixo. Os nomes dos dicionários estão em
# maiúsculas para indicar que não devemos alterá-los (são constantes).
UNIDADES = {
   0:'',  1:'I',  2:'II',  3:'III',  4:'IV',
   5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
DEZENAS = {
   0:'',  1:'X',  2:'XX',  3:'XXX',  4:'XL',
   5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'}
CENTENAS = {
   0:'',  1:'C',  2:'CC',  3:'CCC',  4:'CD',
   5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'}

# CARA não sei se fiz isso de uma boa forma não kkkkkkkk 
# mas deu certo po :) me quebrou esse exericcio kkkk
def roman_convert(number):
   """Converte números inteiros em números romanos. \n (int) -> str"""


   # Coloquei essa condicional, não sei se podia mas não tem nd escrito q não podia... 
   # Minha função só funciona para número menores que 1000
   if number > 999: 
      return "NÚMERO GRANDE DEMAIS!"
   numero = str(number)   

   # Fiz um sisteminha pra transformar cada algarismo em uma chave pro dicionario kkkkkkk                                              
   c = d = u = 0
   if number > 99:
      c = int(numero[-3])
   if number > 9:
      d = int(numero[-2])
   u = int(numero[-1])


   new_number = f"{CENTENAS[c]}{DEZENAS[d]}{UNIDADES[u]}"
   return new_number


n = 987
print(f"{n} em números romanos é {roman_convert(n)}")








