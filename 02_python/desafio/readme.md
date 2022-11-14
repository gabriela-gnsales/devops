# DESAFIO - Fim do módulo

### Criar um sistema cadastral de usuários, modular e com armazenamento de dados em arquivo.

### Requisitos do sistema:

- [X] Menu principal contendo os itens:
    - imprimir lista de usuários: imprimir todos registros na tela, não precisa estar formatado;
    - buscar por um usuário: imprimir o registro do usuário com texto formatado;
    - cadastrar um novo usuário: imprimir o registro do usuário cadastrado na tela e uma mensagem de que o cadastrado foi realizado com sucesso;
    - remover um usuário: imprimir o registro do usuário deletado na tela e uma mensagem de que a remoção foi realizada com sucesso;
    - atualizar os dados de um usuário: imprimir o registro do usuário antes e depois da atualização na tela e uma mensagem de que a atualização foi realizada com sucesso;
    - [bônus] estatísticas do sistema: imprimir um texto formatado com as principais estatísticas do sistema;
    - sair do sistema: encerra a execução do sistema.

- [X] As informações cadastrais devem possuir pelo menos as seguintes opções:
    - nome;
    - gênero;
    - e-mail;
    - telefone;
    - cpf;
    - data de nascimento no formato (dd/mm/aaaa).

- [X] As funções devem ser modularizadas, permitindo reaproveitamento de código.

- [X] A função de buscar pelo usuário deve possuir uma formatação especial, em forma textual.

- [X] O gerenciamento e armazenamento dos dados de usuários deve ser feito em um arquivo.

- [X] O arquivo deve conter o cabeçalho na primeira linha e os registros de usuários nas linhas abaixo.

- [X] Cada registro de usuário deve ocupar uma linha no arquivo

- [X] Deve adotar pelo menos um controle de exceção utilizando o conceito de try/except no sistema

- [X] Deve utilizar alguma estrutura de dados no sistema: lista, tupla, conjunto ou dicionário

- [X] [Bônus] Na função de estatística do sistema, deve imprimir um texto formatado contendo as seguintes estatísticas:
    - quantidade de usuários cadastrados;
    - quantidade de usuários por gênero;
    - quantidade de usuários pelas faixas de idade:
        - até 18 anos / 18 a 35 anos / 35 a 65 anos / maiores que 65 anos.
