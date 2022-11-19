# GIT / GITHUB

### COMANDOS BÁSICOS
* `git init`
* `git add .`
* `git add *`
* `git push origin main`
* `git pull`
* `git commit -m "Descrição commit"` -> `-m` é uma flag que aponta para a mensagem de descrição
* `git commit <nome-do-arquivo> -m "Mensagem de alteração"`
* `git commit -am "Descrição commit"`
* `git diff`
* `git restore`
* `git restore --staged`
* `git remote`
* `git remote -v`
* `git remote add origin (ou outro nome) <url>`
* `git remote set-url origin git@github.com:nome_usuario/nome_repositorio.git`
* `git remote remove origin`
* `git checkout nome_branch` / `git switch nome_branch`-> trocar de branch
* `git checkout -b nome_nova_branch` / `git switch -c nome_nova_branch`-> criar uma nova branch e trocar para ela aparecer 
  * [Qual a diferença entre "git switch" e "git checkout"? - Stack Overflow em Português](https://pt.stackoverflow.com/questions/533866/qual-a-diferença-entre-git-switch-e-git-checkout)

__->__ Para criar um novo repositório no GitHub pelo CLI: `gh repo create [<name>] [flags]`
__->__ Para desfazer um commit: `git reset HEAD~1`

#

-m <msg>
--message=<msg>
Use the given <msg> as the commit message. If multiple -m options are given, their values are concatenated as separate paragraphs.

The -m option is mutually exclusive with -c, -C, and -F.
o -m é de mensagem
#

__->__ Para ver o SHA1: git log -> `ls .git/objects`


### Para fazer alterações/manipulações nos commits:
* `git restore` = alteração que não foi commitada ainda / desfazer uma marcação de adição ou remoção de arquivos
* `git reset <sha1-do-commit>` = alteração que foi commitada, permitirá reverter o commit. Git descarta a execução dos commits após aquele especificado, mas mantém suas alterações.
* `git reset --hard <sha1-do-commit>` = Se quisermos realmente descartar as mudanças feitas após aquele commit, devemos informar o parâmetro `--hard`
* `git revert` = alteração que foi commitada, mas acaba apagando o histórico de commits
* CHERRY-PICK = 

### BRANCHS COMUNS
* __master / main:__ ambiente produtivo -> EX: portal sem o botão Home
* __homolog:__ ambiente homologação -> EX: portal com o botão Home
* __develop:__ ambiente develop
* __feature:__ desenvolver a sua história

### TAG

*  `git tag -a v0.0.1`
* `git tag --list`

## REVISÃO

### Git
  Ferramenta de versionamento

### GitHub
  Plataforma de versionamento
  GitHub Pages (documentação)
  Interface gráfica

### Estrutura Git Flow: 
* feature, develop, realese, main, hotfix

commit: entregável, mostra determinado satus do código, snapshot

### Principais comenados:
* `git init`
* `git add .`
* `git commit -m 'Mensagem'` -> tem um hash que dá para buscar pelos primeiros 4/5 dígitos
* `git push origin main`-> enviar o código para o repositório remoto (origin)
* `git pull` -> trazer código do repositório remoto para o local
* `git merge develop main`-> juntar as branchs

### Cliclo de vida do software:
  Alpha, beta, release candidate, GA
  Major, Minor e Path 1.2.5
  `git tag v1.2.5`

`.gitignore`


