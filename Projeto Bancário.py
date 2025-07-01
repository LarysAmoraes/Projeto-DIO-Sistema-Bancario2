# sistema_bancario.py

def menu():
    return input("""
    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair

    -> """).upper().strip()

def depositar(saldo, extrato):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    except ValueError:
        print("\n@@@ Operação falhou! Valor inválido. @@@")
    
    return saldo, extrato

def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    try:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif excedeu_limite:
            print(f"\n@@@ Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}. @@@")
        elif excedeu_saques:
            print(f"\n@@@ Operação falhou! Número máximo de {limite_saques} saques excedido. @@@")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    except ValueError:
        print("\n@@@ Operação falhou! Valor inválido. @@@")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = menu()

        if opcao == "D":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "S":
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "Q":
            print("\n=== Saindo do sistema. Até mais! ===")
            break
        else:
            print("\n@@@ Operação inválida. Por favor, selecione novamente a operação desejada. @@@")

if __name__ == "__main__":
    main()