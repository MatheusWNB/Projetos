import os
import time

# Para evitar digitar as mesmas coisas
pular_linha = 70 * ('-')

# Listas
tarefas = [[],
           [],
           [],
           []
           ]

usuario = {'Matheus': tarefas[0],
           }

# Mensagem de inicio e cadastro do usuário:
def menu_inicial():
    print('Seja bem-vindo ao gerenciador de tarefas, para iniciar, digite o seu nome: ', end='')

    nome_usuario = input('')
    usuario[nome_usuario] = tarefas[1]

    print(f'Usuário "{nome_usuario}" cadastrado com sucesso!')
    print(pular_linha)

#Faz a validação para acessar uma lista específica

# Menu principal para escolha de opção do usuário:

def menu_escolha_de_opcao():

    print('Menu de opções:')
    print('1 => Gerenciar lista de tarefas \n'
          '2 => Mostrar lista de Tarefas \n'
          '3 => Acessar outra lista \n'
          '4 => Encerrar o programa'
          )

    print(pular_linha)

# Tenta validar a escolha do usuário:
    try:
        print('Digite o que deseja realizar no programa: ', end='')
        escolha_de_opcao = int(input())

        match escolha_de_opcao:
            case 1:
                if not usuario[acessar_lista]:
                    print('Sua lista está vazia no momento, '
                          'gostaria de adicionar algo? S/N: '
                          )

                else:
                    print('Deseja adicionar alguma coisa? "S/N" ou '
                          'deseja remover algo da lista? "R": '
                          )

                gerenciar_lista()

            case 2:
                print('Essa é a sua lista no momento: ')
                loop_mostrar_lista()

            case 3:
                os.system('cls')
                validar_acessar_lista()

            case 4:
                print('Saindo do programa...')
                time.sleep(2)
                os.system('cls')
                print('Aplicativo encerrado.')

# Retorna uma mensagem de erro e redireciona o usuário ao menu novamente para validar novamente:
    except ValueError:
        print('Por favor, digite apenas opções válidas: ')
        menu_escolha_de_opcao()

# Faz o gerencionamento da lista para adicionar ou remover algo da lista:


def gerenciar_lista():
    adicionar_remover_algo_da_lista = input().upper()
    os.system('cls')

    if adicionar_remover_algo_da_lista == 'S':
        print('Digite oque você deseja adicionar na lista: ', end='')

        adicionar_item_na_lista = input()

        usuario[acessar_lista].append(adicionar_item_na_lista)

        print(f'Essa é a sua lista atualizada: ')

        loop_mostrar_lista()

    elif adicionar_remover_algo_da_lista == 'R':
        print(f'Essa é a sua lista: {usuario[acessar_lista]}.')
        print('')

        while True:
            print('Para remover algo, digite o índice que corresponde ao item que '
                  'que deseja remover: ', end='')

            remover_item_da_lista = int(input())

            try:
                print(
                    f'O item "{remover_item_da_lista}" foi removido da lista. ')

                lista_de_tarefas.pop(remover_item_da_lista)

                print('Lista atualizada com sucesso: ')
                print(pular_linha)
                loop_mostrar_lista()

            except IndexError:
                print('Por favor, digite uma opção válida.')
                print(pular_linha)


# Faz a iteração dos itens na lista (tarefas) e mostra ao usuário:
def loop_mostrar_lista():

    numeracao_lista = 1
    
    for indice in usuario[acessar_lista]:

        numeracao_string = str(numeracao_lista)
        print(f'{numeracao_string} => {indice}')

    voltar_ao_menu()

# Funçao para voltar ao menu para evitar digitar toda vez:
def voltar_ao_menu():

    voltar_ao_menu_mensagem = input('Aperte "ENTER" para voltar ao menu.')
    os.system('cls')
    menu_escolha_de_opcao()


# Inicia o programa com o menu inicial de cadastro de usuário

while True:
    menu_inicial()
    
    print('Digite a lista que deseja acessar:')
    print()

    for nome in usuario:
        print(f'{nome}')

    acessar_lista = input()

    print(f'Lista de "{acessar_lista}" acessada com sucesso! ')
    print(pular_linha)
    menu_escolha_de_opcao()
