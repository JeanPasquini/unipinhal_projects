import automatoFinitoDeterministico as afd
import os
import platform

#limpar console
def clr():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


clr()
#estados
while True:
    estadosEntrada = input(f"Defina os estados (Separe os componentes com ',')\n\n(Exemplo: q0, q1)\n-----------------------\n\n")
    estados = estadosEntrada.split(',')
    estados = [componente.strip() for componente in estados]
    if len(estados) == len(set(estados)):
        break
    else:
        clr()
        print("AVISO - O conjunto de Estados contém valores repetidos. Por favor, defina o conjunto com valores únicos.\n")

clr()
#alfabeto
while True: 
    alfabetoEntrada = input("Defina o alfabeto (Separe os componentes com ',')\n\n(Exemplo: 0, 1)\n-----------------------\n\n")
    alfabeto = alfabetoEntrada.split(',')
    alfabeto = [componente.strip() for componente in alfabeto]
    if len(alfabeto) == len(set(alfabeto)):
        break
    else:
        clr()
        print("AVISO - O alfabeto contém valores repetidos. Por favor, defina um alfabeto com valores únicos.\n")
    
clr()
#transicoes
print("Defina as transições a seguir\n\n(Exemplo: q0 : '0' = q1)\n-----------------------\n")
transicoes = {est: {} for est in estados}

for est in estados:
    for alf in alfabeto:
        while True:
            proximo_estado = input(f"{est} : '{alf}' = ")
            if (proximo_estado in estados or proximo_estado == '-'):
                transicoes[est][alf] = proximo_estado
                break
            else:
                clr()
                print('AVISO - Este estado não esta contido no conjunto de estados\n')
 
clr()
#estado inicial
while True:
    estado_inicial = input("Defina o estado inicial\n\n(Exemplo: q0)\n-----------------------\n\n")
    if not(estado_inicial in estados):
        clr()
        print('AVISO - Este estado não esta contido no conjunto de estados\n')
    else:
        break

clr()
#conjunto de estados finais
while True:
    estadosFinaisEntrada = input("Defina o conjunto de estados finais (Separe os componentes com ',')\n\n(Exemplo: q0, q1)\n-----------------------\n\n")

    conjunto_estados_finais = {estado.strip() for estado in estadosFinaisEntrada.split(',')}
    if len(conjunto_estados_finais) != len(set(conjunto_estados_finais)):
        print("Os estados finais contêm valores repetidos. Por favor, defina um conjunto de estados finais com valores únicos.")
        continue

    if not conjunto_estados_finais.issubset(estados):
        clr()
        print('AVISO - Um ou mais estados finais não estão contidos no conjunto de estados válidos.\n')
    else:
        break

#pergunta de leitura
while True:
    clr()
    print(f'Q : {estados}\nΣ : {alfabeto}\nδ : {transicoes}\nq0: {estado_inicial}\nQf: {conjunto_estados_finais}')

    entrada = input('\n-----------------------\n\nDefina o que deseja ler: ')

    teste = afd.AFD(estados, alfabeto, transicoes, estado_inicial, conjunto_estados_finais)

    clr()
    if teste.processar_entrada(entrada):
        print(f"FOI ACEITO! A entrada '{entrada}'\n\n-----------------------\n")
    else:
        print(f"FOI REJEITADA! A entrada '{entrada}'\n\n-----------------------\n")
    
    outroTeste = input("Deseja criar outra entrada? \ns = 'Sim'\nDigite qualquer coisa = 'Não'\n")

    if(outroTeste == 's'):
        pass
    else:
        break