# GIT / GITHUB

### Git
  Ferramenta/sistema de versionamento e monitoramento de código
  * aponta para a branch atual → `cat .git/HEAD`
  * onde está apontando uma branch para o respectivo commit → `cd .git/refs`
  * onde os arquivos estão sendo salvos, de forma compactada → pasta `cd .git/objects`

### GitHub / GitLab / Bitbucket / AWS CodeCommit ...
##### Plataformas de versionamento, de forma distribuída, centralizada e global
* GitHub é o mais utilizado → centraliza os principais códigos OpenSource
* GitHub Pages (documentação)
* Interface gráfica

### Estrutura Git Flow: 
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
* `git merge develop main` → juntar as branchs, necessitando resolver conflitos em alguns casos
* `git diff` → para exibir as alterações nos arquivos antes de realizar o comando `git add .`

> -m <msg>
> --message=<msg>
> Use the given <msg> as the commit message. If multiple -m options are given, their values are concatenated as separate paragraphs.
> The -m option is mutually exclusive with -c, -C, and -F.

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

### Comandos para desfazer modificações / fazer alterações e manipulações nos commits:
* `git restore <caminho (no caso de um arquivo que foi excluído de uma pasta) ou arquivo a ser restaurado>` → para desfazer uma alteração que não foi commitada ainda / desfazer uma marcação de adição ou remoção de arquivos
* `git restore --staged` → para reverter um arquivo que foi adicionado ou removido acidentalmente depois do `git add .` → para torná-lo untracked (não rastreado pelo git)
* `git reset <sha1-do-commit>` = alteração que foi commitada, permitirá reverter o commit. Git descarta a execução dos commits após aquele especificado, mas mantém suas alterações.
* `git reset --hard <sha1-do-commit>` = Se quisermos realmente descartar as mudanças feitas após aquele commit, devemos informar o parâmetro `--hard`
* `git revert` = alteração que foi commitada, mas acaba apagando o histórico de commits
* CHERRY-PICK = 

➡ Para criar um novo repositório no GitHub pelo CLI: `gh repo create [<name>] [flags]`
➡ Para desfazer um commit: `git reset HEAD~1`
➡ Para ver o SHA1: git log → `ls .git/objects`

* __PR (pull request):__ requisição para fazer o merge de 2 branchs
* __clone do repositório:__ clono o repositório para minha máquina e fica isolado do repositório raiz/origem
* __fork do repositório:__ clono o repositório para minha máquina e fica atrelado ao repositório raiz/origem, sinzronizado, podendo mandar uma PR → funcionamento do OpenSource

__OpenSource:__ plataforma aberta, código público → é possível ler a estrutura do código, alterá-la e repassar/recompartilhar com a alteração; projeto que a comunidade contribui; 2 instituições fundamentais nesse processo:
* Linux Foundation
* CNCF - Cloud Native Computing Foundation 

### Ciclo de vida do software:
* Alpha, beta, release candidate, GA (general available)
  * __Major:__ quando há uma quebra de compatibilidade da aplicação com a versão anterior
  * __Minor:__ alteração que acrescenta uma feature nova, mas mantém a compatibilidade
  * __Path:__ correção de bug
##### TAG
* `git tag -a v0.0.1`
* `git tag --list`
* `git tag v1.2.5`

`.gitignore` → definir arquivos para o git não monitorar 

__IaC:__ infra as a code

### Arquivos de marcação
* __XML:__ mais antigo, utilizado na década de 90/2000 para fazer a comunicação entre sistemas, muito grande e complexo de ler, dificultava para absorver o conteúdo, ocupava muito largura de rede
* __JSON:__ veio para substituir o XML; estrutura de chave valor
  * Utilizado: padrão da web de comunicação, criação de IaC
  * Não utilizado:
* XML
* __YAML:__
  * Utilizado: padronizção de arquivos e criação de recursos via IaC (terraform, cloudformation, kubernetes)
  * Não utilizado: comunicação entre serviços; na elaboração do contrato até é usado, mas para enviar e receber informações é raro (JSON é usado nesse caso)

***

#### Database / Banco de dados:
* faz o armazenamento das informações/dados

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
