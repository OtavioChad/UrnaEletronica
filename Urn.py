import random
import base64
import time
from random import choice
from time import sleep
from datetime import datetime

data_hora_formatada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(data_hora_formatada)

def get_limited_input(prompt, min_length, max_length):
    while True:
        user_input = input(prompt)
        if min_length <= len(user_input) <= max_length:
            return user_input
        else:
            print(f"A entrada deve ter entre {min_length} e {max_length} caracteres. Tente novamente.")

votos = [] #Armazenamento de votos 
chave = int(get_limited_input("Digite a chave de comunicação: ", 1, 3))
hashtxt = input('\nDIGITE A VALIDAÇÃO DO ARQUIVO:\n')
escolha = int(input("[1]PRESIDENTIAL\n[2]MUNICIPAL \nESCOLHA:"))
DuraçãoSessão = int(input('DIGITE A DURAÇÃO DA SESSÃO ELEITORAL'))
chaveXor = 'e698d09ee932bfda22360ac27a10f37271834eca9fd7a7efb3aecb36009ffc5eee8a20e5710b0da05c898ba7e2cdeb4d1c9b754f00726e36a7177d3466925215'

FederalDeputy = [  
    ["Alice", "Partido A", 1000],
    ["Marcelo", "Partido B", 2000],
    ["Luan", "Partido C", 3000],
    ["Marcos", "Partido D", 4000],
    ["Maria", "Partido E", 5000],
    ["Tiago", "Partido F", 6000],
    ["Julia", "Partido G", 7000],
    ["Fernando", "Partido H", 8000],
    ["Rafaela", "Partido I", 9000],
    ["Bruno", "Partido J", 1100],
    ["Isabela", "Partido K", 2200],
    ["Carlos", "Partido L", 3300],
    ["Patrícia", "Partido M", 4400],
    ["Nicolas", "Partido N", 5500],
    ["Olivia", "Partido O", 6600],
    ["Juliana", "Partido P", 7700],
    ["Sérgio", "Partido Q", 8800],
    ["Ana", "Partido R", 9900],
    ["Hugo", "Partido S", 1001],
    ["Mariana", "Partido T", 2001],
]

# NUMEROS DE 5 DIGITOS

StateDeputy = [
    ["Aline", "Partido A", 10000],
    ["Bruno", "Partido B", 20000],
    ["Clara", "Partido C", 30000],
    ["Daniel", "Partido D", 400000],
    ["Fernanda", "Partido E", 50000],
    ["Gabriel", "Partido F", 60000],
    ["Helena", "Partido G", 70000],
    ["Igor", "Partido H", 80000],
    ["Júlia", "Partido I", 90000],
    ["Karla", "Partido J", 11000],
    ["Lucas", "Partido K", 22000],
    ["Marta", "Partido L", 33000],
    ["Nicolas", "Partido M", 44000],
    ["Olga", "Partido N", 55000],
    ["Paulo", "Partido O", 66000],
    ["Quitéria", "Partido P", 77000],
    ["Renato", "Partido Q", 88000],
    ["Sofia", "Partido R", 99000],
    ["Tiago", "Partido S", 10001],
    ["Ursula", "Partido T", 20001],
]

# NUMEROS DE 3 DIGITOS

Senator = [
    ["Gustavo", "Partido A", 100],
    ["Helena", "Partido B", 200],
    ["Carlos", "Partido C", 300],
    ["Rafaela", "Partido D", 400],
    ["André", "Partido E", 500],
    ["Fernanda", "Partido F", 600],
    ["João", "Partido G", 700],
    ["Mariana", "Partido H", 80],
    ["Tiago", "Partido I", 900],
    ["Bruno", "Partido J", 110],
    ["Clara", "Partido K", 220],
    ["Daniel", "Partido L", 330],
    ["Eduarda", "Partido M", 440],
    ["Roberto", "Partido N", 550],
    ["Sofia", "Partido O", 660],
    ["Lucas", "Partido P", 77],
    ["Patrícia", "Partido Q", 880],
    ["Nicolas", "Partido R", 990],
    ["Isabela", "Partido S", 101],
    ["Helena", "Partido T", 201],
]
# NUMEROS DE 2 DIGITOS
Governor = [
    ["Igor", "Partido A", 10],
    ["Juliana", "Partido B", 20],
    ["Fábio", "Partido C", 30],
    ["Roberta", "Partido D", 40],
    ["Thiago", "Partido E", 50],
    ["Laura", "Partido F", 60],
    ["Jorge", "Partido G", 70],
    ["Amanda", "Partido H", 80],
    ["Henrique", "Partido I", 90],
    ["Natália", "Partido J", 11],
    ["Vitor", "Partido K", 22],
    ["Simone", "Partido L", 33],
    ["Marcio", "Partido M", 44],
    ["Sabrina", "Partido N", 55],
    ["Ricardo", "Partido O", 66],
    ["Cecília", "Partido P", 77],
    ["Murilo", "Partido Q", 88],
    ["Júlia", "Partido R", 99],
    ["Otávio", "Partido S", 11],
    ["Vanessa", "Partido T", 21],
]

# NUMEROS DE 2 DIGITOS

President = [
    ["Karla", "Partido A", 10],
    ["Lucas", "Partido B", 20],
    ["Patrícia", "Partido C", 30],
    ["Gustavo", "Partido D", 40],
    ["Rafaela", "Partido E", 50],
    ["Eduardo", "Partido F", 60],
    ["Marta", "Partido G", 70],
    ["Nicolas", "Partido H", 80],
    ["André", "Partido I", 90],
    ["Clara", "Partido J", 11],
    ["Rafael", "Partido K", 22],
    ["Juliana", "Partido L", 33],
    ["Fábio", "Partido M", 44],
    ["Lucas", "Partido N", 55],
    ["Ana", "Partido O", 66],
    ["Tiago", "Partido P", 77],
    ["Mariana", "Partido Q", 88],
    ["Helena", "Partido R", 99],
    ["Isabela", "Partido S", 11],
    ["Hugo", "Partido T", 21],
]

# NUMEROS DE 5 DIGITOS

Councilman = [
    ["Mariana", "Partido A", 10000],
    ["Nicolas", "Partido B", 20000],
    ["Olivia", "Partido C", 30000],
    ["Paulo", "Partido D", 40000],
    ["Quitéria", "Partido E", 50000],
    ["Rafael", "Partido F", 60000],
    ["Sofia", "Partido G", 70000],
    ["Thiago", "Partido H", 80000],
    ["Victor", "Partido I", 90000],
    ["Zara", "Partido J", 11000],
    ["Rita", "Partido K", 22000],
    ["Danilo", "Partido L", 33000],
    ["Gustavo", "Partido M", 44000],
    ["Lúcia", "Partido N", 55000],
    ["Frederico", "Partido O", 66000],
    ["Simone", "Partido P", 77000],
    ["Tiago", "Partido Q", 88000],
    ["Fátima", "Partido R", 99000],
    ["Ricardo", "Partido S", 10001],
    ["Marta", "Partido T", 20001],
]

# NUMEROS DE 2 DIGITOS

Mayor = [
    ["Rafael", "Partido A", 10],
    ["Sofia", "Partido B", 20],
    ["Hugo", "Partido C", 30],
    ["Marcos", "Partido D", 40],
    ["Daniel", "Partido E", 50],
    ["Gustavo", "Partido F", 60],
    ["Juliana", "Partido G", 70],
    ["Ricardo", "Partido H", 80],
    ["Fernanda", "Partido I", 90],
    ["Aline", "Partido J", 11],
    ["Paulo", "Partido K", 22],
    ["Cláudia", "Partido L", 33],
    ["Bruno", "Partido M", 44],
    ["Sérgio", "Partido N", 55],
    ["Karla", "Partido O", 66],
    ["Natália", "Partido P", 77],
    ["Rafael", "Partido Q", 88],
    ["Victor", "Partido R", 99],
    ["Tiago", "Partido S", 11],
    ["Eduarda", "Partido T", 21],
]

# CHAVE - VALIDATION (82731642)

# Função para obter entrada do usuário com limite de caracteres
def get_limited_input(prompt, min_length, max_length):
    """
    Solicita uma entrada do usuário e garante que esteja dentro de um limite de caracteres.

    Parâmetros:
    prompt (str): Mensagem a ser exibida ao usuário.
    min_length (int): Comprimento mínimo da entrada.
    max_length (int): Comprimento máximo da entrada.

    Retorna:
    str: A entrada do usuário que atende aos requisitos de comprimento.
    """
    while True:
        user_input = input(prompt)
        if min_length <= len(user_input) <= max_length:
            return user_input
        else:
            print(f"A entrada deve ter entre {min_length} e {max_length} caracteres. Tente novamente.")

# Função para imprimir a lista de candidatos
def imprimir_candidatos(titulo, lista_candidatos):
    """
    Imprime a lista de candidatos com seus respectivos partidos e números.

    Parâmetros:
    titulo (str): Título da eleição (ex: "DEPUTADO FEDERAL").
    lista_candidatos (list): Lista de candidatos com informações.
    """
    print(f"\n{titulo}:")
    for candidato in lista_candidatos:
        print(f"{candidato[0]} - {candidato[1]} - {candidato[2]}")

def decimalToBinary(value):
    """
    Converte um número decimal para sua representação binária.

    Parâmetros:
    value (int): O número decimal a ser convertido.
    """
    global binaryText
    binaryText = ""

    if value > 0:
        decimalToBinary(value // 2)

    binaryText += str(value % 2)
    
# Função auxiliar para coletar voto
def coletar_voto(titulo, lista_candidatos):
    """
    Coleta um voto do usuário para um determinado título e lista de candidatos.

    Parâmetros:
    titulo (str): Título da eleição (ex: "DEPUTADO FEDERAL").
    lista_candidatos (list): Lista de candidatos disponíveis para votação.

    Retorna:
    str: O voto criptografado do usuário.
    """
    imprimir_candidatos(titulo, lista_candidatos)
    while True:
        voto = input(f"\nDIGITE SEU VOTO PARA {titulo.upper()}:\n")
        voto = Cryptrography2(voto).strip()
        decisao = int(input("[1]CORRIGIR [2]CONFIRMAR\n"))
        if decisao == 2:
            return voto
        else:
            print("DIGITE NOVAMENTE")

def Cryptrography1(frase):
    """
    Aplica uma criptografia simples ao deslocar os caracteres da string.

    Parâmetros:
    frase (str): A string a ser criptografada.

    Retorna:
    str: A string criptografada.
    """
    mensagem = ''
    for i in frase:
        mensagem += chr(ord(i) + chave)
    return mensagem

def Cryptrography2(conteudo):
    """
    Aplica um método de criptografia complexo ao conteúdo.

    Parâmetros:
    conteudo (str): A string a ser criptografada.

    Retorna:
    str: A string criptografada.
    """
    messageSampleFinal = ""
    position = 0
    messageSampleArray = []
    traps = [r"H"]

    textInputLength = len(conteudo)
    textToArray = [char for char in conteudo]

    for x in textToArray:
        decimalToBinary(ord(x))
        position += 1
        hexPosition = hex(position).replace("0x", "")
        code1Array = [char for char in binaryText]
        code1Final = "".join("0" if z == "1" else "1" for z in code1Array)

        trapText1 = choice(traps)
        trapText2 = choice(traps)

        messageSample = code1Final + trapText1 + hexPosition + trapText2
        messageSampleArray.insert(random.randint(0, textInputLength), messageSample)

    for z in messageSampleArray:
        messageSampleFinal += z
        print(20 * '===')
    messageSampleFinal = Cryptrography1(messageSampleFinal)
    messageSampleFinal = Cryptrography3(messageSampleFinal, chaveXor)
    return messageSampleFinal

def Cryptrography3(texto, chaveXor):
    """
    Aplica a operação XOR ao texto com uma chave e codifica o resultado em base64.

    Parâmetros:
    texto (str): O texto a ser criptografado.
    chaveXor (str): A chave usada na operação XOR.

    Retorna:
    str: O texto criptografado em base64.
    """
    resultado = bytearray()
    texto_bytes = texto.encode('utf-8')
    chave_bytes = chaveXor.encode('utf-8')
    
    for i in range(len(texto_bytes)):
        resultado.append(texto_bytes[i] ^ chave_bytes[i % len(chave_bytes)])
    
    return base64.b64encode(resultado).decode('utf-8')

def Election(escolha):
    """
    Gerencia o processo de votação com base na escolha do usuário.

    Parâmetros:
    escolha (int): A escolha do tipo de eleição (1 para federal, 2 para municipal).
    """
    start_time = time.time()  # Marca o início do tempo
    while True:
        current_time = time.time()  # Obtém o tempo atual
        elapsed_time = current_time - start_time  # Calcula o tempo decorrido

        if elapsed_time > DuraçãoSessão:
            print("\nTempo esgotado!")
            break

        if escolha == 1:
            votos.append(coletar_voto("DEPUTADO FEDERAL", FederalDeputy))
            votos.append(coletar_voto("DEPUTADO ESTADUAL", StateDeputy))
            votos.append(coletar_voto("SENADOR", Senator))
            votos.append(coletar_voto("GOVERNADOR", Governor))
            votos.append(coletar_voto("PRESIDENTE", President))
        elif escolha == 2:
            votos.append(coletar_voto("VEREADOR", Councilman))
            votos.append(coletar_voto("PREFEITO", Mayor))

    print('VOTAÇÃO CONCLUIDA!')
    sleep(2)      
    print('CARREGANDO NOVA VOTAÇÃO...')
    sleep(5)

    for item in votos:
        lista = list(map(str, range(1000)))
        for i in lista:
            with open("file/" + hashtxt + i, "w", encoding="utf-8") as gravar:
                gravar.write('%s\n' % (hashtxt + i))
                for item in votos:
                    gravar.write('%s\n' % item)


# Chamada da função principal
Election(escolha)