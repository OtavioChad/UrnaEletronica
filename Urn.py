import random
from random import choice
from time import sleep
from datetime import datetime
data_hora_formatada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(data_hora_formatada)

#CHAVE - VALIDATION (82731642)

#Global 
def get_limited_input(prompt, min_length, max_length):
    while True:
        user_input = input(prompt)
        if min_length <= len(user_input) <= max_length:
            return user_input
        else:
            print(f"A entrada deve ter entre {min_length} e {max_length} caracteres. Tente novamente.")

# Usar a função para obter uma senha com limite
chave = int(get_limited_input("Digite a chave de cominicação: ", 1, 5))
hashtxt = input('\nDIGITE A VALIDAÇÃO DO ARQUIVO:\n')
escolha = int(input("[1]PRESIDENTIAL\n[2]MUNICIPAL \nESCOLHA:"))
votos = [] #Armazenamento de votos 



# NUMERO DE 4 DIGITOS
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

# Impressão dos candidatos
def imprimir_candidatos(titulo, lista_candidatos):
    print(f"\n{titulo}:")
    for candidato in lista_candidatos:
        print(f"{candidato[0]} - {candidato[1]} - {candidato[2]}")


def decimalToBinary(value):

    global binaryText 
    
    binaryText = ""

    if value > 0:

        decimalToBinary(value // 2)

    binaryText += str(value % 2)
    


def Cryptrography1(frase):
    
    mensagem = ''

    for i in frase:

        mensagem += chr(ord(i) + chave)

    return mensagem    

def Cryptrography2(conteudo):
    messageSampleFinal = ""
    position = 0
    messageSampleArray = []
    traps = [r"H"]

    textInputLength = len(conteudo)
    textToArray = [char for char in conteudo]

    for x in textToArray:

        decimalToBinary(ord(x))

        position = position + 1
        hexPosition = hex(position)
        hexPosition = str(hexPosition)
        hexPosition = hexPosition.replace("0x", "")

        code1Array = [char for char in binaryText]
        code1Final = ""

        for z in code1Array:

            if z == "1":
                code1Reversion = "0"
            elif z == "0":
                code1Reversion = "1"
            code1Final +=code1Reversion

        trapText1 = choice(traps)
        trapText2 = choice(traps)

        messageSample = code1Final + trapText1 + hexPosition + trapText2
        messageSampleArray.insert(random.randint(0, textInputLength), messageSample)

    for z in messageSampleArray:

        messageSampleFinal = messageSampleFinal + z
        print(20 * '===')
    messageSampleFinal = Cryptrography1(messageSampleFinal)
    return messageSampleFinal

def Election(escolha):
    urnactivated = 1
    ultimo = 0
    while urnactivated == 1:
        if escolha == 1:
            while ultimo == 0:
                while True:             
                    imprimir_candidatos("DEPUTADO FEDERAL", FederalDeputy)
                    voto = input("\nDIGITE SEU VOTO PARA DEPUTADO FEDERAL:\n")
                    voto = Cryptrography2(voto).strip()
                    decisão = int(input("[1]CORRIGIR [2]CONFIRMAR\n"))
                    if decisão == 2:
                        votos.append(voto)
                        break
                    else:
                        print("DIGITE NOVAMENTE")   
                    
                    
                while True:             
                    imprimir_candidatos("DEPUTADO ESTADUAL", StateDeputy)
                    voto = input("\nDIGITE SEU VOTO PARA DEPUTADO ESTADUAL:\n")
                    voto = Cryptrography2(voto).strip()
                    decisão = int(input("[1]CORRIGIR [2]CONFIRMAR\n"))
                    if decisão == 2:
                        votos.append(voto)
                        break
                    else:
                        print("DIGITE NOVAMENTE")   
                    
                    
                while True:
                    imprimir_candidatos("SENADOR", Senator)          
                    voto = input("\nDIGITE SEU VOTO PARA SENADOR:\n")
                    voto = Cryptrography2(voto).strip()
                    decisão = int(input("[1]CORRIGIR [2]CONFIRMAR\n"))
                    if decisão == 2:
                        votos.append(voto)
                        break
                    else:
                        print("DIGITE NOVAMENTE")   
                    
                    
                while True:
                    imprimir_candidatos("GOVERNADOR", Governor)             
                    voto = input("\nDIGITE SEU VOTO PARA GOVERNADOR:\n")
                    voto = Cryptrography2(voto).strip()
                    decisão = int(input("[1]CORRIGIR [2]CONFIRMAR\n"))
                    if decisão == 2:
                        votos.append(voto)
                        break
                    else:
                        print("DIGITE NOVAMENTE")   
                    
                    
                while True:
                    imprimir_candidatos("PRESIDENTE", President)              
                    voto = input("\nDIGITE SEU VOTO PARA PRESIDENTE:\n")
                    voto = Cryptrography2(voto).strip()
                    decisão = int(input("[1]CORRIGIR [2]CONFIRMAR\n"))
                    if decisão == 2:
                        votos.append(voto)
                        break
                    else:
                        print("DIGITE NOVAMENTE")
                urnactivated = int(input("\nDESEJA CONTINUAR A VOTAÇÃO?\n[1]SIM [2]NÃO\n"))
                if urnactivated == 1:
                    ultimo = 0
                else:
                    break
                
        elif escolha == 2:
            while ultimo == 0:
                while True:
                    imprimir_candidatos("VEREADOR", Councilman)              
                    voto = input("\nDIGITE SEU VOTO PARA VEREADOR:\n")
                    voto = Cryptrography2(voto).strip()
                    decisão = int(input("[1]CORRIGIR [2]CONFIRMAR\n"))
                    if decisão == 2:
                        votos.append(voto)
                        break
                    else:
                        print("DIGITE NOVAMENTE")   
                        
                        
                while True:
                    imprimir_candidatos("PREFEITO", Mayor)              
                    voto = input("\nDIGITE SEU VOTO PARA PREFEITO:\n")
                    voto = Cryptrography2(voto).strip()
                    decisão = int(input("[1]CORRIGIR [2]CONFIRMAR\n"))
                    if decisão == 2:
                        votos.append(voto)
                        break
                    else:
                        print("DIGITE NOVAMENTE")
                urnactivated = int(input("\nDESEJA CONTINUAR A VOTAÇÃO?\n[1]SIM [2]NÃO\n"))
                if urnactivated == 1:
                    ultimo = 0
                else:
                    break
                
    print('VOTAÇÃO CONCLUIDA!')
    sleep(3)      
    print('CARREGANDO NOVA VOTAÇÃO...')
    sleep(5)
    
    for item in votos:
        lista = list(map(str, range(10001)))
        for i in lista:
            with open("file/" +hashtxt+i, "w", encoding="utf-8") as gravar:
                gravar.write('%s\n' % (hashtxt+i))
                for item in votos:
                    gravar.write('%s\n' % item)

Election(escolha)


