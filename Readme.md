# Boletim Escolar - Python

Este é um programa simples em Python criado para **estudar a manipulação de arquivos**. O código permite registrar as notas de um aluno em diversas matérias e armazenar essas informações em um arquivo de texto. O objetivo principal é entender como capturar dados interativos do usuário e gravá-los de forma organizada em um arquivo.

## Funcionalidade

- O programa solicita ao usuário o nome do aluno e, em seguida, o nome da matéria e a nota correspondente.
- O usuário pode inserir quantas matérias e notas desejar. O processo é encerrado ao digitar "Sair" no campo da matéria.
- As informações de cada aluno são gravadas no arquivo `boletim.txt`, onde o nome do aluno e suas respectivas notas são armazenados de forma estruturada.

## Como usar

1. **Clone este repositório** ou baixe o arquivo Python:
    ```bash
    git clone https://github.com/usuario/repositório.git
    ```

2. **Execute o script**:
    - Certifique-se de ter o Python 3 instalado em seu computador.
    - Navegue até o diretório onde o arquivo Python está localizado e execute:
      ```bash
      python Main.py
      ```

3. **Interaja com o programa**:
    - O programa solicitará o nome do aluno.
    - Em seguida, você será solicitado a inserir o nome das matérias e suas respectivas notas.
    - Para encerrar a inserção de dados, digite `Sair` quando solicitado pelo nome da matéria.

4. **Verifique o arquivo de saída**:
    - As informações serão gravadas em um arquivo de texto chamado `boletim.txt`. Você pode abrir esse arquivo para visualizar os dados inseridos.

## Exemplo de Execução

```
Insira o nome do aluno: João
insira o nome da materia: Matemática
insira a nota: 8
insira o nome da materia: Português
insira a nota: 7
insira o nome da materia: Sair

Arquivo 'boletim.txt' gerado:
João:
Matemática == 8
Português == 7
```

## Observações

- O programa possui validação para impedir a entrada de valores inválidos para as notas. Caso um valor inválido seja inserido (por exemplo, uma letra no lugar de um número), o programa solicitará novamente a entrada da nota.
- O arquivo `boletim.txt` vai acumulando os dados de todos os alunos inseridos. Cada aluno e suas respectivas notas são adicionados ao final do arquivo.

## Objetivo

Este projeto foi desenvolvido como um estudo de manipulação de arquivos em Python, especificamente para aprender a trabalhar com a leitura e escrita de arquivos de texto. Através dele, foi possível entender como gravar dados de forma contínua e como estruturar informações de maneira simples em arquivos locais.

