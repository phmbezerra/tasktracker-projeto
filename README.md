# TaskTracker

Aplicação de linha de comando desenvolvida em Python para cadastro e visualização de tarefas.

## Funcionalidades

- Cadastrar novas tarefas
- Validar título obrigatório
- Validar prioridade
- Visualizar tarefas cadastradas
- Exibir o status das tarefas

## Dados de uma tarefa

Cada tarefa possui:

- Título
- Descrição
- Prioridade
- Data limite
- Status

## Tecnologias utilizadas

- Python 3
- Git
- GitHub

## Estrutura do projeto

tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py

## Instalação

1. Clone o repositório.
2. Certifique-se de possuir o Python 3 instalado.
3. Abra o terminal na pasta do projeto.

O projeto não utiliza bibliotecas externas.

## Execução

Execute:

python src/main.py

## Execução com Docker

O TaskTracker também pode ser executado em um container Docker, sem a necessidade de instalar o Python diretamente na máquina.

### Pré-requisitos

- Docker Desktop instalado e em execução
- Docker Compose disponível

### Construir a imagem

```bash
docker build -t tasktracker .
```

### Executar com Docker

```bash
docker run -it --rm tasktracker
```

### Executar com Docker Compose (recomendado)

```bash
docker compose run --rm tasktracker
```

### Funcionamento

O Dockerfile utiliza a imagem python:3.11-slim e configura a execução automática da aplicação.

O Docker Compose permite a interação com o menu por meio das configurações stdin_open e tty.

As tarefas ficam armazenadas temporariamente na memória durante a execução do programa.

## Autor

Paulo Henrique de Melo Bezerra  
Ciência da Computação — CEUB  
Campus Asa Norte — Noturno