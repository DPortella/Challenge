import csv
import os.path


username = os.environ['USERPROFILE']

#Função para adicionar CNPJ ao csv
def cnpj_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "CNPJ encontrado"])

#Função para adicionar nomes ao csv
def nome1_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "Nome encontrado"])

#Função para adicionar CPF ao csv
def cpf_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "CPF encontrado"])

def rg_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "RG encontrado"])

def datas_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "Data encontrada"])

def tel_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "Telefone encontrado"])

#Função que adiciona as imagens com rostos ao CSV
def image_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "Foto com rosto detectado"])
