# A- Crie os 3 conjuntos ao lado.
# B- Quais bichos nadam OU voam? Golfinho, jacaré, homem, sabiá, pato, galinha
# C- Quais bichos nadam mas não conseguem voar? Jacaré, homem, golfinho
# D- Quais bichos voam mas não conseguem nadar? Sabiá, galinha.
# E- Galinha está no conjunto (C)? Sim 
# F- Quais bichos conseguem andar e voar? Galinha e pato
# G- Quais bichos de (f) começam com a letra g? 

nadam = {"golfinho", "jacaré", "homem", "pato"}
andam = {"vaca", "gato", "jacaré", "homem", "pato", "galinha"}
voam = {"sabiá", "galinha", "pato"}

print(nadam.union(voam)) #B

c = (nadam.difference(voam)) #C

print(voam.difference(nadam)) #D


print("Galinha está no conjunto 'C'", "galinha" in c) #E

f = (andam.intersection(voam)) #F

for bichos in f: #G
    if bichos[0] == "g":
        print(bichos)

#Quantas letras diferentes existem em "O rato roeu a ropa do rei de Roma, por isso não ganhou queijo."
#Quantas vogais e consoantes tem?

frase = "O rato roeu a ropa do rei de Roma, por isso não ganhou queijo.".lower()

frasenova = ""
for letra in frase:
    if letra in ".,ã ":
        ""
    else:
        frasenova += letra
print(frasenova)

frase = set(frasenova)
print(frase)

vogais = 0
consoantes = 0
for letra in frase:
    if letra in "aeiou":
        vogais += 1
    else:
        consoantes +=1

print("")