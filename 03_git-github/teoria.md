# GIT / GITHUB

### COMANDOS BÁSICOS
* `git init`
* `git add .`
* `git add *`
* `git push origin main`
* `git commit -m "Descrição commit"` -> `-m` é uma flag que aponta para a mensagem de descrição
* `git remote`
* `git remote -v`
* `git remote add origin (ou outro nome) <url>`
* `git remote set-url origin git@github.com:nome_usuario/nome_repositorio.git`
* `git remote remove origin`
* `git checkout nome_branch` / `git switch nome_branch`-> trocar de branch
* `git checkout -b nome_nova_branch` / `git checkout -b nome_nova_branch`-> criar uma nova branch e trocar para ela aparecer 
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



Para fazer alterações/manipulações nos commits:

* RESTORE = alteração que não foi commitada ainda 
* RESET = alteração que foi commitada, permitirá reverter o commit
* REVERT = alteração que foi commitada, mas acaba apagando o histórico de commits
* CHERRY-PICK = 

### BRANCHS COMUNS
* __master / main:__ ambiente produtivo -> EX: portal sem o botão Home
* __homolog:__ ambiente homologação -> EX: portal com o botão Home
* __develop:__ ambiente develop
* __feature:__ desenvolver a sua história

### TAG

*  `git tag -a v0.0.1`
* `git tag --list`
