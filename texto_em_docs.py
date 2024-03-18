import valid_cpf
import infos_to_file
import re
import pandas as pd

def texto(caminho, file, path, text):
    
    base_de_dados_nomes = pd.read_csv('Arquivos/ibgeNomes.csv', encoding='utf-8', sep=';')
    nomes_ibge = '|'.join(base_de_dados_nomes['nome'])

    pattern = r'[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2}'  # Regex CNPJ
    pattern1 = r'\b(\d{3}\.?\d{3}\.?\d{3}-?\d{2})\b'  # Regex CPF
    pattern2 = r'\b\d{2}\.?\d{3}\.?\d{3}-?\d\b'  # Regex RG
    pattern3 = r'(\d{1,2}[-./]\d{1,2}[-./]\d{2,4})'  # Regex datas
    pattern4 = r'(?:\+\d{2}\s?)?(\(\d{2}\)\s?)?\d{4,5}-\d{4}$'  # Regex telefone

    nome = re.findall(r'\b(?!de\s+)(?!da\s+)(?!este\b)(?!dos\s+)(?!dos$)(?!do\s+)(?!das\s+)(' + nomes_ibge.lower() + r')\b', text, flags=re.IGNORECASE)


    #nome = re.findall(r'\b(?!de\s+)(?!da\s+)(?!dos\s+)(?!dos$)(' + nomes_ibge.lower() + r')\b', text, flags=re.IGNORECASE)
    #nome = re.findall(r'\b(?!(de|da|dos|do|das)(\s+|$))(' + nomes_ibge.lower() + r')\b', text, flags=re.IGNORECASE) 
    #nome = re.findall(r'\b(?<!(de|da|dos)(\s+|$))(' + nomes_ibge.lower() + r')\b', text, flags=re.IGNORECASE)
    
    cnpj = re.findall(pattern, text)
    cpf_total = re.findall(pattern1, text)
    rg = re.findall(pattern2, text)
    datas = re.findall(pattern3, text)
    tel = re.findall(pattern4, text)

    
    if len(nome) != 0:

        nome = '\n'.join(nome)
        infos_to_file.nome1_to_file(caminho, nome)
        print(f"Primeiro nome encontrado em: {caminho}:\n{nome}")

    if len(cnpj) != 0:
        cnpj = '\n'.join(cnpj)
        infos_to_file.cnpj_to_file(caminho, cnpj)
        print(f"CNPJ encontrado em: {caminho}:\n{cnpj}")

    # Chamar função para validar CPF
    if len(cpf_total) != 0:
        valid_cpf.valida_cpf(caminho, cpf_total)

    if len(rg) != 0:
        rg = '\n'.join(rg)
        infos_to_file.rg_to_file(caminho, rg)
        print(f"RG encontrado em: {caminho}:\n{rg}")

    if len(datas) != 0:
        datas = '\n'.join(datas)
        infos_to_file.datas_to_file(caminho, datas)
        print(f"Datas encontradas em: {caminho}:\n{datas}")

    if len(tel) != 0:
        tel = '\n'.join(tel)
        infos_to_file.tel_to_file(caminho, tel)
        print(f"Telefone encontrado em: {caminho}:\n{tel}")