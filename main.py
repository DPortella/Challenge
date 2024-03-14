#Parte principal e inicial do programa

import os.path
import rosto_em_imagem
import texto_em_docs
import texto_em_xlsx
import fitz
import openpyxl
from docx import Document

for path, directories, files in os.walk(r'C:\Users\Nick\Desktop'): #Caminho de arquivos a ser analisado
     for file in files:
          if file.endswith(".PNG") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"): #Definindo os tipos de arquivos de imagens
               caminho = os.path.join(path, file)  # Apontando o caminho do arquivo para uma variável
               #Chamar módulo
               rosto_em_imagem.imagem(caminho, file, path)
          elif file.endswith(".pdf"): #Definindo os tipos de arquivos de texto
               caminho = os.path.join(path, file)
               doc = fitz.open(caminho)
               text = ""
               for page in doc:
                   text+=page.get_text()
               texto_em_docs.texto(caminho, file, path, text)
          elif file.endswith(".docx") or file.endswith(".doc"):
               caminho = os.path.join(path, file)
               doc = Document(caminho)
               text = '\n'.join([p.text for p in doc.paragraphs])
               texto_em_docs.texto(caminho, file, path, text)
          elif file.endswith(".xlsx"):
               caminho = os.path.join(path, file)
               workbook = openpyxl.load_workbook(path)
               texto = ""
               for sheet in workbook:
                    for row in sheet.iter_rows():
                         for cell in row:
                              texto += str(cell.value) + "\n"
               texto_em_xlsx.texto(caminho, file, path, texto)