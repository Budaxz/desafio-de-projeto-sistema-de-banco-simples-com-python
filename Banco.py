menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_saque = 500
extrato = ""

while True:

    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do Deposito: "))
        if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                print(f"Saldo atual: {saldo}")
        else:
             print("Valor de deposito insuficiente")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))
        if valor > saldo:
             print("Operação Falhou! Saldo insuficiente.")
        
        elif valor > limite_saque:
             print("Operação Falhou! Limite de saque por operação atingido")

        elif valor <= saldo:
             saldo -= valor
             extrato += f"Saque: R$ {valor:.2f}\n"
             print(f"Saque realizado, saldo atual: {saldo:.2f}")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "q":
         print("Encerrando...")
         break
    
    else:
         print("Comando invalido, selecione novamente o comando desejado.")
                