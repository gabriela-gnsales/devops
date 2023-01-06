# MÓDULO: CONTEINERIZAÇÃO

 Encapsular as aplicações junto com suas dependências em um único pacote padronizado.

### Container
Isolamento de aplicação, ambiente de execução e contexto, diretamente sobre o kernel.
* aplicação: programa a executar
* ambiente de execução: base de sistema onde vai rodar (arquivos + configurações + serviços)
* contexto: configurações específicas do programa e do ambiente operacional desse programa
**Um processo roda de forma isolada dentro do kernel do sistema operacional.**

Em um container o código da aplicação, junto aos arquivos de configuração, dependências, pacotes e afins são encapsulados em um executável padronizado.

**OBS:** WSL é uma camada do kernel, não uma máquina virtual

### Histórico
* primórdios - BSD jail (kernel baseado no linux), POSIX chroot
* 2008 - lxc rodando no kernel linux (C)
* 2013 - docker (go)
* 2014 - kubernetes (go)
* 2015 / 2017 / 2019 - containerd, runc

### Processo de instalação e configuração do Docker

**Windows:**
* Abrir o terminal e executar `wsl --install`
* Acessar a loja do Windows e instalar o Ubuntu 22.04
* Instalar o Docker: https://docs.docker.com/desktop/install/windows-install/
* Ativar a integração com o WSL do Ubuntu na engrenagem de configuração do Docker com o seguinte processo: clica na engrenagem > resources > WLS Integrations > Enable integration (marcar o checkbox) + marcar integração com as opções que aparecerem abaixo

**Ubuntu:**
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04

### Comandos Docker

##### Rodar o container como aplicação
* `docker run hello-world` → executar um container à partir da imagem "hello-world"
* `docker run pyhon:3.11` → executar um container à partir da imagem "python na versão 3.11"
* `docker run -it pyhon:3.11 python` → executar um container à partir da imagem "python na versão 3.11" de modo interativo
* `docker run -it --name <nome> <imagem>`
* `docker run -it --name <nome> <imagem> <comando>` → executar um comando na imagem
    * ex: `docker run -it --name py_com_shell python:3.11 /bin/bash -c "pip install pandas"`
* `docker run -it --name <nome> --rm <imagem> <comando>` → remover o container após ?

##### Rodar o container como serviço
* `docker run -d <imagem>` → rodar de forma desconectada
    * ex: `docker run -d --name nginx nginx`
* `docker run -d redis:latest` → executar a última versão do redis em backgroud
* `docker run -d -p "porta_local:porta_no_container" <imagem>`
    * ex: `docker run -d -p "8080:80" nginx:latest` → executar um container à partir da imagem "nginx:latest" mapeando a porta 8080 local (seu host) para a porta 80 do container (porta de serviço do nginx)
    * ex: `docker run -d -e POSTGRES_PASSWORD=12345678 -e POSTGRES_USER=ada -e POSTGRES_DB=devas -p 5432:5432 --name pgsql_devas postgres:15`
    * ex: `docker run -d -p 5432:5432 --env-file env.dev --name pgsql_devas_2 postgres:15`

##### Mostrar os containers
* `docker ps -a` → exibir todos os containers existentes (parados os rodando) via CLI (command-line interface)
* `docker ps` → exibir somente os containers ativos via CLI

##### Parar o container
* `docker kill <identificação>`
* `docker stop <identificação>`

##### Excluir o container
* `docker rm <identificação>`

##### Verificar erros
* `docker logs <identificação>`

##### Configurar ambiente
* `docker run -e VARIÁVEL=valor <imagem>`→ definir variáveis de ambientes na criação do container
    * ex: `docker run -it -e AUTHOR="gabriela" -e DATE="20221222" alpine sh`

##### Inspecionar o container
* `docker inspect [ID ou nome do container]` 

### Imagens

Imagens são para um container como uma receita é para um bolo. A imagem de um container contém todas as informações necessárias para que esse container possa ser executado, ou seja, ela inclui o passo a passo completo com todas as especificações e características, bem como alguns scripts que devem ser seguidos no momento de se executar o container. Assim o container é um processo executável provisionado partindo de uma imagem pré-estabelecida.

Uma imagem nada mais é do que um conjunto de arquivos "guia", ou seja, é um template para a criação do container. Imagens são obtidas quando, por meio do docker client, uma solicitação do tipo "build docker" é enviada ao docker daemon e executada. Assim, tendo uma imagem é possível executar um container a partir desta. Cada container só pode subir a partir de uma única imagem, por isso é importante entender o funcionamento do processo de criar e customizar imagens para atender diferentes necessidades.

Existem imagens que são publicadas e mantidas atualizadas pela própria empresa, no caso a docker, e por isso são nomeadas **imagens oficiais**. Essas imagens garantem requisitos básicos de segurança e boas práticas e atendem cenários comuns a muitos usuários.

* `docker images`
* `docker image ls` → visualizar as imagens disponíveis para serem utilizadas
* `docker build -t <nome dono>/<nome imagem>:<tag - opcional> .` → o ponto significa para criar a imagem no diretório local
> Este comando enviará ao docker daemon a instrução de criar uma nova imagem a partir do Dockerfile existente no diretório onde a instrução é enviada, essa especificação do local onde o Dockerfile se encontra é dada pelo ponto no final do comando. Essa imagem ficará com a identificação de nome de imagem, tag e nome do dono da imagem conforme especificado no comando.

> Formato do nome da imagem: `owner/image_name:version`
> `latest`: versão padrão / última versão

Uma imagem Docker é construída por meio do uso de um arquivo chamado **Docker File** e é armazenada em um **Docker Hub** ou em um **repositório**.

##### Dockerfile:
** Sequência de comandos/instruções para construir uma imagem.**
* `FROM <image>:<tag>` →  primeira instrução informando a partir de qual imagem base o container deve subir
> As tags nas imagens são marcações usualmente utilizadas para versionamento das imagens, elas possibilitam que diferentes versões de uma mesma imagem possam coexistir em um repositório e serem utilizadas conforme a necessidade do cliente.
* `RUN ...` → criar a pasta
* WORKDIR → criar diretório de trabalho
* COPY → copiar arquivos da máquina
* ADD → consegue adicionar no container um repositório git
* RUN → 
* ENV → configurar variáveis de ambiente (não recomendado)
* EXPOSE → expor a porta (apenas informa para o usuário mapeá-la corretamente)
* CMD →
* ENTRYPOINT → 

> **Diferença CMD e ENTRYPOINT**
> O CMD defini como a imagem vai rodar, já o ENTRYPOINT não.
> O Dockerfile só pode ter um dos dois e eles têm que ser o último comando.

### Docker Registry e Docker Hub

O Docker Registry é um serviço open source usado para armazenar e distribuir imagens Docker. Por meio desse serviço múltiplos usuários podem ter acesso a imagens customizadas feitas por outros usuários. A interface do serviço possibilita um trabalho mais colaborativo e simplifica o processo de transferir imagens de um indivíduo para o outro.

De forma semelhante, o Docker Hub é a ferramenta padrão da própria empresa Docker para esta mesma função. Ou seja, no momento de compartilhar imagens é possível escolher a ferramenta de registro que mais se adequa ao cenário da sua empresa ou projeto. É possível também criar repositórios privados para imagens que precisam ser compartilhadas, mas não publicamente.

A comunicação entre o Docker Client e o Docker Registry é feita por meio de comandos de `pull` e `push`.

* `docker pull <image>:<tag>` → buscar uma determinada imagem em um repositório Docker
	 * ex: `docker pull pyhon:3.11` → para baixar a imagem para o docker local (pull)
* `docker push <image>:<tag>` → disponibilizar no repositório as alterações feitas

### Volumes Docker

Um volume Docker é sempre gerenciado pelo Docker host (o Docker Daemon), a única função do usuário é criar ou destruir o volume conforme necessário e, em casos específicos, realizar um mapeamento dentro do container para o volume. 

* `docker volume create [OPTIONS] [VOLUME]` → criar um volume docker
* `docker volume ls [OPTIONS]` → listar volumes
* `docker volume inspect [OPTIONS] VOLUME [VOLUME...]` → inspecionar volumes
