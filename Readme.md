# Boletim Escolar 2.0 - Python

Este é um programa simples em Python criado para **estudar a manipulação de arquivos**. O código permite registrar as notas de um aluno em diversas matérias, ler as notas armazenadas e formatar o boletim (limpando o arquivo). O objetivo principal é entender como capturar dados interativos do usuário e gravá-los de forma organizada em um arquivo de texto.

## Funcionalidades

- **Adicionar Notas**: O programa solicita ao usuário o nome do aluno e, em seguida, o nome da matéria e a nota correspondente. O usuário pode inserir quantas matérias e notas desejar.
- **Ler Notas**: O programa permite que você leia o conteúdo do arquivo `boletim.txt`, exibindo as notas de todos os alunos cadastrados.
- **Formatar Boletim**: Caso deseje, o programa permite apagar o conteúdo do arquivo de notas e recomeçar a inserção de dados, através da opção de "formatar" o boletim.
- **Validação de Notas**: Há uma validação para garantir que as notas estejam entre 0 e 10. Caso contrário, o programa solicitará que o usuário insira um valor válido.

## Como usar

1. **Clone este repositório** ou baixe o arquivo Python:
    ```bash
    git clone https://github.com/QuaseVitor/BoletimPy.git
    ```

2. **Execute o script**:
    - Certifique-se de ter o Python 3 instalado em seu computador.
    - Navegue até o diretório onde o arquivo Python está localizado e execute:
      ```bash
      python Main.py
      ```

3. **Interaja com o programa**:
    - O programa oferecerá três opções:
        - **Adicionar Notas**: Insira o nome do aluno, as matérias e as notas.
        - **Ler Notas**: Exibe o conteúdo do arquivo `boletim.txt`.
        - **Formatar Boletim**: Apaga o conteúdo atual do arquivo e permite inserir novas notas.
    - Para adicionar notas, digite o nome da matéria e a nota. Digite "Sair" para finalizar a inserção de notas.
    
4. **Verifique o arquivo de saída**:
    - As informações serão gravadas no arquivo de texto chamado `boletim.txt`. Você pode abrir esse arquivo para visualizar os dados inseridos.

## Exemplo de Execução

### Adicionar Notas

```
O que você deseja fazer?
    Adicionar notas
    Ler notas
    Formatar Boletim
Adicionar
Insira o nome do aluno: João
insira o nome da materia: Matemática
insira a nota: 8
insira o nome da materia: Português
insira a nota: 7
insira o nome da materia: Sair

Arquivo 'boletim.txt' gerado:
João:
Matemática = 8
Português = 7
```

### Ler Notas

```
O que você deseja fazer?
    Adicionar notas
    Ler notas
    Formatar Boletim
Ler
João:
Matemática = 8
Português = 7
```

### Formatar Boletim

```
O que você deseja fazer?
    Adicionar notas
    Ler notas
    Formatar Boletim
Formatar
O boletim foi apagado e está pronto para novos dados.
```

## Observações

- **Validação de Notas**: O programa verifica se a nota inserida está dentro do intervalo de 0 a 10. Caso contrário, solicita que o valor seja refeito.
- **Acúmulo de Dados**: As informações de cada aluno são adicionadas ao final do arquivo `boletim.txt`. Cada aluno e suas respectivas notas são registrados de forma estruturada.
- **Formato do Arquivo**: O arquivo `boletim.txt` contém os dados no formato:
    ```
    João:
    Matemática = 8
    Português = 7
    ```

## Objetivo

Este projeto foi desenvolvido como um estudo de manipulação de arquivos em Python, especificamente para aprender a trabalhar com a leitura e escrita de arquivos de texto. Além disso, o programa aborda como permitir a interação com o usuário para adicionar, ler e formatar dados, além de garantir a integridade da entrada com validações.
