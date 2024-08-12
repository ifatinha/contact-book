"""
Este módulo contém a função `menu` para exibir um menu interativo ao usuário.

Funções:
---------
- menu(): Exibe um menu com opções para criar um novo contato, listar contatos existentes
  ou sair do programa. Retorna a escolha do usuário como uma string.
"""


def menu():
    """
    Exibe um menu interativo ao usuário com as opções:
    [1] Novo Contato, [2] Listar Contatos e [0] Sair.

    Retorna:
    --------
    str: A escolha do usuário, correspondente à opção selecionada no menu.
    """

    menu_input = """################ MENU ################
    [1] Novo Contato
    [2] Listar Contatos
    [0] Sair
    => """

    return input(menu_input)
