import os
import random

print ("Arquivos no diretório atual: ", os.listdir())

os.makedirs("Projetos", exist_ok=True)

nome_arquivo = f"arquivo_{random.randint(1, 99)}.txt"
caminho_arquivo = os.path.join("Projetos", nome_arquivo)

conteudo = f"Hello World"

with open(caminho_arquivo, 'w') as f:
    f.write("Hellooooo")
