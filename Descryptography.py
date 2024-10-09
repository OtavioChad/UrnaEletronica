from datetime import datetime
import os
data_hora_formatada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(data_hora_formatada)

def get_limited_input(prompt, min_length, max_length):
    while True:
        user_input = input(prompt)
        if min_length <= len(user_input) <= max_length:
            return user_input
        else:
            print(f"A entrada deve ter entre {min_length} e {max_length} caracteres. Tente novamente.")

# Usar a função para obter uma senha com limite
chave = int(get_limited_input("Digite a chave de cominicação: ", 1, 6))

# NUMERO DE 4 DIGITOS
federalDeputy = [
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

stateDeputy = [
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

senator = [
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
governor = [
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

president = [
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

councilman = [
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

mayor = [
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


votoscripto = [] # VOTOS CRIPTOGRAFADOS
votoslimpos = [] # VOTOS DESCRIPTOGRAFADOS
FederalDeputy = []  # 4
StateDeputy = []  # 5
Senator = []  # 2
Governor = []  # 2 
President = []  # 2
Councilman = []  # 5
Mayor = []  # 2

def Descryptrography1(mensagem):

    frase = ''

    for i in mensagem:

        frase += chr(ord(i) - chave)

    return frase

def Descryptrography2(messageSampleFinal):
    if linha:  # Verifica se a linha não está vazia
        messageSampleFinal = messageSampleFinal.strip()
        messageSampleFinal = Descryptrography1(messageSampleFinal)
        oddValue = 0
        messageList = list(messageSampleFinal.split('H'))
        messageList.pop()
        finalMessage = ""
        binaryLetter = ""
        finalMessageList = []
        messageListSize = len(messageList)/2
        messageListSize = int(messageListSize)

        while messageListSize > 0:

            finalMessageList += " "
            messageListSize = messageListSize - 1

        for x in messageList:
            
            blankBinary = ""
            messageToArray = [char for char in x]

            if oddValue == 0:

                for y in messageToArray:

                    if y == "1":
                        code1Reversion = "0"
                    elif y == "0":
                        code1Reversion = "1"
                
                    blankBinary += code1Reversion

                oddValue = 1

                binaryLetter = chr(int(blankBinary, 2))

            elif oddValue == 1:

                letterCurrentPosition = int(x, 16)
                finalMessageList[letterCurrentPosition-1] = binaryLetter
                oddValue = 0

        for z in finalMessageList:

                finalMessage += z  
        finalMessage = int(finalMessage)
        votoslimpos.append(finalMessage)
    else:
        return 0
    

verification = "607e0cfae779b2aa9fc6331b6d7d36af07827a887ba081c31e121d0c55c78eefd6909b745b537499b3d51f8246f394f011bacecc6e3347ba84d929f6729462dc"
arquivo_escolhido = input('DIGITE O ARQUIVO:\n')
diretorio = "file/"
caminho_arquivo = os.path.join(diretorio, arquivo_escolhido)

with open(diretorio + arquivo_escolhido, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    # Verificando no conteúdo lido
if verification in linhas[-1]:
    print("ARQUIVO VALIDO")
    if linhas:  # Se a lista não estiver vazia
        linhas.pop()  # Remove a última linha
        with open(diretorio + arquivo_escolhido, 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(linhas) #ELE ADICIONA O CONTEUDO DE VOLTA AO ARQUIVO, REESCREVE!
else:
    os.remove(os.path.join(caminho_arquivo))
        
with open("file/"+arquivo_escolhido, "r", encoding="utf-8") as arquivo:
    arquivo.readline().strip()  # Lê e ignora a primeira linha, se necessário
    for linha in arquivo:
        linha = linha.strip()  # Remove espaços em branco ao redor da linha
        if not linha:  # Verifica se a linha está vazia
            votoslimpos.append(0)  # Adiciona 0 se a linha estiver vazia
        else:
            voto = Descryptrography2(linha)
            if voto is not None:  # Verifica se o voto não é None
                votoslimpos.append(voto)  # Adiciona à lista se não for None
            
Type = int(input('DIGITE O TIPO DE ELEIÇÃO: \n'))
if Type == 1:
    contador = 0 
    while True:
        for i in votoslimpos:
            if contador == 0:
                FederalDeputy.append(i)
                contador += 1
            elif contador == 1:
                StateDeputy.append(i)
                contador += 1
            elif contador == 2:
                Senator.append(i)
                contador += 1
            elif contador == 3:
                Governor.append(i)
                contador += 1
            elif contador == 4:
                President.append(i)
                contador = 0
        break
    print("=========================================================================================================")
    # Inicializa a contagem de votos para os candidatos aos DEPUTADOS
    
    FederalDeputy_vote_count = {candidate[2]: 0 for candidate in federalDeputy}  # Chave: número do candidato, Valor: contagem
    StateDeputy_vote_count = {candidate[2]: 0 for candidate in stateDeputy}  # Chave: número do candidato, Valor: contagem
    Senator_vote_count = {candidate[2]: 0 for candidate in senator}  # Chave: número do candidato, Valor: contagem
    Governor_vote_count = {candidate[2]: 0 for candidate in governor}  # Chave: número do candidato, Valor: contagem
    President_vote_count = {candidate[2]: 0 for candidate in president}  # Chave: número do candidato, Valor: contagem
    total_votos_validos = []
    total_votos_branco = 0
    total_votos_nulos = []

    for i in FederalDeputy:
        if i != 0:
            total_votos_validos.append(i)
        elif i == 0:
            total_votos_branco += 1
    total_votos_sessão = total_votos_branco + len(total_votos_validos) + len(total_votos_nulos)
    # Percorre a lista de votos e conta os votos para os candidatos a DEPUTADO FEDERAL
    for vote in total_votos_validos:
        for candidate in federalDeputy:
            if vote == candidate[2]:  # Verifica se o voto corresponde ao número do candidato
                FederalDeputy_vote_count[candidate[2]] += 1  # Incrementa a contagem do candidato correspondente
                break  # Para de verificar após encontrar uma correspondência
        if vote != candidate[2]:
            total_votos_nulos.append(vote)
            
            
    for voto_nulo in total_votos_nulos:
        while voto_nulo in total_votos_validos:  # Enquanto o voto nulo estiver na lista de válidos
            total_votos_validos.remove(voto_nulo)
            
    total_votos = len(total_votos_validos)

    # Exibe os resultados da contagem de votos para DEPUTADO FEDERAL, incluindo porcentagens
    print("Votos para DEPUTADO FEDERAL:")
    candidato_mais_votado = None
    max_votos = 0

    for candidate in federalDeputy:
        partido = [candidate[1]]
        votos = FederalDeputy_vote_count[candidate[2]]
        porcentagem = (votos / total_votos * 100) if total_votos > 0 else 0  # Calcula a porcentagem
        print(f"Candidato: {candidate[0]}, {partido[0]}, Votos: {votos}, Porcentagem: {porcentagem:.2f}%")
        
        # Verifica se este candidato tem o maior número de votos
        if votos > max_votos:
            max_votos = votos
            candidato_mais_votado = candidate[0]
            
    # Exibe o total de votos e o candidato que recebeu mais votos
    print(f"\nTotal de Votos da Sessão: {total_votos_sessão}")
    print(f"Candidato mais votado: {candidato_mais_votado} com {max_votos} votos.")
    print(f"VOTOS VALIDOS DA SESSÃO:{len(total_votos_validos)}")
    print(f"TOTAL DE VOTOS EM BRANCO: {total_votos_branco}")
    print(f"TOTAL DE VOTOS NULOS: {len(total_votos_nulos)}")

    print("=========================================================================================================")
    total_votos_validos = []
    total_votos_branco = 0
    total_votos_nulos = []

    for i in StateDeputy:
        if i != 0:
            total_votos_validos.append(i)
        elif i == 0:
            total_votos_branco += 1
    total_votos_sessão = total_votos_branco + len(total_votos_validos) + len(total_votos_nulos)
    # Percorre a lista de votos e conta os votos para os candidatos a DEPUTADO ESTADUAL
    for vote in total_votos_validos:
        for candidate in stateDeputy:
            if vote == candidate[2]:  # Verifica se o voto corresponde ao número do candidato
                StateDeputy_vote_count[candidate[2]] += 1  # Incrementa a contagem do candidato correspondente
                break  # Para de verificar após encontrar uma correspondência
        if vote != candidate[2]:
            total_votos_nulos.append(vote)
            
            
    for voto_nulo in total_votos_nulos:
        while voto_nulo in total_votos_validos:  # Enquanto o voto nulo estiver na lista de válidos
            total_votos_validos.remove(voto_nulo)
            
    total_votos = len(total_votos_validos)

    # Exibe os resultados da contagem de votos para DEPUTADO ESTADUAL, incluindo porcentagens
    print("Votos para DEPUTADO ESTADUAL:")
    candidato_mais_votado = None
    max_votos = 0

    for candidate in stateDeputy:
        partido = [candidate[1]]
        votos = StateDeputy_vote_count[candidate[2]]
        porcentagem = (votos / total_votos * 100) if total_votos > 0 else 0  # Calcula a porcentagem
        print(f"Candidato: {candidate[0]}, {partido[0]}, Votos: {votos}, Porcentagem: {porcentagem:.2f}%")
        
        # Verifica se este candidato tem o maior número de votos
        if votos > max_votos:
            max_votos = votos
            candidato_mais_votado = candidate[0]
            
    # Exibe o total de votos e o candidato que recebeu mais votos
    print(f"\nTotal de Votos da Sessão: {total_votos_sessão}")
    print(f"Candidato mais votado: {candidato_mais_votado} com {max_votos} votos.")
    print(f"VOTOS VALIDOS DA SESSÃO:{len(total_votos_validos)}")
    print(f"TOTAL DE VOTOS EM BRANCO: {total_votos_branco}")
    print(f"TOTAL DE VOTOS NULOS: {len(total_votos_nulos)}")
    
    print("=========================================================================================================")
    total_votos_validos = []
    total_votos_branco = 0
    total_votos_nulos = []

    for i in Senator:
        if i != 0:
            total_votos_validos.append(i)
        elif i == 0:
            total_votos_branco += 1
    total_votos_sessão = total_votos_branco + len(total_votos_validos) + len(total_votos_nulos)
    # Percorre a lista de votos e conta os votos para os candidatos a SENADOR
    for vote in total_votos_validos:
        for candidate in senator:
            if vote == candidate[2]:  # Verifica se o voto corresponde ao número do candidato
                Senator_vote_count[candidate[2]] += 1  # Incrementa a contagem do candidato correspondente
                break  # Para de verificar após encontrar uma correspondência
        if vote != candidate[2]:
            total_votos_nulos.append(vote)
            
            
    for voto_nulo in total_votos_nulos:
        while voto_nulo in total_votos_validos:  # Enquanto o voto nulo estiver na lista de válidos
            total_votos_validos.remove(voto_nulo)
            
    total_votos = len(total_votos_validos)

    # Exibe os resultados da contagem de votos para SENADOR, incluindo porcentagens
    print("Votos para SENADOR:")
    candidato_mais_votado = None
    max_votos = 0

    for candidate in senator:
        partido = [candidate[1]]
        votos = Senator_vote_count[candidate[2]]
        porcentagem = (votos / total_votos * 100) if total_votos > 0 else 0  # Calcula a porcentagem
        print(f"Candidato: {candidate[0]}, {partido[0]}, Votos: {votos}, Porcentagem: {porcentagem:.2f}%")
        
        # Verifica se este candidato tem o maior número de votos
        if votos > max_votos:
            max_votos = votos
            candidato_mais_votado = candidate[0]
            
    # Exibe o total de votos e o candidato que recebeu mais votos
    print(f"\nTotal de Votos da Sessão: {total_votos_sessão}")
    print(f"Candidato mais votado: {candidato_mais_votado} com {max_votos} votos.")
    print(f"VOTOS VALIDOS DA SESSÃO:{len(total_votos_validos)}")
    print(f"TOTAL DE VOTOS EM BRANCO: {total_votos_branco}")
    print(f"TOTAL DE VOTOS NULOS: {len(total_votos_nulos)}")
    
    print("=========================================================================================================")
    
    total_votos_validos = []
    total_votos_branco = 0
    total_votos_nulos = []
    for i in Governor:
        if i != 0:
            total_votos_validos.append(i)
        elif i == 0:
            total_votos_branco += 1
    total_votos_sessão = total_votos_branco + len(total_votos_validos) + len(total_votos_nulos) 
    # Percorre a lista de votos e conta os votos para os candidatos a GOVERNADOR
    for vote in total_votos_validos:
        for candidate in governor:
            if vote == candidate[2]:  # Verifica se o voto corresponde ao número do candidato
                Governor_vote_count[candidate[2]] += 1  # Incrementa a contagem do candidato correspondente
                break  # Para de verificar após encontrar uma correspondência
        if vote != candidate[2]:
            total_votos_nulos.append(vote)
            
            
    for voto_nulo in total_votos_nulos:
        while voto_nulo in total_votos_validos:  # Enquanto o voto nulo estiver na lista de válidos
            total_votos_validos.remove(voto_nulo)
            
    total_votos = len(total_votos_validos)

    # Exibe os resultados da contagem de votos para GOVERNADOR, incluindo porcentagens
    print("Votos para GOVERNADOR:")
    candidato_mais_votado = None
    max_votos = 0

    for candidate in governor:
        partido = [candidate[1]]
        votos = Governor_vote_count[candidate[2]]
        porcentagem = (votos / total_votos * 100) if total_votos > 0 else 0  # Calcula a porcentagem
        print(f"Candidato: {candidate[0]}, {partido[0]}, Votos: {votos}, Porcentagem: {porcentagem:.2f}%")
        
        # Verifica se este candidato tem o maior número de votos
        if votos > max_votos:
            max_votos = votos
            candidato_mais_votado = candidate[0]
            
    # Exibe o total de votos e o candidato que recebeu mais votos
    print(f"\nTotal de Votos da Sessão: {total_votos_sessão}")
    print(f"Candidato mais votado: {candidato_mais_votado} com {max_votos} votos.")
    print(f"VOTOS VALIDOS DA SESSÃO:{len(total_votos_validos)}")
    print(f"TOTAL DE VOTOS EM BRANCO: {total_votos_branco}")
    print(f"TOTAL DE VOTOS NULOS: {len(total_votos_nulos)}")
    
    print("=========================================================================================================")
    
    total_votos_validos = []
    total_votos_branco = 0
    total_votos_nulos = []
    for i in President:
        if i != 0:
            total_votos_validos.append(i)
        elif i == 0:
            total_votos_branco += 1
    total_votos_sessão = total_votos_branco + len(total_votos_validos) + len(total_votos_nulos)       
    # Percorre a lista de votos e conta os votos para os candidatos a PRESIDENTE
    for vote in total_votos_validos:
        for candidate in president:
            if vote == candidate[2]:  # Verifica se o voto corresponde ao número do candidato
                President_vote_count[candidate[2]] += 1  # Incrementa a contagem do candidato correspondente
                break  # Para de verificar após encontrar uma correspondência
        if vote != candidate[2]:
            total_votos_nulos.append(vote)
            
            
    for voto_nulo in total_votos_nulos:
        while voto_nulo in total_votos_validos:  # Enquanto o voto nulo estiver na lista de válidos
            total_votos_validos.remove(voto_nulo)
            
    total_votos = len(total_votos_validos)

    # Exibe os resultados da contagem de votos para PRESIDENTE, incluindo porcentagens
    print("Votos para PRESIDENTE:")
    candidato_mais_votado = None
    max_votos = 0

    for candidate in president:
        partido = [candidate[1]]
        votos = President_vote_count[candidate[2]]
        porcentagem = (votos / total_votos * 100) if total_votos > 0 else 0  # Calcula a porcentagem
        print(f"Candidato: {candidate[0]}, {partido[0]}, Votos: {votos}, Porcentagem: {porcentagem:.2f}%")
        
        # Verifica se este candidato tem o maior número de votos
        if votos > max_votos:
            max_votos = votos
            candidato_mais_votado = candidate[0]
            
    # Exibe o total de votos e o candidato que recebeu mais votos
    print(f"\nTotal de Votos da Sessão: {total_votos_sessão}")
    print(f"Candidato mais votado: {candidato_mais_votado} com {max_votos} votos.")
    print(f"VOTOS VALIDOS DA SESSÃO:{len(total_votos_validos)}")
    print(f"TOTAL DE VOTOS EM BRANCO: {total_votos_branco}")
    print(f"TOTAL DE VOTOS NULOS: {len(total_votos_nulos)}")
    
elif Type == 2:
    contador = 0
    while True:
        for i in votoslimpos:
            if contador == 0:
                Councilman.append(i)
                contador += 1
            elif contador == 1:
                Mayor.append(i)
                contador = 0
        break
    #QUANTIDADE DE VOTOS
    print("VOTO VEREADOR:",Councilman)
    print("VOTO PREFEITO:", Mayor)
    
    # Inicializa a contagem de votos para os candidatos a VEREADOR
    
    Mayor_vote_count = {candidate[2]: 0 for candidate in mayor}  # Chave: número do candidato, Valor: contagem
    Councilman_vote_count = {candidate[2]: 0 for candidate in councilman}  # Chave: número do candidato, Valor: contagem
    total_votos_validos = []
    total_votos_branco = 0
    total_votos_nulos = []
    
    # Total de votos válidos
    
    print("========================================================================================================================")
    
    for i in Councilman:
        if i != 0:
            total_votos_validos.append(i)
        elif i == 0:
            total_votos_branco += 1
    total_votos_sessão = total_votos_branco + len(total_votos_validos) + len(total_votos_nulos)
    
    # Percorre a lista de votos e conta os votos para os candidatos a VEREADOR
    for vote in total_votos_validos:
        for candidate in councilman:
            if vote == candidate[2]:  # Verifica se o voto corresponde ao número do candidato
                Councilman_vote_count[candidate[2]] += 1  # Incrementa a contagem do candidato correspondente
                break  # Para de verificar após encontrar uma correspondência
        if vote != candidate[2]:
            total_votos_nulos.append(vote)
            
            
    for voto_nulo in total_votos_nulos:
        while voto_nulo in total_votos_validos:  # Enquanto o voto nulo estiver na lista de válidos
            total_votos_validos.remove(voto_nulo)
            
    total_votos = len(total_votos_validos)

    # Exibe os resultados da contagem de votos para VEREADOR, incluindo porcentagens
    print("Votos para VEREADOR:")
    candidato_mais_votado = None
    max_votos = 0

    for candidate in councilman:
        votos = Councilman_vote_count[candidate[2]]
        porcentagem = (votos / total_votos * 100) if total_votos > 0 else 0  # Calcula a porcentagem
        print(f"Candidato: {candidate[0]}, Votos: {votos}, Porcentagem: {porcentagem:.2f}%")
        
        # Verifica se este candidato tem o maior número de votos
        if votos > max_votos:
            max_votos = votos
            candidato_mais_votado = candidate[0]
            
    # Exibe o total de votos e o candidato que recebeu mais votos
    print(f"\nTotal de Votos da Sessão: {total_votos_sessão}")
    print(f"Candidato mais votado: {candidato_mais_votado} com {max_votos} votos.")
    print(f"VOTOS VALIDOS DA SESSÃO:{len(total_votos_validos)}")
    print(f"TOTAL DE VOTOS EM BRANCO: {total_votos_branco}")
    print(f"TOTAL DE VOTOS NULOS: {len(total_votos_nulos)}")

    print("========================================================================================================================")

    total_votos_validos = []
    total_votos_branco = 0
    total_votos_nulos = []
    
    for i in Mayor:
        if i != 0:
            total_votos_validos.append(i)
        elif i == 0:
            total_votos_branco += 1
    total_votos_sessão = total_votos_branco + len(total_votos_validos) + len(total_votos_nulos)
    
    # Percorre a lista de votos e conta os votos para os candidatos a prefeito
    for vote in total_votos_validos:
        for candidate in mayor:
            if vote == candidate[2]:  # Verifica se o voto corresponde ao número do candidato
                Mayor_vote_count[candidate[2]] += 1  # Incrementa a contagem do candidato correspondente
                break  # Para de verificar após encontrar uma correspondência
        if vote != candidate[2]:
            total_votos_nulos.append(vote)
            
            
    for voto_nulo in total_votos_nulos:
        while voto_nulo in total_votos_validos:  # Enquanto o voto nulo estiver na lista de válidos
            total_votos_validos.remove(voto_nulo)
            
    total_votos = len(total_votos_validos)

    # Exibe os resultados da contagem de votos para prefeitos, incluindo porcentagens
    print("Votos para Prefeitos:")
    candidato_mais_votado = None
    max_votos = 0

    for candidate in mayor:
        votos = Mayor_vote_count[candidate[2]]
        porcentagem = (votos / total_votos * 100) if total_votos > 0 else 0  # Calcula a porcentagem
        print(f"Candidato: {candidate[0]}, Votos: {votos}, Porcentagem: {porcentagem:.2f}%")
        
        # Verifica se este candidato tem o maior número de votos
        if votos > max_votos:
            max_votos = votos
            candidato_mais_votado = candidate[0]
            
    # Exibe o total de votos e o candidato que recebeu mais votos
    print(f"\nTotal de Votos da Sessão: {total_votos_sessão}")
    print(f"Candidato mais votado: {candidato_mais_votado} com {max_votos} votos.")
    print(f"VOTOS VALIDOS DA SESSÃO:{len(total_votos_validos)}")
    print(f"TOTAL DE VOTOS EM BRANCO: {total_votos_branco}")
    print(f"TOTAL DE VOTOS NULOS: {len(total_votos_nulos)}")