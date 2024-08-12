"""
Módulo de Gerenciamento de Contatos

Este módulo implementa a aplicação de gerenciamento de contatos, proporcionando
um loop principal que permite ao usuário interagir com o sistema por meio de um menu.

O menu oferece opções para criar um novo contato, listar contatos existentes,
ou encerrar a aplicação.

Funções:
--------
app() -> None
    Executa o loop principal da aplicação de gerenciamento de contatos. Exibe
    um menu de opções para o usuário e aguarda a seleção, executando ações
    correspondentes com base na escolha.

Uso:
-----
    Para executar a aplicação, use o seguinte comando:

    python main.py

    O menu será exibido, permitindo ao usuário selecionar entre criar um novo
    contato, listar contatos, ou encerrar a aplicação.
"""

# pip freeze > config/requirements.txt
# pip install -r requirements.txt

from util.menu import menu
from database.db_initializer import initialize_database


def app():
    """
    Executa o loop principal da aplicação de gerenciamento de contatos.

    Antes de iniciar o loop, verifica e cria o banco de dados necessário para
    armazenar os contatos, se ele ainda não existir.

    Este método exibe um menu de opções para o usuário e aguarda a seleção
    de uma das seguintes opções:

    - "1": Exibe a mensagem "Novo Contato" para a criação de um novo contato.
    - "2": Exibe a mensagem "Listar contatos" para listar todos os contatos.
    - "0": Exibe a mensagem "Encerrando aplicação!" e encerra o loop, finalizando a aplicação.

    Se uma opção inválida for selecionada, exibe a mensagem "Opção inválida!".

    O loop continua até que a opção "0" seja selecionada.
    """

    initialize_database()

    while True:
        opcao = menu()

        if opcao == "1":
            print("Novo Contato")
        elif opcao == "2":
            print("Listar contatos")
        elif opcao == "0":
            print("Encerrando aplicação!")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    app()
