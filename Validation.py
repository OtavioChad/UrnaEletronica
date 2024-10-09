import os
from hashlib import sha3_512
from datetime import datetime
data_hora_formatada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(data_hora_formatada)

#ARQUIVO 82731642-736
validation = "18788c3cbf5a8ee553b33ed767682a8e2285bb63de9726a1afb3f3f1e12c20638ebbc315d32f9752c332ce05e2aaf955d6cb9a51b866d1b9b5cfdcdcfaccf933"
#SENHA = "5a485b074cc436d5831224346085f2a622f54e6ff4fc6d5af08d46d3b4917a51c2c0850f23299170a52f2fb85b37852cc69566a04f064cdd769a98689907499e"
Key = "e2560249975fd3bbf13c922abd2ef448884594a55bfb5276bd398557fa654627ce1aa065a942ce67bb9b2f3c3e6f2dde87156998fb865ee5c214d45f9c878d72"
Arquivo_valido = []

def hashCheck():
    # Diretório onde os arquivos estão localizados
    diretorio = 'file'
    
    # Verificar se o diretório existe
    if not os.path.exists(diretorio):
        print(f"O diretório {diretorio} não existe.")
        return
    arquivos = os.listdir(diretorio)

    # Verificar se há arquivos no diretório
    if not arquivos:
        print("Nenhum arquivo encontrado no diretório.")
        return

    # Escolher um arquivo aleatório
    arquivo_escolhido = input("ESCOLHA UM ARQUIVO:\n")
    try:
        with open(os.path.join(diretorio, arquivo_escolhido), "r", encoding="utf-8") as arquivo:
            hashfied = (arquivo.readline()).strip()
            hashfied = sha3_512(hashfied.encode()).hexdigest()
    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
        return
    
    if  hashfied == validation:
        print("Arquivo escolhido é válido para apuração!")
        tentativas = 3
        while tentativas > 0:
            print(f"VOCê TEM {tentativas} PARA ACESSAR O ARQUIVO.")
            senha = input("DIGITE A SENHA DE SEGURANÇA:\n")
            if sha3_512(senha.encode()).hexdigest() == Key:
                Arquivo_valido.append(arquivo_escolhido)
                print("Senha válida!")
                with open(f"file/"+arquivo_escolhido, 'a') as arquivo:
                    arquivo.write("607e0cfae779b2aa9fc6331b6d7d36af07827a887ba081c31e121d0c55c78eefd6909b745b537499b3d51f8246f394f011bacecc6e3347ba84d929f6729462dc")
                for arquivo in arquivos:
                    if arquivo != arquivo_escolhido:
                        os.remove(os.path.join(diretorio, arquivo))
                break
                
                        
            else:
                tentativas -= 1
                print(f"SENHA INVALIDA, VOCê TEM {tentativas} PARA ACESSAR O ARQUIVO.")
                if tentativas == 0:
                    for arquivo in arquivos:
                        try:
                            os.remove(os.path.join(diretorio, arquivo))
                            print(f"Arquivo removido: {arquivo}")
                        except Exception as e:
                            print(f"Erro ao remover o arquivo {arquivo}: {e}")
                
                             
    else:
        for arquivo in arquivos:
            try:
                os.remove(os.path.join(diretorio, arquivo))
                print(f"Arquivo removido: {arquivo}")
            except Exception as e:
                print(f"Erro ao remover o arquivo {arquivo}: {e}")

hashCheck()
