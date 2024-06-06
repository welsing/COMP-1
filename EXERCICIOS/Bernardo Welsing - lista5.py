#===============================================================================
# COMPUTAÇÃO 1 - 2024.1 - LISTA DE EXERCÍCIOS 5
# Entregar até sexta (3-abril-2024)!
# Aluno: BERNARDO WELSING FERNANDES
# DRE: 124031228
# ==============================================================================
# EXERCÍCIO 1  
# ===========
# Com o poder da repetição você pode até impressionar seus colegas! Gere uma
# sequência de Fibonacci com 1000 números. Para funcionar, a lista deve começar
# com pelo menos dois números. Então, provavelmente, você vai querer um contador
# que vá de 2 até 1000 (excluso) com incremento AO FINAL da iteração. Depois,
# divida o penúltimo número da lista pelo último. O valor resultante é chamado
# de Razão Áurea.

fibo = [1, 1]
# i = 2                          COM CONTADOR
# while i <= 1000:
#    soma = fibo[-1] + fibo[-2]
#    fibo.append(soma)
#    i += 1

while len(fibo) <= 1000:       # SEM CONTADOR
   soma = fibo[-1] + fibo[-2]
   fibo.append(soma)

#print(fibo)
print("O NÚMERO DE OURO (R. ÁUREA): {:.4f}".format(fibo[-1]/fibo[-2]))
print("#"*30, "\n") # apenas um separador


# ==============================================================================
# EXERCÍCIO 2
# ===========
# Escreva um código que pergunte um inteiro n e imprima sua tabuada usando um
# laço while. A saída deve ter o seguinte formato (para n=5 por exemplo):
#   5 x 1  = 5
#   5 x 2  = 10
#   5 x 3  = 15
#   5 x 4  = 20
#   5 x 5  = 25
#   5 x 6  = 30
#   5 x 7  = 35
#   5 x 8  = 40
#   5 x 9  = 45
#   5 x 10 = 50 

count = 1
n = int(input("DIGITE UM NÚMERO INTEIRO: "))
print(f" # TABUADA DE {n} #")
while count <= 10:
   print("{:3} x {:2} = {:3}".format(count, n, count*n))
   count += 1
print("#"*20, "\n")


# ==============================================================================
# EXERCÍCIO 3
# ===========
# Variáveis acumuladoras são essenciais em computação. Sem uma variável
# acumuladora, não conseguiríamos calcular a soma de uma P.A. de 1 a 1000,
# i.e.  1 + 2 + 3 + ... + 998 + 999 + 1000. O código a seguir faz isso:
soma = 0
k = 1
while k <= 1000:
   soma = soma + k
   k = k + 1
print(f"Soma = {soma}")

# Crie um código para calcular o fatorial de um número n, i.e.
# 1 x 2 x 3 x ... x (n-1) x n.


n = i = result = 5      
while i > 1:
   i -= 1
   result = result*i
   
print(f"-- A fatorial de {n} é {result}")
print("#"*20, "\n")


# ==============================================================================
# EXERCÍCIO 4
# ===========
# Uma professora deseja guardar a nota final de seus alunos em uma lista. Claro
# que precisamos guardar o nome dos alunos também, para saber de quem é a nota.
# Portanto, modifique o exemplo da Aula 6 para perguntar nome e nota do aluno,
# e guarde-os em listas separadas (o tipo de variável para nota é float).
# Um exemplo de interação com o usuário no Terminal seria:
#
# Digite nome e nota de cada aluno:
#   nome? Marco Aurélio<ENTER>
#   nota? 9.4
#   nome? Giovanna<ENTER>
#   nota? 9.8
#   nome? fim
# Obrigado professor!
# A média da turma é 9.6

nomes = []
notas = []

print("-- MÉDIA DOS ALUNOS DA TURMA --")

while True:
   aluno = input("NOME DO ALUNO: ").capitalize()
   nomes.append(aluno)
   nota = float(input(f"NOTA DO(a) {aluno}: "))
   notas.append(nota)
   print(f"{aluno} REGISTRADO COM NOTA {nota}")
   
   soun = input("Deseja continuar? [S/N]: ").upper().strip()[0] 
   if soun == "N":
      break

média = sum(notas) / len(notas)
print(f"A MEDIA DA TURMA É: {média:.1f}")



# ==============================================================================
# EXERCÍCIO 5
# ===========
# Leia a Seção "Construindo strings" da Aula 6. Copie o código do Jogo da Forca
# e cole no site:    
# Mude a palavra a ser adivinhada, as letras reveladas e clique em
# "Visualize Execution". Faça o passo-a-passo do programa com ajuda do
# pythontutor, e preencha uma tabela como aquelas que fizemos em aula,
# para acompanhar a evolução das variáveis i, letra e mostrar.
#
#   i   |    letra   |   mostrar   |
# ------|------------|--------------
#   0   |     "a"    |  "a"        #
#   1   |     "b"    |  "a_"       #
#   2   |     "a"    |  "a_A"      # 
#   3   |     "c"    |  "a_a_"     #
#   4   |     "a"    |  "a_a_a"    #
#   5   |     "t"    |  "a_a_a_"   #
#   6   |     "e"    |  "a_a_a__"  #
####################################

# ==============================================================================
# EXERCÍCIO 6 (Não vale ponto)
# ===========
# Vamos descriptografar uma string que foi criptografada assim:
frase = "O rato roeu a roupa do Rei de Roma"
cripto = frase[::2] + frase[1::2]

# Precisamos desfazer os passos da criptografia. Primeiro, separamos a frase
# em duas metades:
i = len(cripto)//2
parte1 = cripto[:i]
parte2 = cripto[i:]

# Agora, você pode recriar a frase original juntando o caractere parte1[i]
# com o caractere parte2[i].
descripto = ""
# Coloque seu código aqui

num = 0                       ## Foi o jeito que consegui fazer, na tentativa e erro e logica, mas realmente acho que não entendi 100% kkkkk 
print(f"PARTE 1: {parte1}")   ## fiquei uns 40mins nisso
print(f"PARTE 2: {parte2}")
while num <= 16:
   #cripto[i]
   #print(parte1[i], end="")
   descripto += parte1[num]
   #print(parte2[i], end="")
   descripto += parte2[num]
   num += 1


print(descripto)