import os 
import random

# CRiar a pasta se não existir
os.makedirs("Projetos", exist_ok=True)

#Seleciona o caminho do Arquivo

for i in range(5):
    nome_arquivo = f"arquivo_{random.randint(1,99)}.txt"
    caminho_arquivo = os.path.join('Projetos', nome_arquivo)

    try:
        # Escreve dentro do arquivo novo
        with open(caminho_arquivo, 'w') as f:
            f.write("OI")
        print("Sucesso!!")
    except:
        print("Deu ruim!!")