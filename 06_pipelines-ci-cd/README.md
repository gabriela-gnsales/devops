# MÓDULO: PIPELINES DE CI E CD

#### Código
Todo código desenvolvido precisa ser armazenado, rastreável, disponibilizado de forma que diversas pessoas possam contribuir para que o ciclo de vida seja o mais longo possível e a manutenção possa acontecer de forma facilitada.

#### Organização de repositórios
Controladores de versão com GIT, SVN são úteis  nesse processo, onde também podemos usar ferramentas na nuvem para armazenar os códigos desenvolvidos de forma visual e integrada com os protocolos mais famosos.

#### Termos importantes
**Build:** Construir artefatos com suas dependências, a partir de código desenvolvido.
**Steps:** Divisão de processos por tipo - exemplo: Checkout.
**Jobs:** Tarefas que podem ser executadas para complementar o processo de construção, entre outros.
**Environments:** Divisão de ambientes por contexto, como produção, desenvolvimento.
**Test:** Processo de validação e checagem de saúde do código.
**Deploy:** Processo de implantação do código após a parte de integração.

#### Pipelines
Pipelines são como esteiras de código, tal qual uma linha de montagem com diversos steps, processos de checagem para garantir a qualidade do nosso produto: **o Código Produtivo**.
Esteiras com diversos passos que geram artefatos.

*Pipelines* de **Continuous Integration** e **Continuous Delivery**, ou *pipelines* de **Integração e *Entrega Contínua** consiste uma esteira de passos, etapas em que o código passará até chegar a sua versão final em ambiente de produção.

A prática da execução de pipelines e automações, são um dos principais pilares da cultura DevOps e da abordagem SRE. O principal objetivo dessas etapas é acelerar o processo de entrega de software, ou seja, quanto mais rápida uma nova versão fica disponível, mais veloz os usuários desse software poderão usufruir dos novos recursos.

**Tópicos da Pipeline:**
* **Compilação:** estágio em que a aplicação é compilada;
* **Teste:** estágio em que o código é testado. Aqui, a automação poupa tempo e esforço;
* **Lançamento:** quando a aplicação é enviada ao repositório;
* **Implantação:** o código é implantado no ambiente de produção;
* **Validação e conformidade:** é possível usar ferramentas de verificação da segurança de imagens, como o Clair, para ter certeza da qualidade das imagens ao compará-las com vulnerabilidades (CVEs) conhecidas.

#### Ferramentas de integração contínua
Jenkins, GitLab CI, GitHub Actions, Argocd, CircleCI...

#### Integração contínua
Uma forma de gerar código produtivo de forma automatizada.
Trata-se de um sistema integrado e contínuo, ou seja, algo que precisa ser configurado uma única vez, e logo em seguida pode ser usado contínuamente fazendo as etapas manuais de forma total ou parcialmente automatizada.

#### Build automatizado
Podemos construir artefatos sem precisarmos de um time especializado para isso através de ferramentas.
Cada artefato possui uma identificação que facilita o desenvolvimento e controle de versões a cada incremento de software, podemos voltar ou avançar versões conforme necessário.
Uma dos últimos estágios do desenvolvimento de software é o build. Em linhas gerais, o build é processo de empacotamento da aplicação, deixando-a pronta para o deploy nos ambientes, ou a deixando pronta para instalação e utilização por outros usuários.
Em outras palavras, build é a construção e definição dos mecanismos e processos de instalação. Ao contruir um build, podemos ter como resultados executáveis, bibliotecas, arquivos ou pacotes, como por exemplo: exe, msi, dll, lib, deb, rar, jar, war, entre outros.
Partindo da premissa que todo processo manual pode ser automatizado, tornar o processo de build automático pode gerar uma boa economia de tempo, além de manter um padrão, reduzindo erros.

#### Deploy
Processo/ato de levar o resultado do build de um local isolado para um ambiente em produção.
Deploy é um dos termos amplamente utilizados por desenvoldores de software e outros profissionais de tecnologia. O conceito diz respeito a prática de implantação, quando tornamos uma funcionalidade ou uma nova versão do sistema disponível para a utilização dos usuários.
Toda site, sistema, aplicativo, atualizações lançadas que estão atualmente funcionando, passaram de alguma forma pelo processo de deploy, seja ele automático ou manual. Quando pegamos, por exemplo, o código que estava localmente na máquina do desenvolvedor e jogamos para um servidor Web, estamos fazendo o deploy, ou a implantação de uma aplicação.

#### Rollback
Processo que consiste em voltar para versões anteriores de forma a manter a saúde do seu ecossistema de aplicações e serviços.

#### Entrega contínua
Quando escolhemos se um artefato pronto vai ou não para produção.
Processo de implantação dó código após ter passado por uma esteira de testes, validações e outros processos que criam versões prontas para estarem disponíveis em ambientes produtivos. Isso facilita que possamos lançar novas funções e melhorar a experiência do usuário de forma controlada.

**Modelo Trunk Based:** modelo baseado em tronco; branches são mergeadas na principal

## Jenkins
Doc Oficial: https://www.jenkins.io/doc/
Jenkins é uma ferramenta bastante utilizada e madura para realizar integração contínua, possuindo diversos plugins e sendo Open Source, o que facilitou mais a sua adoção por diversas empresas.
O Jenkins gerencia e controla o processo de entrega de software durante todo o ciclo de vida, incluindo compilação, documentação, teste, empacotamento, preparação, implantação, análise de código estático e muito mais.
O Jenkins pode ser configurado para monitorar qualquer alteração de código em locais como GitHub, Bitbucket ou GitLab e automatizar compilações usando ferramentas como o Maven. Você pode aproveitar tecnologias de contêiner como Docker e Kubernetes para iniciar os testes e, em seguida, realizar operações como rollback ou rollforward em ambiente produtivo.
Por questões de segurança do próprio Jenkins, um `hash` é gerado em cada nova instalação.
Jenkins se tornou popular por ter sido uma das primeiras ferramentas de integração contínua mais robustas (o projeto surgiu em 2004), o que fez com que muitas empresas passassem a utilizá-lo. Hoje em dia temos mais opções como Gitlab CI, CodePipeline, Bitbucket Pipeline, CircleCi e etc.

#### Componentes Jenkins
**Agent** - Ajuda a execução de jobs em diversos locais como clouds, servidores locais entre outros
**Build** - Processo de construção de artefatos a partir de steps pré-definidos que podem incluir testes, geração de imagens, entre outros.
**Jobs** - São as execuções que ocorrem após a configuração dos steps pré-definidos
**Pipelines** - É a composição de passos para validarmos código, escolhermos de onde o código será incluído, bem como scripts, relatórios e outros componentes
**Plugins** - São extensões do Jenkins, geralmente utilizadas para facilitar integrações com outras ferramentas e serviços. Ex: Integração com AWS

#### Plugins
Os plugins são bastante importantes no Jenkins, eles funcionam como pequenas ferramentas dentro do Jenkins.
Existe uma vasta gama de plugins no Jenkins que podem ser usados para as mais variadas funções, como por exempo: notificações de Jobs, deploy de linguagens específicas, integração com ferramentas de análise de código e testes unitários, entre outros.
Podemos ter vários plugins instalados, porém, por questões de segurança, é uma boa prática observar se eles estão sendo atualizados com frequência e não deixar de atualizá-los.

#### Job
Um Job no Jenkins é toda atividade automatizada.
Existem, atualmente 6 tipos de Jobs que podem ser criados no Jenkins, são eles:
* **Estilo Livre** - O estilo mais antigo do Jenkins, com ele, podemos criar diversos tipos de automações, integrar com repositórios e até utilizar de forma flexível com os inúmeros plugins existentes na base do Jenkins.
* **Pipeline** - Esse tipo é usado para criar automações mais complexas, permite um nível de flexibilidade maior que o estilo livre.
* **Multiplas Configurações** - Funciona como um Job estilo livre, porém, é bastante recomendado para projetos que necessitam de um número variado de configurações, como por exemplo, teste em mais de um ambiente.
* **Folder** - É um recurso que possibilita a organização de Jobs em estruturas de pastas.
* **Multibranch Pipeline** - Esse estilo de Job faz uma análise de repositórios e gera automaticamente um Job para cada branch encontrado no repositório analisado.
* **Organization Folder** - Cria um conjunto de subpastas e várias ramificações verificando repositórios.

O tipo de Jobs mais apropriado depende da necessidade e das particularidades de cada projeto.

#### Comandos Jenkins

**1.** Criar um volume jenkins 
* `docker volume create jenkins-data`
* `docker volume inspect jenkins-data` → consultar e verificar se o volume foi realmente criado

**2.** Rodar o container
`docker container run --name jenkins --restart always --detach --privileged --volume jenkins-data:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts`
    * `–restart=always` → reiniciar o container em caso de falha
    * `-p 8080:8080` → define a porta do host para o container (porta que vai rodar)
    * `-p 50000:50000` → define a porta para escutar o agent (via protocolo JNLP)
    * `-u 0` → ID do usuário root para executar o container
    * `-v jenkins_home:/var/jenkins_home` → monta o volume persistente

**3.** Abrir o console do jenkins via bash para pegar a senha do admin
* `docker exec -ti <parte do hash> bash`
   `cat /var/jenkins_home/secrets/initialAdminPassword`
* `docker container exec <parte do hash> cat /var/jenkins_home/secrets/initialAdminPassword`
* `docker logs <nome container>`

**4.** Instalar plugin *blue ocean*

**5.** Criar tarefa (pipeline) do tipo *Construir um software de estilo livre*
* Incluir um repositório qualquer em código fonte e especificar o nome da branch (Gerenciamento de código fonte → Git)
* Incluir para rodar a cada 5 min (Gatilho de disparo para construções → Consultar periodicamente o SCM): `H/15 * * * *`
* Incluir um script (Passos de construção → Executar shell): `echo "${BUILD_NUMBER}" && echo "${GIT_BRANCH}"`
* Explorar outros componentes que podem ser utilizados

**6.** Criar nó (Agent)
* Configurações:
    * Nome: nodejenkins
    * Tipo: agente permanente
    * Número de executores: 1
    * Diretório raiz remoto: .
    * Método de lançamento: lançar um agente conectando-o ao controlador
    * Diretório de dados internos: remoting
* Pegar senha (secret) no comando *Executar da linha de comando do agente*
* `docker inspect <nome ou id do container jenkins>` → consultar o endereço IP do jenkins
    * `docker inspect jenkins`
* `docker run -d --init jenkins/inbound-agent -url http://endereçodojenkins:8080 <hash senha> <nome nó>`
    * `docker run -d --init jenkins/inbound-agent -url http://172.17.0.2:8080 ccdd81a07d22a5d3dbf19ccc89ad0843ec9ab5f448feeba1cd37d0d5cd95878e nodejenkins`

**7.** Desafio
* Descobrir como deixar a saída da mensagem de erro/sucesso (output) do Jenkins colorida
    * Install AnsiColor plugin On Jenkins: Manage Jenkins > Manage Plugins > Available > search and install 'Ansi Color'
    * Configure your build/job Under Build Environment section check Color ANSI Console Output and select xterm
        * Ambiente de construção → Color ANSI Console Output → ANSI color map: xterm
    * Inside Execute shell step add something like:
    ```
        set +x
        info() {
        echo "\033[1;33m[Info]    \033[0m $1"
        }

        error() {
        echo "\033[1;31m[Error]   \033[0m $1"
        }


        success() {
        echo "\033[1;32m[Success] \033[0m $1"
        }


        info "This is information message"
        error "Houston we have a problem"
        success "Great!!!"

        echo "Foreground colors"
        echo "\033[31m Red \033[0m"
        echo "\033[32m Green \033[0m"
        echo "\033[33m Yellow \033[0m"
        echo "\033[34m Blue \033[0m"
        echo "\033[35m Magneta \033[0m"
        echo "\033[36m Cyan \033[0m"
        echo "Background colors"
        echo "\033[41m Red \033[0m"
        echo "\033[42m Green \033[0m"
        echo "\033[43m Yellow \033[0m"
        echo "\033[44m Blue \033[0m"
        echo "\033[45m Magneta \033[0m"
        echo "\033[46m Cyan \033[0m"
        echo "Different combinations"
        echo "\033[1;31m Red \033[0m"
        echo "\033[1;4;37;42m Green \033[0m"
        echo "\033[1;43m Yellow \033[0m"
        set -x
    ```