# Receba nota1
# Receba nota2
# Receba nota3

# media = (nota1 + nota2 + nota3) / 3

# se (media >= 7) então
#     informe("Aprovado")
# senão se (media < 5) então
#     informe("Reprovado")
# senão
#     informe("De Recuperação")
print(f'\nBem vindo a calculadora de média de notas')

while True:
    print(f'\n \nEscolha uma opção: \n1. Calular média de notas \n2. Sair')

    opcao = input(f"\nDigite o número da opção desejada: ")
    if opcao == '1':
        nome = input(f'\nDigite o nome do aluno: ')
        identificação = input('Digite o número do ID do aluno: ')
        while True:
            try:
                nota1 = float(input('Nota 1: '))
                nota2 = float(input('Nota 2: '))
                nota3 = float(input('Nota 3: '))
                break
            except:
                print('Por favor, digite um número válido para as notas.')

        media = (nota1 + nota2 + nota3) / 3

        if media >= 7:
            print(f'O aluno {nome} ID: {identificação} está APROVADO!')
        elif media < 5:
            print(f'O aluno {nome} ID: {identificação} está REPROVADO!')
        else:
            print(f'O aluno {nome} ID: {identificação} está de RECUPERAÇÃO!')

    elif opcao == '2':
        print('Fechando o programa...')
        break
    else:
        print('Opção inválida. Por favor, escolha 1 ou 2.')