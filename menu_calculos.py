import cmath # Para fazer cálculos complexos.
import time

# Boas vindas ao usuário
print('Olá, seja muito bem vindo ao Menu de Cálculos. Para iniciar digite o seu nome, por favor:')
nome_usuario = input('Digite o seu nome: ').capitalize()

print()

print(f'Certo {nome_usuario}, para começarmos eu preciso que você selecione oque gostaria de calcular: ')
print('-' * 40)

# Apresenta o menu de opções para o usuário.
def menu_opcoes_calculos():
    print('(Média escolar) = 1')
    print('(Conversor de temperatura) = 2')
    print('(Fórmula de Bhaskara) = 3')
    print('(Adição, subtração, multiplicação ou divisão) = 4')
    print('(Sair do aplicativo) = 5')

# Verifica a opção digitada pelo usuário e direciona ele até a opção desejada.
def resposta_do_usuario(resposta_usuario_menu):
    match resposta_usuario_menu:

        # Opção 1: Calcula a média do usuário de acordo com suas notas e mostra se ele efoi aprovado ou não.
        case '1':
                print('Para calcular a sua média eu preciso que você me informe as suas notas:\n')
                
                n1 = float(input('Nota 1: '))
                n2 = float(input('Nota 2: '))
                n3 = float(input('Nota 3: '))
                n4 = float(input('Nota 4: '))

                print()

                calculo_media_notas = (n1 + n2 + n3 + n4) / 4

                print(f'{nome_usuario}, a sua média é {calculo_media_notas:.2f}.')

                print()

                if calculo_media_notas >= 7:
                    print('Parabéns, você foi aprovado!')

                else:
                    print('Sinto muito, você foi reprovado.')

                print()

        # Opção 2: Converte uma unidade de medida de temperatura em outra e apresenta se está abaixo do ponto de congelamento.
        
        case '2':
            print('Certo, qual unidade de medida gostaria de converter?')
            print('(Fahrenheit para Celsius) = 1')
            print('(Celsius para Fahrenheit) = 2')

            print()
            
            resposta_case_2 = input('Digite sua escolha: ')

            print()

            # Converte a temperatura de Fahrenheit para Celsius de acordo com valor que o usuário digitou.
            if resposta_case_2 == '1':
                temperatura_fahrenheit = float(input('Certo, qual a temperatura em °F?:\n'))

                fahrenheit_celsius = (temperatura_fahrenheit - 32) // 1.8
                    
                print(f'O resultado é {fahrenheit_celsius} °C.\n')

            # Converte a temepratura de Celsius para Fahrenheit de acordo com o valor que o usuário digitou.
            elif resposta_case_2 == '2':
                temperatura_celsius = float(input('Certo, qual a temperatura em Celsius?:\n'))

                print()

                celsius_fahrenheit = temperatura_celsius * 1.8 + 32
            
            # Mostra se a temperatura em Fahrenheit está acima, igual ou abaixo do ponto de congelamento.
                if celsius_fahrenheit > 32:
                    print(f'O resultado é {celsius_fahrenheit:.1f} °F.\nA temperatura está acima do ponto de congelamento.')

                elif celsius_fahrenheit == 32:
                    print(f'O resultado é {celsius_fahrenheit:.1f} °F.\nA temperatura está no ponto de congelamento.')

                else: 
                    print(f'O resultado é {celsius_fahrenheit:.1f} °F.\nA temperatura está abaixo do ponto de congelamento.')

            #Retorna ao menu se a opção for inválida
            else:
                print('Por favor, digite um número válido')
                
            print()

        # Opção 3: Calcula a equação de segundo grau (Bhaskara) de acordo com os valores que o usuário digitou.
        case '3':
            print(f'Certo {nome_usuario}, para calcularmos eu preciso que me informe os valores da equação:\n')
            
            a = float(input('a = '))
            b = float(input('b = '))
            c = float(input('c = '))

            print()

            calculo_discriminante = (b ** 2) - 4 * a * c 

            calculo_bhaskara_x1 = (-b + cmath.sqrt(calculo_discriminante)) / (2 * a)
            calculo_bhaskara_x2 = (-b - cmath.sqrt(calculo_discriminante)) / (2 * a)

            # Mostra ao usuário as raízes Reais e Imaginárias da equação.
            print('As raízes da equação são: ')            
            print(f"x' = Real -> {calculo_bhaskara_x1.real:.2f} e imaginária -> {calculo_bhaskara_x1.imag:.2f}.")
            print(f'x" = Real -> {calculo_bhaskara_x2.real:.2f} e imaginária -> {calculo_bhaskara_x2.imag:.2f}.\n')
           
        # Opção 4: Realiza as operações básicas de acordo com a opção que o usuário escolheu.
        case '4':
            def escolha_operacoes_basicas():
                print(f'Certo {nome_usuario}, primeiro eu preciso que você selecione qual operação deseja efetuar:')

                print('(Soma) = 1')
                print('(Subtração) = 2')
                print('(Multiplicação) = 3')
                print('(Divisão) = 4\n')

                resposta_usuario_operacoes_basicas = input('Digite a sua escolha: ')

                print()

                if resposta_usuario_operacoes_basicas == '1':
                    print('Certo, digite os números que deseja somar:\n')

                
                lista_numeros_soma = []

                while len(lista_numeros_soma) <1000:
                    def operacao_soma():
                        numeros_soma = float(input())
                        lista_numeros_soma.append(numeros_soma)

                        print(f'Números para soma: {lista_numeros_soma}.\nDeseja adicionar mais um número? S/N:')

                        resposta_s_n = input()

                        print()

                        if resposta_s_n.lower() == 's':
                            operacao_soma()

                        elif resposta_s_n.lower() == 'n':
                            resultado_da_soma = sum(lista_numeros_soma)
                            print(f'Resultado = {resultado_da_soma:.1f}\nDeseja realizar uma nova soma? S/N: ')
                            realizar_nova_soma = input()

                            if realizar_nova_soma.lower() == 's':
                                lista_numeros_soma.clear()
                                print('-' * 40)
                                operacao_soma()

                            elif realizar_nova_soma.lower() == 'n':
                                print('-' * 40)
                                lista_numeros_soma.clear()
                                return loop_pricipal()
                                                                   
                        else:
                            print('Você não digitou uma opção válida')
                            lista_numeros_soma.clear()
                            escolha_operacoes_basicas()
                                 
                    operacao_soma()

            escolha_operacoes_basicas() 

        # Opção 5: Encerra o aplicativo.
        case '5':
            return False

    return True

# Faz o loop do menu de cálculos até que o usuário digite 5 e encerre o aplicativo.
def loop_pricipal():
    continuar = True
    while continuar:
        menu_opcoes_calculos()
        print()
        resposta_usuario_menu = input('Digite sua escolha: ')
        print('-' * 40)
        continuar = resposta_do_usuario(resposta_usuario_menu)
        if resposta_usuario_menu == '5':
            print('Encerrando aplicativo...')
            time.sleep(2)
            break

        elif resposta_usuario_menu <='4':
            input('Aperte "Enter" para voltar ao menu.')

        else:
            print('Opção inválida. Por favor, digite um número de 0-5.')
        print('-' * 40)

loop_pricipal()




    
    

    




    
 







