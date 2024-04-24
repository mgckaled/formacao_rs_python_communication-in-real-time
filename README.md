<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD014 -->

# Comunicação em tempo real Real com Flask - Formação Python

<div align="center">
  <img alt="Made by mgckaled" src="https://img.shields.io/badge/made%20by-mgckaled-darkblue">
  <img alt="GitHub Repo Size" src="https://img.shields.io/github/repo-size/mgckaled/trilha-python_communication-in-real-time-with-flask">
  <img alt="pylint badge" src="https://img.shields.io/badge/linting-pylint-yellowgreen">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</div>

## Sumário

- [Comunicação em tempo real Real com Flask - Formação Python](#comunicação-em-tempo-real-real-com-flask---formação-python)
  - [Sumário](#sumário)
  - [Sobre o Projeto](#sobre-o-projeto)
  - [Tecnologias](#tecnologias)
    - [Linguagem de Programação](#linguagem-de-programação)
    - [Gerenciadores de Ambiente Virtual](#gerenciadores-de-ambiente-virtual)
    - [Bibliotecas Instaladas (Packages)](#bibliotecas-instaladas-packages)
  - [Como clonar o projeto?](#como-clonar-o-projeto)
  - [Licença](#licença)

## Sobre o Projeto

Neste módulo, vamos explorar o conceito de notificações em tempo real e suas aplicações, além de discutir as estratégias mais comuns para implementá-las, como long pooling e WebSockets. Em seguida, teremos um projeto prático, onde construiremos uma API de pagamento do zero e implementaremos notificações em tempo real. O projeto envolverá a criação de um pagamento simulado de PIX e a confirmação desse pagamento em tempo real.

Notificações em tempo real são importantes para enviar informações imediatas aos usuários sem que eles precisem atualizar manualmente a página. O WebSocket é uma tecnologia utilizada para implementar notificações em tempo real, permitindo a comunicação bidirecional entre o cliente e o servidor com baixa latência. Exemplos de aplicações que utilizam WebSocket incluem chats em tempo real, rastreamento de atividades e ferramentas de colaboração. A estratégia de long pooling também pode ser utilizada, mas é mais adequada para sistemas que não requerem atualizações em tempo real constantes. Na próxima aula, aprenderemos a implementar um sistema de notificações em tempo real com WebSocket.

> [anotações](./github/docs/notes.md)

## Tecnologias

### Linguagem de Programação

- [`python`](https://www.python.org/) (v3.11.5)

### Gerenciadores de Ambiente Virtual

- [`pyenv`](https://github.com/pyenv/pyenv)
- [`pipenv`](https://pipenv.pypa.io/en/latest/)

### Bibliotecas Instaladas (Packages)

- [`flask`](https://flask.palletsprojects.com/en/3.0.x/)

## Como clonar o projeto?

1. Certifique-se de que está usando o `pyenv` e o `pipenv` para gerenciar as dependências do projeto. Veja como instalar e configurar clicando nos respectivos links do tópico [Gerenciadores de Ambiente Virtual](#gerenciadores-de-ambiente-virtual).

2. Faça o clone pelo Github:

    ```shell
    $ git clone https://github.com/mgckaled/trilha-python_communication-in-real-time-with-flask.git
    ```

3. Acesse o diretório:

    ```shell
    $ cd trilha-python_communication-in-real-time-with-flask
    ```

4. Instale as dependências do arquivo `requirements.txt`:

    ```shell
    $ pipenv install -r requirements.txt
    ```

5. Ative o ambiente virtual no seu terminal

    ```shell
    $ pipenv shell
    ```

## Licença

Distribuído sob a licença *MIT*. Veja [LICENSE](LICENSE) para mais informações.

---

<h5 align="center">
  2024 - <a href="https://github.com/mgckaled/">Marcel Kaled</a>
</h5>
