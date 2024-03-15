#Parte principal e inicial do programa

import os.path
import rosto_em_imagem
import texto_em_docs
import fitz
from docx import Document
from tkinter import *
from tkinter import messagebox

class MinhaGUI:
    def __init__(self):
        # Criamos a janela principal
        self.janela_principal = Tk()

        # Criando os frames
        self.frame_cima = Frame(self.janela_principal)
        self.frame_baixo = Frame(self.janela_principal)

        # Criando label e botões do frame de cima
        self.label = Label(self.frame_cima, text='Indique o caminho que deve ser analisado:')

        # Criando o widget de entrada
        self.entrada = Entry(self.frame_cima, width=30)

        # Empacotando label e entrada no frame de cima
        self.label.pack(side='left')
        self.entrada.pack(side='left')

        # Criando os botões, no frame de baixo
        self.botao = Button(self.frame_baixo, text='Pesquisar', command=self.exibe)
        self.botao_sair = Button(self.frame_baixo, text='Sair', command=self.janela_principal.quit)

        # Empacotando os botões no frame de baixo
        self.botao.pack(side='left')
        self.botao_sair.pack(side='left')

        # Empacotando os botões janela principal
        self.botao.pack()
        self.botao_sair.pack()

        # Empacotando os frames na janela principal
        self.frame_cima.pack()
        self.frame_baixo.pack()

        # Rodando
        mainloop()

    def exibe(self):
        for path, directories, files in os.walk(self.entrada.get()): #Caminho de arquivos a ser analisado
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

gui = MinhaGUI()