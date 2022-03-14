print('               Bem vindo a nossa calculadora multifunções')
print('\n  Escolha uma operação de nossa calculadora conforme as opções dispostas abaixo')
print('\nSoma = 1')
print('Subtração = 2')
print('Multiplicação = 3')
print('Divisão = 4')



opcao=int(input('\nEscolha uma opção: '))


if opcao == 1:
    print('\n\n\n\n\n\n\n                                      Calculadora de Soma')
    a=int(input("\n\n\n\n\n\nDigite um Valor: "))
    b=int(input("Digite um Valor: "))
    soma=a+b
    print('\nResultado', soma)
    
if opcao == 2:
    print('\n\n\n\n\n\n\n                                    Calculadora de Subtração')
    a=int(input("\n\n\n\n\n\nDigite um Valor: "))
    b=int(input("Digite um Valor: "))
    subtracao=a-b
    print('\nResultado', subtracao)

if opcao == 3:
    print('\n\n\n\n\n\n\n                                   Calculadora de Multiplicação')
    a=int(input("\n\n\n\n\n\nDigite um Valor: "))
    b=int(input("Digite um Valor: "))
    subtracao=a*b
    print('\nResultado', subtracao)
    
if opcao == 4:
    print('\n\n\n\n\n\n\n                                      Calculadora de Divisão')
    a=float(input("\n\n\n\n\n\nDigite um Valor: "))
    b=float(input("Digite um Valor: "))
    divisao=a/b
    print('\nResultado', divisao))