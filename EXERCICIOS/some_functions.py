def barra(tamanho, caractere="*", exer=0):
    """Imprime uma barra de caracteres e o número do exercicio.
    (int, str, int) -> None
    """
    print("\n")
    print(caractere * tamanho)
    #if exer != 0: print(" "*tamanho,f">> EXERCÍCIO {exer} <<\n")
    if exer != 0: print(f"{f">> EXERCÍCIO {exer} <<":>{tamanho}}")