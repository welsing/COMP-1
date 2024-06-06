#===============================================================================
# COMPUTAÇÃO 1 - 2024.1 - LISTA DE EXERCÍCIOS 7
# Entregar até sexta (31-maio-2024)!
# Aluno: BERNARDO WELSING FERNANDES
# DRE: 124031228
#===============================================================================


def barra(tamanho, caractere="*", exer=0):
    """Imprime uma barra de caracteres e o número do exercicio.
    (int, str, int) -> None
    """
    print(caractere * tamanho)
    if exer != 0: print(" "*tamanho,f">> EXERCÍCIO {exer} <<\n")


# ==============================================================================
# EXERCÍCIO 1  
# ===========
# Crie uma função usando laço FOR que retorna uma sequência de Fibonacci, na
# forma de lista. A sequência deve conter n elementos, onde n será o argumento
# da função. Lembre-se que, como a lista já começa com [1, 1], então você vai
# precisar de mais n-2 elementos, ou seja, um iterável que vai de 2 a n (fora).

barra(20,"-=",1)
def fibonacci(n):
    """ Retorna uma lista da sequencia de fibonacci com a quantidades de elementos determinados.\n
    (int) -> list """
    fibo = [1,1]
    for i in range(2, n):
        fibo.append(fibo[-1] + fibo[-2])
    
    return fibo


# casos de teste
print(fibonacci(5))  # Aparecer 5 números no output


# ==============================================================================
# EXERCÍCIO 2
# ===========
# Usamos muitos exemplos lúdicos mas não podemos esquecer o principal motivo
#  pelo qual os computadores foram inventados: processamento de dados! E uma
# das tarefas mais comuns é a multiplicação de vetores. Agora, imagine vetores
# representados por tuplas, e.g.
# a = (1, 2, 3, 4)
# b = (-5, -6, -7, -8)
# Escreva uma função, usando laços for e zip, para retornar a soma de dois
# vetores na forma de tupla. O resultado da soma de a com b será:
# (1+(-5), 2+(-6), 4+(-7), 5+(-8)) = (-4, -4, -4, -4)
#
# Há duas formas de criar tuplas:
# 1)	Crie uma lista da forma que já vimos, usando list.append() para anexar
#     elementos novos à lista, e então, converta a lista para tupla usando
#     a função tuple().
# 2)	Comece com uma tupla vazia: t = (); depois, em cada iteração, acrescente
#     uma tupla com o elemento novo, i.e. t += (n,).
#
# Coloque dois casos de teste com o valor esperado em comentários.
# OBS.: Laços FOR de uma linha não serão aceitos!  # COMO ASSIM?


barra(20,"-=",2)

# 1) Criando listas e depois transformando em tuplas

# def soma_Vet(x, y):
#    """Realiza a soma de 2 vetores \n (tuple, tuple) -> tuple"""
#    new_Vet = []
#    for n, m in zip(x,y):
#        soma = n+m            ## Não entendi pq não é aceito só 1 linha no FOR....
#        new_Vet.append(soma)
#    return tuple(new_Vet)


# 2) Trabalhando com interação de tuplas

def soma_Vet(x, y):
    """Realiza a soma de 2 vetores \n (tuple, tuple) -> tuple"""
    new_Vet = ()
    for n, m in zip(x,y):
        s = n+m
        new_Vet += (s, )           
    return new_Vet


# casos de testes
a = (1, 2, 3, 4)
b = (-5, -6, -7, -8)
c = (2, 4, 6, 8)
print(soma_Vet(a, b)) # (-4, -4, -4, -4)
print(soma_Vet(a, c)) # (3, 6, 9, 12)






# ==============================================================================
# EXERCÍCIO 3
# ===========
# Uma frase estilizada causa impacto! Crie uma função que pegue uma string e
# passe todas as vogais para minúscula e consoantes para maiúscula. A função
# deve retornar a string estilizada. Apresente um caso de teste.
barra(20,"-=",3)
def text_modify(texto):
    """Estiliza strings. Transforma vogais em minusculas e consoantes em maiusculas \n (str) -> str"""
    new_text = ""
    for letra in texto:
        if letra in "AEIOUÁÉÍÓÚÂÊÎÔÛ":
            letra = letra.lower()
        
        if letra in "bcdfghjklmnpqrstvxwyz":
            letra = letra.upper()
        
        new_text += letra
    return new_text
            
        
# CASOS DE TESTE
print(text_modify("Só quero JogAR loL")) # Só QueRo JoGaR LoL
print(text_modify("PyThON É SENsacional")) # PYTHoN é SeNSaCioNaL

# ==============================================================================
# EXERCÍCIO 4
# ===========
# Na última aula, você criou uma função para calcular o produto escalar de dois
# vetores com duas componentes cada. Agora crie, usando for com zip, uma função
# prod_esc para calcular o produto escalar de vetores com mais componentes:
#   (a_0,a_1,a_2,…)⋅(b_0,b_1,b_2,…) => a_0 b_0 + a_1 b_1 + a_2 b_2 + ...

# A melhor forma de fazer isso é multiplicar cada par de componentes e somar as
# componentes ao acumulador. Utilize os seguintes casos de teste para ver se
# funcionou:

barra(20,"-=",4)

def prod_esc(x, y):
    """Realiza o produto de vetores com componentes ilimitados. \n (tuple, tuple) -> int"""
    h = 0
    for n, m in zip(x, y):
        h += n*m
    return h


# CASOS DE TESTE
a = (3, 9, -1, 2)
b = (-5, -5, 0, 0)
c = (1, 1, 1, 1)
print( prod_esc(a, b) )  # -60
print( prod_esc(a, c) )  # 13
print( prod_esc(b, c) )  # -10

