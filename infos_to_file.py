import csv
import os.path

username = os.environ['USERPROFILE']


#Contagem de tipos de arquivos encontrados
def count_data_types(data_type, file_path=fr'{username}\Documents\Data_result.csv'):
    count = 0
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 3 and data_type in row[2]: 
                    count += 1
    except FileNotFoundError:
        print(f"Arquivo '{file_path}' não encontrado. Não foi possivel executar.")
    return count


def top_paths_info(file_path, n=10):
    paths_info = {}
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:  # Check if row has at least 2 elements
                path = row[1]
                if path in paths_info:
                    paths_info[path] += 1
                else:
                    paths_info[path] = 1
    sorted_paths_info = sorted(paths_info.items(), key=lambda x: x[1], reverse=True)
    return sorted_paths_info[:n]



#Função para adicionar CNPJ ao csv
def cnpj_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Data_result.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "CNPJ encontrado"])
               global global_cnpj_count 
               global_cnpj_count =+1

               

#Função para adicionar nomes ao csv
def nome1_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Data_result.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "Nome encontrado"])
               global global_cnpj_count  # Access the global variable (assuming it's defined elsewhere)
               global_cnpj_count += 1
               

#Função para adicionar CPF ao csv
def cpf_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Data_result.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "CPF encontrado"])
               

def rg_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Data_result.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "RG encontrado"])
               

def datas_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Data_result.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "Data encontrada"])
               

def tel_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Data_result.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "Telefone encontrado"])

#Função que adiciona as imagens com rostos ao CSV
def image_to_file(caminho):
     lst1 = ["PATH"]
     lst2 = [caminho]
     with open(fr'{username}\Documents\Data_result.csv', 'a') as file:
          writer = csv.writer(file, delimiter=",")
          for i in range(len(lst1)):
               writer.writerow([lst1[i], lst2[i], "Foto com rosto detectado"])


def count_CNPJ():
    return count_data_types("CNPJ")

def count_nome():
    return count_data_types("Nome")

def count_cpf():
    return count_data_types("CPF")

def count_rg():
    return count_data_types("RG")

def count_datas():
    return count_data_types("Data")

def count_tel():
    return count_data_types("Telefone")

def count_image():
    return count_data_types("Foto")


