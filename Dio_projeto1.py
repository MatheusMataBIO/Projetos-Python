menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))  # importante pois ao informar o valor pode ser número decimal
        
        if valor > 0: # condição criada para que o valor não seja negativo
            
            saldo += valor # saldo tem que ser positivo
            
            extrato += f"Depósito: R$ {valor:.2f}\n" # informa no extrato o deposito feito na condicional que não pode ser número negativo. Sem espaço e com 2 casas decimais
        
        else:
            print("Operação falhou! O valor informado é inválido!") # condicional usada para caso coloque um valor negativo
        

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo # condição para verificar para saber se o valor excedeu o saldo
        
        excedeu_limite = valor > limite # condição para saber se excedeu o valor do limite
       
        excedeu_saques = numero_saques >= LIMITE_SAQUES # condição para verificar se excedeu o número de saques
       
        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! O número de saques foi excedido.")
        
        elif valor > 0:
            saldo -= valor # valor debitado da conta
            extrato += f"Saque: R$ {valor:.2f}\n" #concatena a variável extrato ao histórico
            numero_saques += 1 #para que a variável limite de saque aconteça pois todo saque será contabilizado
        
        else: 
            print("Operação falhou! o valor informado é inválido.")
    
    elif opcao == "3":
        print("\n****************** EXTRATO ******************")
        
        print("Não foram realizadas movimentações." if not  extrato else extrato) # if ternário condição escrita em uma linha
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("************************************************")
    
    elif opcao == "4":
        print("Obrigado e tenha um bom dia!")
        break

    else:
        print("Operação inválida, por favor selecione um dos números do painel")



