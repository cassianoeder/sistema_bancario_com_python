import time

clientes = {'Ederson Wermeier': {'Senha': '12345', 'Saldo': 600, 'Limite': 2000, 'Ativo': True, 'Extrato': ''},
            'Vini Moiano': {'Senha': '1234', 'Saldo': 100, 'Limite': 1000, 'Ativo': True, 'Extrato': ''},
            'Andre Almeida': {'Senha': '0123', 'Saldo': 500, 'Limite': 800, 'Ativo': False, 'Extrato': ''},
            'Monique Werner': {'Senha': '123', 'Saldo': 10500, 'Limite': 5000, 'Ativo': True, 'Extrato': ''}
            }

def transferencia(usuario):
    #em criacao
    pass

#funcao depositar
def depositar(usuario):
    while True:
        deposito = input(f''' 
Olá {usuario} qual valor deseja depositar?
Deposito --> R$: ''')
        
        #Verifica se os dados digitados sao numeros
        if deposito.isdigit():
            deposito = int(deposito)
            #Se o valor for maior que 4 ele continua
            if deposito >= 5:

                saldo_antigo = clientes[usuario]['Saldo']

                saldo_atualizado = clientes[usuario]['Saldo'] = saldo_antigo + deposito

                #Adiciona deposito no extrato
                clientes[usuario]['Extrato'] += f'Deposito de R$:{deposito}\n'

                print(f'\n\nSaldo anterior era R$:{saldo_antigo}\nSaldo atual R$:{saldo_atualizado}\nOperação finalizada!\n\n')
                menu(usuario)
                break

            #se o valor especificado é menor de 5    
            else:
                print('O valor mínimo de depósito é R$: 5,00')
                depositar(usuario)
                break

        else:
            print('Digite apenas numeros')
            depositar(usuario)
            break

def sacar(usuario):
    while True:

        saldo = clientes[usuario]['Saldo']
        limite = clientes[usuario]['Limite']
        ativo = clientes[usuario]['Ativo']
        limite_saque = saldo + limite

        valor_a_sacar = int(input(f'''
Olá {usuario} você tem R$:{saldo} disponível conta!
Seu limite é R$:{limite} portanto poderá sacar até R$:{limite_saque}

Quanto deseja sacar? '''))
        #caso a conta esteja ativa
        if ativo:
            #verificar se a entrada é numerica
            if type(valor_a_sacar) == float or type(valor_a_sacar) == int:

                if valor_a_sacar <= limite_saque:

                    print(f'SAQUE DE R$:{valor_a_sacar} EM ANDAMENTO..')

                    clientes[usuario]['Saldo'] = saldo - valor_a_sacar

                    #Adiciona saque no extrato
                    clientes[usuario]['Extrato'] += f'Saque de R$:{valor_a_sacar}\n'

                    time.sleep(3)

                    print('Contando cédulas..\nAguarde')

                    time.sleep(3)

                    print('Retire o valor abaixo\n')

                    time.sleep(4)

                    print('Operação finalizada com SUCESSO\n')

                    menu(usuario)

                    break
                else:
                    print('Entrada não permitida!\n Apenas números')
                    sacar(usuario)
                    break
        else:
            print('Encontramos um pequeno problema com a sua conta!\nPor gentileza contate o gerente!')
            break    

def extrato(usuario):

    #buscar cliente
    cliente = clientes[usuario]
    #buscar extrato
    extrato_cliente = cliente['Extrato']

    if extrato_cliente:
        exibir_extrato = (extrato_cliente)
    else:
        exibir_extrato = 'Sem movimentações até o momento!'

    return exibir_extrato

def menu(usuario):

    usuario = usuario
    saldo = clientes[usuario]['Saldo']
    while True:
        acao = input(f'''
        Olá {usuario} bom te ver!
        Saldo disponível em conta R$:{saldo}
    
        [1] - Sacar
        [2] - Depositar
        [3] - Transferencia
        [4] - Extrato 
        [5] - Sair
        Opção: ''')
        if acao == '1':
            sacar(usuario)
            break
        elif acao == '2':
            depositar(usuario)
            break
        elif acao == '3':
            transferencia(usuario)
            break
        elif acao == '4':
            print(extrato(usuario))
        elif acao == '5':
            print('Você saiu')
            break
        else:
            print(f"{acao} não corresponde a nenhuma tarrefa!")


#funcao login
def acessar_menu():
    tentativas_login = 3
    #Looping verifica credenciais de acesso ao menu do caixa
    while True:
        resposta_erro = 'Tente novamente'

        if tentativas_login < 2:
            resposta_erro = 'Ultima tentativa!'
        elif tentativas_login == 0:
            break
        nome = input("Informe o nome do cadastro: ")
        nome = nome.title()

        senha = input("Informe a senha da conta: ")
        senha = senha.lower()

        #se nome dentro de clientes e senha dentro do cliente informado
        if nome in clientes and senha == clientes[nome] ['Senha']:
            menu(nome)
            break
        else:
            print(f"Dados incorretos! {resposta_erro}")

        tentativas_login -= 1

acessar_menu()

#DESAFIO DE CODIGO DA DIO
#FALTA IMPLEMENTAR MAIS COISAS E MELHORAS ALGUMAS PARTES MAS FOI FEITO COM CARINHO