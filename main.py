#Parte principal e inicial do programa
import tkinter as tk
import os.path
import rosto_em_imagem
import texto_em_docs
import texto_em_xlsx
import fitz
import openpyxl
from docx import Document
from tkinter import *
from tkinter import PhotoImage as pht
from tkinter import messagebox




#Montando GUI
class MinhaGUI:
    def __init__(self):
        # Criamos a janela principal
        self.janela_principal = Tk()
        self.janela_principal.iconbitmap("ico2.ico")
        self.janela_principal.maxsize(width=580, height=200)
        self.janela_principal.title('GetSens3')

        #Criando Label do logo
        self.img = pht(file=r"logooo.png")
        self.label1 = tk.Label(self.janela_principal, image=self.img)
        self.label1.pack(side='bottom')

        # Criando os frames
        self.frame_cima = Frame(self.janela_principal)
        self.frame_baixo = Frame(self.janela_principal)


        # Criando label e botões do frame de cima
        self.label = Label(self.frame_cima, text='Indique o caminho que deve ser analisado:')

        # Criando o widget de entrada
        self.entrada = Entry(self.frame_cima, width=40)

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

               elif file.endswith(".xlsx"):
                    caminho = os.path.join(path, file)
                    workbook = openpyxl.load_workbook(caminho)
                    texto = ""
                    for sheet in workbook:
                        for row in sheet.iter_rows():
                            for cell in row:
                                texto += str(cell.value) + "\n"
                    texto_em_xlsx.texto(caminho, file, path, texto)

        messagebox.showinfo("GetSens3", "Análise feita com sucesso!")

gui = MinhaGUI()