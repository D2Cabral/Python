import textwrap

def menu(): 
    menu = """\n

    ========================= MENU ===============================
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova Conta
    [lc]\t Listar Contas
    [nu]\t Novo Usuário
    [q]\t Sair    
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito :\t R$ {valor: .2f}\n"
        print("\n === Depósito realizado com sucesso! ====")
    else:
        print("\n@@@ Operação falhou, o valor informado é invalido. @@@")   
        
    return saldo, extrato        

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    execedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if execedeu_saldo:
        print("\n@@@ Operação falhou, voce não possui saldo suficiente. @@@")
        
    elif execedeu_limite:
        print("\n@@@ Operação falhou, valor do saque excede o limite. @@@")   
        
    elif execedeu_saques:
        print("\n@@@ Operação falhou, Número maximo de saques excedido. @@@")      
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso!. ===")    

    else:
        print("\n@@@ Operação falhou! o valor informador é inválido. @@@")
        
    return saldo, extrato

def exibir_extrato(saldo, /, * , extrato):
    return 0

def criar_usuario(usuarios):
    return 0 

def filtrar_usuarios(cpf, usuarios:)              
               
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
   
    while True:    
        opcao = menu()
    
        if opcao == "d":        
            valor = float(input("Informe o valor:"))
            saldo, extrato = depositar(saldo, valor, extrato)   
              
        elif opcao == "s":
            
            valor = float(input(("Informe valor desejado: ")))
            saldo, extrato = sacar (
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )
                     
        elif opcao == 'e':        
            exibir_extrato(saldo, extrato= extrato)
            
        elif opcao == 'nu':
            criar_usuario = (usuarios) 
            
        elif opcao == 'lc':
            listar 
                
        elif opcao == 'q':
            break    

    else: 
        print("Operacao inválida, por favor selecione a operação desejada.") 
               
return     