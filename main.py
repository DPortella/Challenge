import os.path
import rosto_em_imagem

for path, directories, files in os.walk(r'C:\Users\marci\Downloads\teste'): #Caminho de arquivos a ser analisado
     for file in files:
          if file.endswith(".PNG") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"): #Definindo os tipos de arquivos de imagens
               caminho = os.path.join(path, file)  # Apontando o caminho do arquivo para uma variável
               rosto_em_imagem.imagem(caminho, file, path)