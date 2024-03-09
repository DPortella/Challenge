import csv
import json

#Função para adicionar CNPJ ao csv
def cnpj_to_file(caminho, cnpj):
     lst1 = ["PATH", "CNPJ"]
     lst2 = [caminho, cnpj]
     with open('info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i]])



#Função para adicionar CPF ao csv
def cpf_to_file(caminho, cpf_validos):
     lst1 = ["PATH", "CPF"]
     lst2 = [caminho, cpf_validos]
     with open('info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i]])

def rg_to_file(caminho, rg):
     lst1 = ["PATH", "RG"]
     lst2 = [caminho, rg]
     with open('info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i]])

def datas_to_file(caminho, datas):
     lst1 = ["PATH", "DATA"]
     lst2 = [caminho, datas]
     with open('info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i]])

def tel_to_file(caminho, tel):
     lst1 = ["PATH", "TELEFONE"]
     lst2 = [caminho, tel]
     with open('info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i]])

'''def json1(image, cnpj, cpf):
     data = {
          "image": image,
          "CNPJ": cnpj,
          "CPF": cpf
     }
     with open('info.json', 'a') as file:
          json.dump(data, file)

def json2(image):
     data = {
          "image": image,
     }
     with open('info.json', 'a') as file:
          json.dump(data, file)'''

#Função que adiciona as imagens com rostos ao CSV
def image_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open('info.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "Foto com rosto detectado"])
