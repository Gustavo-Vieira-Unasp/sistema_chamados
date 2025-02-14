def cadastrar_chamados(nome, motivo, descrissão):
    nome = input("Insira seu nome:")
    motivo = motivo_chamado()
    descrissão = input("Descreva com mais detalhes o motivo")


def motivo_chamado():
    razao = True
    while razao == True:
        print("\n 1. Sistema fora do ar \
               \n 2. Problemas de conexão \
               \n 3. Aparelho fora de funcionamento\
               \n 4. Problema não identificado")
    pass