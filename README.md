# Contact Book

Este é um projeto de uma agenda telefônica implementada em Python. O objetivo é gerenciar contatos, armazenando telefones e e-mails de maneira organizada e eficiente.

## Estrutura do Projeto

O projeto está organizado em vários diretórios e arquivos, conforme descrito abaixo:

- **`classes/`**: Contém as classes principais, como `Contact`, `Phone`, e `Email`, responsáveis por gerenciar as entidades.
- **`config/`**: Arquivos de configuração do projeto.
- **`database/`**: Contém classes relacionadas ao gerenciamento de conexões e operações com o banco de dados.
- **`enums/`**: Define enumerações como `PhonesTypes` e `EmailTypes`, que são utilizadas para categorizar os tipos de telefone e emails.
- **`factories/`**: Contém fábricas para criação de objetos.
- **`logs/`**: Configuração e armazenamento dos logs gerados pelo sistema.
- **`util/`**: Contém utilitários e funções auxiliares que suportam o restante do projeto.
- **`.flake8`**: Configuração do Flake8 para análise de código, incluindo regras de estilo e exclusões.
- **`.pylintrc`**: Configuração do Pylint para análise estática de código.
- **`README.md`**: Arquivo de documentação do projeto.
- **`app.py`**: Script principal para execução do sistema de agenda telefônica.
- **`main.py`**: Outro ponto de entrada para testes e funcionalidades específicas.

## Funcionalidades

- **Gerenciamento de Contatos**: Permite a criação, leitura, atualização e exclusão (CRUD) de contatos.
- **Suporte a Vários Tipos de Telefone**: Suporte para tipos de telefone como Celular, Fixo, VoIP, Fax, Satélite e Emergência.
- **Persistência de Dados**: Salva e recupera contatos e informações associadas de um banco de dados.
- **Logs**: Configuração para registrar eventos e erros do sistema.

## Requisitos

- Python 3.x
- MySQL
- Bibliotecas listadas no `requirements.txt` (se aplicável)

## Como Usar

1. **Clonar o Repositório**:
   ```bash
   git clone https://github.com/ifatinha/contact-book.git

2. **Configurar o Ambiente Virtual:**
    ```
    python3 -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. **Instalar Dependências:**
    ```
    pip install -r requirements.txt
    ```

3. **Executar o Projeto:**
    ```
    python app.py
    ```

4. **Contribuições**
Contribuições são bem-vindas! Por favor, siga as boas práticas ao abrir issues ou pull requests.

5. **Licença**
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
