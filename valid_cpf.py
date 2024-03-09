import infos_to_file

def valida_cpf(caminho, cpf_total):
    cpf_validos = []
    for numero_cpf in cpf_total:
        # Remove caracteres não numéricos do CPF
        cpf = ''.join(filter(str.isdigit, numero_cpf))

        # Verifica se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            return False

        # Calcula o primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = soma % 11
        if resto < 2:
            digito_verificador1 = 0
        else:
            digito_verificador1 = 11 - resto

        # Calcula o segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = soma % 11
        if resto < 2:
            digito_verificador2 = 0
        else:
            digito_verificador2 = 11 - resto

        # Verifica o segundo dígito verificador
        if int(cpf[9]) == digito_verificador1 and int(cpf[10]) == digito_verificador2:
            cpf_validos.append(cpf)
    cpf_validos = '\n'.join(cpf_validos)
    print("Cpf encontrado em: ",caminho, cpf_validos)
    infos_to_file.cpf_to_file(caminho, cpf_validos)