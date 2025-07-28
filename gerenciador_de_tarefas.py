import os
import cmath
import time

pular_linha = 70 * ('-')

def voltar_ao_menu():

    voltar_ao_menu_mensagem = input('Aperte "ENTER" para voltar ao menu.')
    os.system('cls')
    menu_escolha_de_opcao()

lista_de_tarefas = ['Comer', 'Ir no mercado', 'Sair']
quantidade_de_itens_na_lista = len(lista_de_tarefas)


def menu_escolha_de_opcao():

    try:
        print('Digite o que deseja realizar no programa: ', end='')
        escolha_de_opcao = int(input())

        match escolha_de_opcao:
            case 1:
                if not lista_de_tarefas:
                    print('Sua lista está vazia no momento, '
                          'gostaria de adicionar algo? S/N: '
                          )
                    
                else:
                    print(f'Essa é a sua lista no momento: {lista_de_tarefas}. ')
                    print('Deseja adicionar alguma coisa? S/N: ')

                opcao_um_gerenciar_lista()

            case 2:
                print('Essa é a sua lista no momento: ')
                loop_mostrar_lista()
                          
    except ValueError:
        print('Por favor, digite apenas opções válidas: ')
        menu_escolha_de_opcao()


def opcao_um_gerenciar_lista():
    resposta_adicionar_item_na_lista = input().upper()
    print(pular_linha)

    if resposta_adicionar_item_na_lista == 'S':
        print('Digite oque você deseja adicionar na lista: ', end='')

        adicionar_item_na_lista = input()

        lista_de_tarefas.append(adicionar_item_na_lista)

        print(f'Essa é a sua lista atualizada: ')

        loop_mostrar_lista()


def loop_mostrar_lista():
    i = 0
    numeracao_lista = 1

    indices_lista = len(lista_de_tarefas)

    while indices_lista:

        try:
            numeracao_string = str(numeracao_lista)
            print(f'{numeracao_string} => {lista_de_tarefas[i]}')

            i += 1
            numeracao_lista += 1

        except:
            print(pular_linha)
            voltar_ao_menu()

menu_escolha_de_opcao()



