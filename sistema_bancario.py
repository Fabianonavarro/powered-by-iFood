from datetime import date

# Constantes
LIMITE = 500
LIMITE_SAQUES = 3

def exibir_mensagem_bem_vindo():
    atual = date.today().year
    print("\n" + "="*50)
    print(f"       Sistema Bancário - Ano {atual}")
    print("="*50 + "\n")

def exibir_menu():
    print("\n" + "="*40)
    print("                MENU PRINCIPAL")
    print("="*40)
    print("Escolha uma das opções abaixo:")
    print(" 1 - Depositar")
    print(" 2 - Sacar")
    print(" 3 - Extrato")
    print(" 4 - Saldo")
    print(" 0 - Sair")
    print("="*40)
    return input("Digite sua opção: ")

def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("O valor deve ser positivo. Tente novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

def realizar_deposito(saldo, extrato):
    valor = obter_valor("Informe o valor do depósito: R$ ")
    confirmar = input(f"Você deseja confirmar o depósito de R$ {valor:.2f}? (s/n): ").strip().lower()
    if confirmar == 's':
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito realizado com sucesso! Valor: R$ {valor:.2f}")
    else:
        print("Depósito não realizado.")
    return saldo, extrato

def realizar_saque(saldo, extrato, limite, numero_saques):
    valor = obter_valor("Informe o valor do saque: R$ ")
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque realizado com sucesso! Confira o valor: R$ {valor:.2f}")
    return saldo, extrato, numero_saques

def exibir_extrato(extrato, saldo):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def mostrar_saldo(saldo):
    print(f"\nSaldo atual: R$ {saldo:.2f}")

def main():
    saldo = 0
    extrato = ""
    numero_saques = 0

    exibir_mensagem_bem_vindo()

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            saldo, extrato = realizar_deposito(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, numero_saques = realizar_saque(saldo, extrato, LIMITE, numero_saques)
        elif opcao == "3":
            exibir_extrato(extrato, saldo)
        elif opcao == "4":
            mostrar_saldo(saldo)
        elif opcao == "0":
            print("\n" + "="*40)
            print("               SAINDO DO SISTEMA")
            print("="*40)
            print("Obrigado por usar o sistema bancário.")
            print("="*40)
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
