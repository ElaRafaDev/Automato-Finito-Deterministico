# Função para conversão de string para inteiro
def conversao_int(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        return False


# Função que faz a conversão de estados
def conversao_estados(primeiro_estado, palavra):
    transicao_estados.append(tabela_transicao[estados.index(primeiro_estado)][alfabeto.index(palavra)])
    return tabela_transicao[estados.index(primeiro_estado)][alfabeto.index(palavra)]


# Recebe a quantidade de estados do autômato
qnt_estados = False
while not qnt_estados:
    qnt_estados = conversao_int(input("Informe a quantidade de estados: "))
    if not qnt_estados:
        print('Informe um valor válido para a quantidade de estados!')

# Recebe os estados do autômato
estados = [input(f'Informe o {i + 1}° estado: ') for i in range(0, qnt_estados)]

# Recebe o tamanho do alfabeto do autômato
qnt_alfabeto = False
while not qnt_alfabeto:
    qnt_alfabeto = conversao_int(input('Informe o tamanho do alfabeto: '))
    if not qnt_alfabeto:
        print('Informe um valor válido para o tamanho do alfabeto!')

# Recebe o alfabeto do autômato
alfabeto = [input(f'Informe a {i + 1}ª chave do alfabeto: ') for i in range(0, qnt_alfabeto)]

# Recebe o estado inicial do autômato
estado_inicial = False
while not estado_inicial:
    estado_inicial = input('Informe o estado inicial: ')
    if estado_inicial not in estados:
        print('Este estado não existe!')
        estado_inicial = False

# Recebe o estado final do autômato
estado_final = False
while not estado_final:
    estado_final = input('Informe o estado final: ')
    if estado_final not in estados:
        print('Este estado não existe!')
        estado_final = False

# Recebe a tabela de transição do autômato
print('Informe a tabela de transição: ')
tabela_transicao = [0 for i in range(len(estados))]
for i in range(len(estados)):
    tabela_transicao[i] = [0 for j in range(len(alfabeto))]
    for j in range(len(alfabeto)):
        tabela_transicao[i][j] = input(f'Estado ({estados[i]}), chave ({alfabeto[j]}) : ')

flag = True
while flag:
    # Inicialização da lista que armazena a transição de estados
    transicao_estados = []

    # Mantém o estado inicial informado pelo o usuário
    indice_estado_inicial = estado_inicial

    # Recebe a string do autômato
    string = input('Informe a string: ')

    # Realiza a transisição de estados
    for indice in string:
        indice_estado_inicial = conversao_estados(indice_estado_inicial, indice)

    # Determina se a string foi aceita ou não
    print('Aceitou' if transicao_estados[-1] == estado_final else 'Rejeitou')

    escolha = False
    while not escolha:
        escolha = input('Deseja informar outra string? (S/N) ')

        if escolha.lower() == 's':
            print('Retornando . . .')
            flag = True
        elif escolha.lower() == 'n':
            print('Finalizando . . .')
            flag = False
        else:
            escolha = False
            print('Informe apenas "S" para sim ou "N" para não!')
