import datetime

def depositar(saldo, extrato):
    print("\n### VOCÊ ESTÁ EM DEPÓSITO ###")
    valor = float(input("\nInforme o valor do depósito: "))
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f} => Realizado em: {datetime.datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}\n"
        print("\nDepósito realizado com sucesso!\n")
        print(f"Seu saldo é de: R$ {saldo:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    print("\n### VOCÊ ESTÁ EM SAQUE ###")
    print(f"Seu saldo é: R$ {saldo:.2f}")

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.\n")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f} => Realizado em: {datetime.datetime.now().strftime('%d/%m/%Y - %H:%M:%S')}\n"
        numero_saques += 1
        print(f"Seu saldo depois do saque é: R$ {saldo:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

### BEM-VINDO AO NOSSO BANCO ###
menu = """
### POR FAVOR, SELECIONE UMA DAS OPÇÕES ABAIXO ###

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """.upper()

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor_saque, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
    
    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        print("### OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS ###")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")