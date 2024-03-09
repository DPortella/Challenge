import valid_cpf
import infos_to_file
from PIL import Image
import pytesseract
import re

def texto(caminho, file, path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(caminho)
    pattern = r'[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2}'  # Regex CNPJ
    pattern1 = r'\b(\d{3}\.?\d{3}\.?\d{3}-?\d{2})\b'  # Regex CPF
    pattern2 = r'\b\d{2}\.?\d{3}\.?\d{3}-?\d\b'  # Regex RG
    pattern3 = r'(\d{1,2}[-./]\d{1,2}[-./]\d{2,4})'  # Regex datas
    pattern4 = r'(?:\+\d{2}\s?)?(\(\d{2}\)\s?)?\d{4,5}-\d{4}$'  # Regex telefone
    cnpj = re.findall(pattern, text)
    cpf_total = re.findall(pattern1, text)
    rg = re.findall(pattern2, text)
    datas = re.findall(pattern3, text)
    tel = re.findall(pattern4, text)

    if len(cnpj) != 0:
        cnpj = '\n'.join(cnpj)
        infos_to_file.cnpj_to_file(caminho, cnpj)
        # json1(image, cnpj, cpf)
        print(f"CNPJ encontrado em: {caminho}:\n{cnpj}")
        # cv2.waitKey()  # Esperar input para a próxima imagem

    # Chamar função para validar CPF
    if len(cpf_total) != 0:
        valid_cpf.valida_cpf(caminho, cpf_total)

    if len(rg) != 0:
        rg = '\n'.join(rg)
        infos_to_file.rg_to_file(caminho, rg)
        # json1(image, cnpj, cpf)
        print(f"RG encontrado em: {caminho}:\n{rg}")
        # cv2.waitKey()  # Esperar input para a próxima imagem

    if len(datas) != 0:
        datas = '\n'.join(datas)
        infos_to_file.datas_to_file(caminho, datas)
        # json1(image, cnpj, cpf)
        print(f"Datas encontradas em: {caminho}:\n{datas}")
        # cv2.waitKey()  # Esperar input para a próxima imagem

    if len(tel) != 0:
        tel = '\n'.join(tel)
        infos_to_file.tel_to_file(caminho, tel)
        # json1(image, cnpj, cpf)
        print(f"Teefone encontrado em: {caminho}:\n{tel}")
        # cv2.waitKey()  # Esperar input para a próxima imagem