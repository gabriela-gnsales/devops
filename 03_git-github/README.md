# MÓDULO: GIT / GITHUB

### Git
[Documentação do Git](https://git-scm.com/docs/git/pt_BR)

Ferramenta/sistema de versionamento e monitoramento de código
  * aponta para a branch atual → `cat .git/HEAD`
  * onde está apontando uma branch para o respectivo commit → `cd .git/refs`
  * onde os arquivos estão sendo salvos, de forma compactada → pasta `cd .git/objects`

### GitHub / GitLab / Bitbucket / AWS CodeCommit ...
##### Plataformas de versionamento, de forma distribuída, centralizada e global
* GitHub é o mais utilizado → centraliza os principais códigos OpenSource
> __OpenSource:__ plataforma aberta, código público → é possível ler a estrutura do código, alterá-la e repassar/recompartilhar com a alteração; projeto que a comunidade contribui; 2 instituições fundamentais nesse processo: __Linux Foundation__ e __Cloud Native Computing Foundation (CNCF)__ 
* GitHub Pages (documentação)
* Interface gráfica

### Fluxos de Trabalho (Workflow) 
* Git Flow, GitHub Flow e GitLab Flow
>Dica: uma boa prática na hora de criar os branches é prefixá-los com o tipo do trabalho que será feito: para novas funcionalidades, nomeie-o como `feature/<nome-da-funcionalidade>`; para correções de bugs, use `hotfix/<descrição-da-correção>`; e se o Fluxo que você escolher necessidade de branches de releases, chame-os de `release/<versão>`.

#### Estrutura Git Flow: 
* __main / master:__ branch principal que aponta para o ambiente de produção
* __feature:__ ambiente de desenvolvimento de features, desenvolvimento da história
* __develop:__ apontar para o ambiente de desenvolvimento, fazer o deploy e implantar na conta da AWS de desenvolvimento
* __realese / homolog:__ implantar numa conta para os stackholders (gerentes, POs...) homologarem
* __hotfix:__ branch destinada para quando há algum bug a ser corrigido; branch gerada a partir da main

__OBS:__ outra estrutura para fazer o gerenciamento de branchs → _Trunk Based Development_

__branch:__ apontamento para um determinado commit; cópias do código; cada branch é um estado atual do código

__commit:__ entregável, mostra determinado satus do código, snapshot, confirmação da entrega

### Principais comandos:
* `git init` → inicializar o repositório
* `git status` → verificar status dos arquivos do repositório
* `git add <nome(s) do(s) arquivo(s)>` ou `git add . ` (todos os arquivos) ou `git add *` ou `git add -A` → adicionar os arquivos do repositório para serem monitorados/versionados pelo git 
* `git commit -m 'Mensagem - descrição commit'` → salva as as alterações, isto é, o status e a versão atual; tem um hash que dá para buscar pelos primeiros 4/5 dígitos
  * `-m` é uma flag que aponta para a mensagem de descrição
* `git commit <nome-do-arquivo> -m "Mensagem de alteração"`
* `git commit -am "Descrição commit"`
* `git push <nome repositório remoto> <nome branch>` → `git push origin main` → enviar o código para o repositório remoto (origin)
* `git pull` → trazer o código do repositório remoto para o local, sincronizar, atualizar o repositório local
* `git merge <nome da branch com os códigos que serão passados para a branch atual>` → juntar as branchs, necessitando resolver conflitos em alguns casos
> A mesclagem de um branch é utilizada quando queremos incorporar todas as modificações efetuadas naquele branch para o qual estamos trabalhando neste momento - ao contrário do `cherry-pick`, que traz apenas um único commit.
* `git diff` → para exibir as alterações nos arquivos antes de realizar o comando `git add .`
* `git diff <branch 1> <branch 2>` → para ver as diferenças entre branches
* `git stash push` → para salvar essas alterações, guardá-las e removê-las do estado atual do seu projeto, mantendo-o "limpo" novamente
* `git stash pop` → para restaurar as modificações
* `git stash list` → para ver a lista de modificações feitas
* `git stash pop <número da modificação>` → para restaurá-la
* `git stash apply` → não remove aquela alteração da pilha, permitindo então a rápida mudança entre diversos estados salvos em seguida

__OBS:__

`-m <msg>`

`--message=<msg>`

Use the given `<msg>` as the commit message. 

If multiple `-m` options are given, their values are concatenated as separate paragraphs.

The `-m` option is mutually exclusive with -c, -C, and -F.

### Comandos branchs
* `git branch` → saber qual branch está e quantas branchs têm
* `git checkout <nome_branch>` / `git switch <nome_branch>` → trocar de branch
* `git checkout -b <nome_nova_branch>` / `git switch -c <nome_nova_branch>` → criar uma nova branch e trocar para ela aparecer 
[Diferença entre "git switch" e "git checkout"? - Stack Overflow em Português](https://pt.stackoverflow.com/questions/533866/qual-a-diferença-entre-git-switch-e-git-checkout)

### Comandos remote
* `git remote` → mostrar o nome dos repositórios remotos
* `git remote -v` → para ver o endereço do repositório remoto
* `git remote add origin (ou outro nome) <URL repositório remoto (no GitHub ou outra plataforma)>` →
  * origin = nome padrão do repositório remoto, mas pode ser qualquer outro
* `git remote set-url origin git@github.com:nome_usuario/nome_repositorio.git` →
* `git remote remove <name>` → remover apontamento do repositório remoto
* `git remote rename <old name> <new name>` → renomear URL do repositório remoto

### Comandos para desfazer modificações / fazer alterações e manipulações nos commits e nas branchs:
* `git restore <caminho (no caso de um arquivo que foi excluído de uma pasta) ou arquivo a ser restaurado>` → para desfazer uma alteração que não foi commitada ainda / desfazer uma marcação de adição ou remoção de arquivos
* `git restore --staged` → para reverter um arquivo que foi adicionado ou removido acidentalmente depois do `git add .` → para torná-lo untracked (não rastreado pelo git)
* `git restore --source <hash do commit>` → para reverter determinado arquivo para o commit informado
* `git reset <sha1-do-commit>` → alteração que foi commitada, permitirá reverter o commit; git descarta a execução dos commits após aquele especificado, mas mantém suas alterações; apaga o commit do histórico
* `git reset --hard <sha1-do-commit>` → se quisermos realmente descartar as mudanças feitas após aquele commit, devemos informar o parâmetro `--hard`
* `git revert` → cria um commit "inverso", revertendo as modificações introduzidas → linhas que foram removidas serão adicionadas, arquivos que foram adicionados serão excluídos, e assim sucessivamente
* `git commit --amend` → para editar um commit
* `git commit --amend --no-edit` → para editar um commit sem editar a mensagem
* `git cherry-pick` → para escolher individualmente commits (de uma branch) para serem incorporados a outro trabalho/branch
* `git rebase <nome-da-branch-base> <nome-da-base-que-quero-atualizar>` → [Documentação oficial do Git: Rebase](https://git-scm.com/book/pt-br/v2/Branches-no-Git-Rebase)
  * `git push -f origin` → informar o servidor remoto que houve uma grande modificação, passando a opção `-f` para forçar a reescrita do histórico no `push`
  * `git push -u origin main`
  * `git rm -r --cached <arquivo ou pasta que quer que o git pare de monitorar>` → para excluir do repositório remoto pastas/arquivos que foram incuídos no .gitignore depois
  * `git commit -m 'Removendo arquivos da staging area'`
  * `git branch -M main` → renomear branch para 'main'

### Comandos para visualizar o histórico de commits
* `git log` → para listar todos os commits que foram realizados
> Cada bloco apresenta um commit, com seu hash SHA-1, autor (que configuramos globalmente no início deste material), data e a mensagem (por isso a importância de utilizar mensagens explicativas)
* `git log --pretty=oneline` → para mostrar de um jeito mais clean, simplificado, em uma linha
* `git log --follow <nome arquivo>` → para restringir os logs apenas para um arquivo
* `git show <id do commit mostrado no git log = hash` → para visualizar as alterações feitas em um único commit; é suficiente pegar apenas os 4 ou 5 primeiros códigos do ID (hash)
* `git blame <nome arquivo>` → para saber as últimas modificações feitas em cada linha de um arquivo
> Com esse comando, conseguimos ver a versão curta do hash SHA-1, o autor e a data do último commit que modificou aquela linha. Esse comando é muito útil quando quisermos saber quando uma certa linha foi alterada pela última vez.

> O __hash SHA-1__ é uma identificação única do commit → [The Git Commit Hash](https://www.mikestreety.co.uk/blog/the-git-commit-hash/)


➡ Para gerar um arquivo de patch: `git diff -p > ~/meu-patch.diff`

➡ Para gerar patches com metadados dos commits; gera um arquivo pronto para ser enviado por email: `git format-patch`
> Os patches são utilizados quando você não possui acesso de escrita ao repositório (ou seja, não pode efetuar commits nele) mas precisa compartilhar certas alterações com outras pessoas até que o responsável pelo projeto aceite as mudanças.
* `git apply` → para compartilhar o arquivo com outras pessoas para que elas apliquem o patch

➡ Para criar um novo repositório no GitHub pelo CLI: `gh repo create [<name>] [flags]`

➡ Para desfazer um commit: `git reset HEAD~1`

➡ Para ver o SHA1: git log → `ls .git/objects`

* __PR (pull request):__ requisição para fazer o merge de 2 branchs
* __clone do repositório:__ clono o repositório para minha máquina e fica isolado do repositório raiz/origem
* __fork do repositório:__ clono o repositório para minha máquina e fica atrelado ao repositório raiz/origem, sinzronizado, podendo mandar uma PR → funcionamento do OpenSource
> O "fork" consiste em duplicar um repositório que você não possui acesso de escrita para sua própria conta, fazer as alterações nessa cópia e informar ao dono do projeto através de um Pull Request (PR) que essa sua versão possui funcionalidades que podem beneficiar aquele sistema. Esse processo é a base da colaboração da comunidade, e é o que fez o GitHub crescer tanto em popularidade.

### Ciclo de vida do software:
* Alpha, beta, release candidate, GA (general available)
  * __Major:__ quando há uma quebra de compatibilidade da aplicação com a versão anterior
  * __Minor:__ alteração que acrescenta uma feature nova, mas mantém a compatibilidade
  * __Path:__ correção de bug
##### TAGS → demarcando versões
* `git tag -a v0.0.1 -m 'Mensagem explicando a versão do sistema'`
* `git tag -a v0.0.1`
* `git tag --list`
* `git push origin v0.0.1`

### Ignorando arquivos
`.gitignore` → definir arquivos para o git não monitorar 
> Esses arquivos podem ser configurações do ambiente com informações sensíveis (por exemplo, senhas para bancos de dados), pastas criadas pela própria IDE ou editor de texto (aplicações que utilizamos para desenvolver) que contém detalhes do projeto, arquivos de logs gerados pela aplicação, entre outros.

> Por exemplo: imagine que nossa aplicação precise se conectar a um banco de dados, isto é, um sistema utilizado para armazenar e consultar informações. É uma boa prática criar um arquivo chamado .env e colocar as credenciais de acesso lá - o que chamamos de variáveis de ambiente. Além disso, assuma que ela gera vários logs de execução e erros na pasta logs/.

***
### Arquivos/linguagens de marcação
##### Sintaxes que adicionam contexto e informações aos dados brutos que estão sendo passados
* __XML:__ eXtensible Markup Language → linguagem de marcação extensível 
Mais antigo, utilizado na década de 90/2000 para fazer a comunicação entre sistemas, muito grande e complexo de ler, dificultava para absorver o conteúdo, ocupava muito largura de rede
  * extensão: `.xml`
* __JSON:__ JavaScript Object Notations → notação de objetos JavaScript
Veio para substituir o XML; estrutura de chave valor
  * extensão: `.json`
  * Utilizado: padrão da web de comunicação, criação de IaC
* __YAML:__ Yet Another Markup Language → mais uma linguagem de marcação →→ YAML Ain't Markup Language → YAML não é uma linguagem de marcação
  * extensões: `.yaml` (recomendada oficialmente) ou `.yml`
  * Utilizado: padronizção de arquivos e criação de recursos via IaC (terraform, cloudformation, kubernetes)
  * Não utilizado: comunicação entre serviços; na elaboração do contrato até é usado, mas para enviar e receber informações é raro (JSON é usado nesse caso)

>__IaC:__ infra as a code

***

#### Database / Banco de dados:
* utilizado para armazenar e consultar informações

#### Back-end:
* conecta com o banco de dados por meio do CRUD (create, read, update, delete)
* disponibiliza um servior web expondo uma aplicação / uma API (Rest...) / um endpoint → rodando na porta X (ex: 8080) com protocolo X (ex: HTTP)
* armazena os dados no database
* deve expor os dados do database de forma segura (algumas informações são sensíveis)

#### Front-end:
* consome a API, os dados 
* renderiza os dados em uma tela/interface

__API (Application Programming Interface)__
→ significa que vai pegar uma informação de um ponto e irá expor em outro ponto, por meio de um contrato / via protocolo (HTTP...) para ambas as partes conseguirem se comunicar, autenticando quem está requisitando a informação (token) para autorizar ou não

__ENDPOINT:__ ponto final, endereço de um link

__JAVA__
* JRE
* JDK
* JVM - Java Virtual Machine → compila a aplicação

__Biblioteca:__ pedaços de código prontos que pode ser importado para a aplicação para utilizá-la 

__Framework:__ nível mais macro, contém bibliotecas com partes de códigos que poderão ser executados, vai subir um servidor para gerenciar a aplicação (faz essa configuração) → conjunto de bibliotecas e faz a comunicação com o sistema operacional e oferece mais recursos para gerenciar e provisionar a aplicação, vai abstrair muitas informaçãoes para o desenvolvimento da aplicação

##### Métodos que fazem ações/requisições HTTP: 
  * POST: criação
  * GET: consulta
  * PUT: atualização
  * DELETE: exclusão

###### Postman = client HTTP
