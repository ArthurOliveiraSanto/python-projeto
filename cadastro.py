import re
import random
import string

lista = []
id_counter = 1

def gerar_senha_criptografada(tamanho=12):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for _ in range(tamanho))

while True:
    print("1-Cadastrar 2-Mostrar")
    escolha = input(": ")
   
    if escolha == "1":
        tipo = input("Tipo (cliente/funcionario/vendedor): ")
        nome = input("Nome: ")
        email = input("Email: ")
       
        while True:
            cpf = input("CPF (formato: 999.999.999-99): ")
           
            padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
            if re.match(padrao_cpf, cpf):
                cpf_formatado = cpf.replace('.', '').replace('-', '')
                break
            else:
                print("Invalido! Use exatamente: 999.999.999-99")
                print("Exemplo: 123.456.789-00")
       
        senha = input("Senha: ")
        senha_criptografada = gerar_senha_criptografada()
       
        while True:
            telefone = input("Telefone (formato: (99) 9999-9999): ")
           
            padrao = r'^\(\d{2}\)\s\d{4,5}-\d{4}$'
            if re.match(padrao, telefone):
                ddd = telefone[1:3]  
                numero = telefone[6:].replace('-', '')
                telefone_formatado = f"ddd {ddd} telefone {numero}"
                break
            else:
                print("Formato inválido! Use exatamente: (DDD) XXXXX-XXXX")
                print("Exemplo: (41) 99829-2672")
       
        lista.append([id_counter, tipo, nome, email, cpf_formatado, senha, senha_criptografada, telefone_formatado])
        print(f"Cadastrado!")
        id_counter += 1  
       
    elif escolha == "2":
        print("Cadastros:")
        print("-" * 30)
        for item in lista:
            id_cadastro, tipo, nome, email, cpf, senha_real, senha_cripto, telefone = item
            print(f"id : {id_cadastro}")
            print(f"tipo : {tipo}")
            print(f"nome : {nome}")
            print(f"email : {email}")
            print(f"cpf : {cpf}")
            print(f"senha : {senha_cripto}")  
            print(f"telefone : {telefone}")
            print("-" * 30)
