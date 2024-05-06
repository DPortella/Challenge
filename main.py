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
from tkinter import Frame, Entry, Label, Button, Tk, PhotoImage
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




class MinhaGUI:
    def __init__(self):
        # Criamos a janela principal
        self.janela_principal = Tk()
        self.janela_principal.iconbitmap("ico2.ico")
        self.janela_principal.maxsize(width=580, height=200)
        self.janela_principal.title('GetSens3')

        #Criando Label do logo
        self.img = PhotoImage(file=r"logooo.png")
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
        self.botao_grafico = Button(self.frame_baixo, text='Abrir Gráfico', command=self.abrir_grafico)

        # Empacotando os botões no frame de baixo
        self.botao.pack(side='left')
        self.botao_sair.pack(side='left')
        self.botao_grafico.pack(side='left')

        # Empacotando os botões janela principal
        self.botao.pack()
        self.botao_sair.pack()

        # Empacotando os frames na janela principal
        self.frame_cima.pack()
        self.frame_baixo.pack()

    def exibe(self):
        # Função para ação do botão "Pesquisar"
        pass

    def abrir_grafico(self):
        # Função para ação do botão "Abrir Gráfico"
        x = [1, 2, 3, 4]
        y = [2, 3, 4, 3]

        # criando a "figura" para comportar os gráficos e formar nosso Dashboard
        Figura = plt.figure(figsize=(12, 6))
        Figura.suptitle('Harry Potter menino maravilhoso')

        # adicionando a primeira figura
        Figura.add_subplot(331)

        plot1 = plt.plot(x, y, label='dados ')
        plot1 = plt.title('número de arquivos com dados relevantes')

        plt.legend()

        # adicionando o segundo plot na figura
        Figura.add_subplot(332)
        # segundo gráfico teste
        cores = ['green', 'red', 'blue']
        plot2 = plt.bar(x, y, label='número de sugadinhas', color=cores)
        plot2 = plt.title('número de cpfs encontrados')

        plt.legend()

        # adicionando o 3 gráfico
        Figura.add_subplot(333)
        # terceiro gráfico teste
        plot3 = plt.plot(x, y)
        plot3 = plt.title('tipo de dado mais encontrado')

        plt.legend()

        # SEGUNDA LINHA DA FIGURA

        # adicionando o 4 gráfico
        Figura.add_subplot(334)
        # terceiro gráfico teste
        fatiax = [3, 2, 4]
        cores = ['green', 'red', 'blue']
        plot4 = plt.pie(fatiax, colors=cores)
        plot4 = plt.title('tipo de dado mais encontrado')

        plt.legend()

        # adicionando uma terceira figura
        Figura.add_subplot(335)
        valorx = [5, 7, 3, 9]
        valory = [1, 2, 3, 4]
        plot4 = plt.scatter(valorx, valory, label='cpf, tamanho peniano')

        plt.show()

        plt.close()  # Fecha a janela do Matplotlib após desenhar o gráfico

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
                                xl= []

                    texto_em_xlsx.texto(caminho, file, path, texto)

        messagebox.showinfo("GetSens3", "Análise feita com sucesso!")


if __name__ == "__main__":
    app = MinhaGUI()
    app.janela_principal.mainloop()
