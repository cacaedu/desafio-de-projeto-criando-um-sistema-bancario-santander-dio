import datetime

print("### BEM-VINDO AO NOSSO BANCO ###")

menu = """
### POR FAVOR, SELECIONE UMA DAS OPÇÕES ABAIXO ###

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """.upper() # Para um visual mais claro e para exercitar o uso da função upper()

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower() # Para garantir que não haja problemas com case sensitive 

    if opcao == "d":
        print("### VOCÊ ESTÁ EM DEPÓSITO ###") # Avisa o cliente em qual operação ele está
        valor = float(input("\nInforme o valor do depósito: "))

        if valor > 0:
            saldo += valor
            # Mostra a data e o horário do depósito com formatação definida por mim
            extrato += f"Depósito: R$ {valor:.2f} => Realizado em: {datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}\n"
            print("\nDepósito realizado com sucesso!\n")
            print(f"Seu saldo é de: R$ {saldo:.2f}") 

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print("### VOCÊ ESTÁ EM SAQUE ###") # Avisa o cliente em qual operação ele está
        print(f"Seu saldo é: R$ {saldo:.2f}")

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.\n")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            # Mostra a data e o horário do depósito com formatação definida por mim
            extrato += f"Saque:    R$ {valor:.2f} => Realizado em: {datetime.datetime.now().strftime("%d/%m/%Y - %H:%M:%S")}\n"
            numero_saques += 1
            print(f"Seu saldo depois do saque é: R$ {saldo:.2f}")


        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        print("### OBRIGADO POR UTILIZAR NOSSOS SERVIÇOS ###") # Notifica o cliente que ele saiu do sistema com uma mensagem amigável e gentil
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
