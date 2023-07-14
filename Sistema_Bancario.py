menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':        
        print("Depósito")
        deposito = float(input("Informe o valor:"))
        if deposito > 0 :
            saldo += deposito   
            extrato += f"Depósito: R$ {deposito: .2f}\n"
        else:
            print("Valor inválido")
             
    elif opcao == 's':
        valor_saque = int(input(("Informe valor desejado: ")))
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES 
              
        if  excedeu_saldo: 
            print("Saldo insuficiente")
        
        elif excedeu_limite: 
            print("Limite máximo de saque excedido")  
               
        elif excedeu_saque:
            print("Limite de saques excedido")  
                 
        elif valor_saque > 0: 
            saldo -= valor_saque        
            print("Retire o dinheiro")
            numero_saques+= 1
            extrato += f"Saque: R$ {valor_saque: .2f}\n"
                 
        else: 
            print("Informe um valor válido para realizar a operação")       
             
    elif opcao == 'e':        
        print("=================== EXTRATO ======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo: .2f}\n")
        print("========================================")
            
    elif opcao == 'q':
        break    

    else: 
        print("Operacao inválida, por favor selecione a operação desejada.") 
               