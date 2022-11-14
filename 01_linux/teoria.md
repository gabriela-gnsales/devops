# LINUX

SOFTWARE: aquilo que não é palpável, parte lógica, digital
HARDWARE: parte palpável - gabinete, monitor, mouse, teclado, caixa de som...

GABINETE: onde está armazenado toda a plataforma de hardware: fonte de energia, drive de DVD/CD, placa-mãe, processador, memória, placa de vídeo, placa de som, disco rígido, leitor interno

infos de entrada: pelo teclado, por exemplo
infos de saída: exibição na tela/monitor

PLACA-MÃE: onde tá tudo plugado para ser executado, hardware onde tá a CPU, memória, onde liga cabos

MEMÓRIA RAM: volátil, não armazena os dados depois que o computador é desligado, só armazena temporariamente enquanto as tarefas são executadas 
* função de manter os dados em processamento, armazena os dados em tempo de execução, é medida em Hertz, muito importante para sistemas complexos (ex: SAP, sistema de gerenciamento de CRM ?) onde tem um consumo muito grande (muita coisa sendo rodada, processamento em paralelo)
* ela tem dentes, ela é plugada na placa-mãe, algumas de notebook são removíveis e outras não
* memória de ESCRITA e de LEITURA

------------------
Para falar de SAP precisamos falar brevemente sobre ERP, sistema integrado de gestão empresarial. O ERP tem como função principal integrar todas as áreas de uma empresa: logística, contabilidade, vendas, fiscal, contabilidade e outras. O sistema SAP é um tipo de ERP.
SAP é a abreviação da expressão em alemão ‘Systeme, Anwendungen und Produkte in der Datenverarbeitung’, traduzido como Sistemas, Aplicativos e Produtos para Processamento de Dados. A expressão em alemão tem um motivo: o sistema foi desenvolvido por uma empresa alemã, líder no segmento de software corporativos

Ele nada mais é que um sistema que ajuda a gerenciar os dados das empresas. Por exemplo, gerencia se a empresa tem estoque, materiais, produtos. Então, tudo que engloba os processos empresariais, o SAP auxilia a administrar.
------------------

MEMÓRIA ROM:
* não é um pente como a memória RAM, diferença física
* vem mais enraizada na placa-mãe
* é APENAS DE LEITURA, não serve para escrever algo nela (não é para pegar info. do servidor e escrever nela)
* memória de inicialização, onde está escrito pelo fornecedor infos. para o S.O. subir
* colocamos o sistema para ligar, ele começa a fazer a inicialização, conecta com a placa-mãe, verifica quais dispositivos/periféricos estão conectados (HD, memória RAM, processador...)

BIOS (basic input output system): é a memória ROM
* sistema que coordena a inicialização, verifica se a memória / o pulso elétrico tá plugado
* a BIOS "diz" para um computador que ele é um computador

CPU (Central Processing Unit = Unidade de Processamento Central) - PROCESSADOR:
* é um chip, a parte mais inteligente, cérebro
* parte que faz todos os processos, PID, tarefas
* faz a orquestração do fluxo de tarefas
* velocidade no clock (giro, volta)
* quanto mais rápido um processador for, mais clocks/execuções ele consegue fazer
* melhores atualmente: AMD e INTEL
* os processadores se conectam com o S.O. através de um DRIVER (programa que vai permitir a conexão entre o seu dispositivo / hardware e o seu S.O.)

HD (hard disk - disco sólido): memória sólida
* salva os dados em repouso, mantém os dados enquanto o computador tá ligado e desligado
* é composto de discos e um cabeçote com agulha
* o dado é escrito no disco de forma MAGNÉTICA
* rotaciona o disco e escreve em algum ponto do disco
* os dados são segmentados no disco, tanto para escrita quanto para leitura
* PONTOS NEGATIVOS / VULNERABILIDADE: fragilidade, é muito sensível e barulhento
* PONTOS POSITIVOS: barato, consegue armazenar os dados por uma duração maior que o SSD

SSD (solid state drive)
* não tem disco, é mais compacto, sua estrutura é parecida com a da memória RAM
* salva dados em chip
* memória flash
* PONTOS NEGATIVOS: é mais caro e a vida útil é menor que do HD
* PONTOS POSITIVOS: é mais seguro que o HD, em relação a quedas..., é dedicado para ambientes de situação crítica (em que as operações não podem parar, ex: bancos, hospitais...), não é barulhento

FIRMWARE: interface gráfica para acessar um hardware específico / sistema embarcado do roteador / modem
* interface gráfica direta / específica para um hardware

SISTEMA EMBARCADO: aquele sist. que já vem junto com o hardware, sistemas de IOT (internet das coisas)
ex: roteador, sensor de chuva, sensor de temperatura, sensor de estacionamento, arduino

KERNEL
linux é o kernel do sistema operacional (SO) do GNU
cérebro inteligente que faz a gestão/orquestração dos processos e faz a comunicação com o hardware (os periféricos), ele que dimensiona quanto de processamento e memória o usuário vai precisar em cada tarefa, transformando nossos comandos em instrução de máquina (0 ou 1)
a comunicação sempre vai ser um pulso elétrico: 1 = sinal de energia
quem faz a comunicação/conversão da imagem para o 0/1 ou ao contrário é o kernel
EX: se o usuário quer abrir uma planilha, o kernel emite um comando para o processador criar um processo para abrir a planilha, esse processo vai precisar ir no HD ou no SSD buscar essa planilha e armazenar na memória RAM e, quanto estiver na memória RAM,  vai abrir a planilha pra executar

ENIAC: década de 40 -> fazia equações matemáticas

MAINFRAME: computadores gigantescos de alto processamento
* utilizado somente nas grandes empresas, a IBM é a mãe do mainframe
* ainda é utilizado pelas empresas, mas estão migrando para cloud
* as provedoras de cloud tbm utilizam mainframe

UNIX: primeiro sistema, S.O. mãe
permitiu que conseguíssemos gerir multi usuários, permitir que tivesse várias conexões, fazer vários processos em paralelo, que é uma arquitetura clássica de servidor
* a tela preta / shell surgiu com o UNIX
* foi desenvolvido em assembly e depois foi reescrito em C

SERVIDOR: local para fazer uma conexão, pegar uma informação, armazenar um dado... de forma CENTRALIZADA, pensar em centralização
local que disponibiliza serviços
conjunto de serviços que vai oferecer alguma solução para determinado problema

LINUX: kernel

GNU: sistema que utiliza o kernel do linux, não é UNIX, pq não é pago, é free

S.O. é um conjunto de pacotes

DEBIAN: conhecido pela sua estabilidade, confiável, é indicado para servidores, empresas optam por ele

UBUNTU: muito utilizado pelo usuário final, fácil curva de aprendizagem, muito parecido com o windows, é baseado no DEBIAN

KALI LINUX: utilizado pelos hackers para fazer testes, atacar, para explorar vulnerabilidades

VERSÃO SERVER x VERSÃO CLIENT
a versão server conta com mais recursos e pacotes diferenciados, é utilizada na instação de ambeintes corporativos
versão cliente é destinada para o usuário final
é comum o usuário instalar uma interface gráfica na versão client, pq dá uma visão melhor de como é o sistema
mas na server não, pois a interface pesa muito na instalação e na execução do sistema, por isso é deixada apenas a tela preta para manter a performance do sistema a mais alta possível

VERSÃO LTS (long time suport) - recebe atualizações até 5 anos, uma nova versão do sistema é lançada a cada 2 anos

SERVIDOR
* ideia de centralização de uma informação -> informação que está centralizada em um local e eu posso conectar com ela, acessá-la, editá-la
* servidor oferece um serviço (ex: de sistemas de arquivos FTP, serviço web (sites), servidor de hora NTP (para compartilhar uma hora, centraliá-la -> muito importante para evitar vulnerabilidade a um ataque)
tipos de servidores: torre, rack ou nuvem

SERVIDOR BARE METAL: servidor puro/novo (que não tem nenhum SO) e será feita a instalação de um SO, pra isso é preciso ter a imagem (arquivo .iso) do SO, colocar em um CD ou pen-drive, configurar a BIOS (sistema base de entrada e saída) pra fazer a inicializaçõa por essa mídia removível, dá pra fazer via rede tbm

como alternativa/forma de mudar a operação -> virtualização através de um HYPERVISOR (software com função de SO, que permite rodar várias máquinas virtuais (ubuntu, mac, windows...), permite criar máquinas diferentes do sistema origem/host, ele quebra/divide a memória e processamento da máquina pra cada SO
* principais hypervisor utilizados no mercado: VMware Workstation, VMware vSphere (+ nível enterprise), Virtual Box (da Oracle), Hyper-V (nativo da Microsoft), Citrix

HYPERVISOR tipo 1 / nativo / mare metal: instala direto no harware 
HYPERVISOR tipo 2: instala em cima do SO host da máquina

AWS: maior provedora de cloud do mundo, líder do mercado

COMANDOS LINUX

/ significa diretório raiz do SO linux, diretório mais importante

cd /
bash

manual dos comandos: man comando (ex: man ls)

manual dos comandos: MAN COMANDO

cd --help

sudo apt update
apt install vim
sudo apt install vim

SUDO é um comando que você invoca pra dizer que voce é administrador do sistema
SUDO é uma forma de informar ao sistema que você deseja logar com o usuário ROOT
abreviação pra "super user do"

sudo -i -> #root = super usuário, tomar cuidado com os comandos

ROOT: usuário super administrador no linux, que consegue/tem permissão para fazer TUDO no sistema -> CUIDADO 
comando 'sudo -i' vai para o ROOT (#)
para sair digitar 'exit'

UPGRADE vs UPDATE - rever aula 21:25

comando source perdi

ssm = session manager

se for para criar uma pasta com nome com espaços, tipo: nome da pasta, usem aspas ou aspas simples, senão ele cria uma pasta para cada palavra

nano / etc/apt/sources.list -> arquivo que o sistema busca quando vai fazer o update

UPDATE: atualiza a lista de repositórios
UPGRADE: vai pegar a lista atualizada e vai atualizar o sistema, um arquivo que esteja desatualizado, demora um pouco mais, diz quato de memória vai precisar

APT (Advanced Packaging Tool): gerenciador de pacotes e dependências no Ubuntu

VIM: editor de textos via linha de comando
p/ começar a editar o vim: digitar a letra 'i' de insert
p/ sair e salvar o arquivo: digitar :wq
só para sair (sem salvar): :q!

PWD (print working directory): exibe qual é o diretório atual

CD (change directory): altera o diretório onde você está trabalhando na linha de comando

LS (list)
ls = Lista os arquivos não ocultos;
ls -a = Lista os arquivos visíveis e também os ocultos;
ls -l = Lista os arquivos em formato de lista mostrando o dono do arquivo e sua data de criação;
ls -la = A mesma exibição do ls -l acrescentando os arquivos ocultos.
ls -lah = mostra o tamanho do arquivo de forma mais intuitiva

CP (copy): realiza a cópia de um arquivo. Necessário informar o arquivo origem da cópia e o nome do arquivo de destino que será criado | ex: cp arquivo-origem arquivo-copia

MKDIR (make directory): cria um diretório/pasta

RM (remove): remove arquivos e diretórios. Pode-se utilizar os parâmetros -rf para forçar uma deleção recursiva dos arquivos dentro de um diretório
REMOVER DIRETÓRIO: rm -r nome_diretório

ZIP: compacta os arquivos usando o ZIP | ex: zip arquivo.zip nome-arquivo
unzip

TAR
Compacta os arquivos usando o TAR. Essa é a forma mais utilizada de compactação pois consegue comprimir o arquivo com um menor tamanho comparado ao Zip. Os parâmetros usados são listados abaixo:

tar -cvf diretorio.tar diretorio/  Compacta
tar -xvf diretorio.tar Descompacta
c – cria um novo arquivo .tar
v – mostra uma descrição do progresso de compactação
f – nome do arquivo.

GZIP
Compacta os arquivos usando o GZIP. Ele é muito semelhante ao TAR e inclusive pode ser utilizado junto com ele. Os parâmetros usados são listados abaixo:

gzip nome_arquivo  
Irá gerar um arquivo compactado e apagar a versão não compactada, caso queira manter a versão original utilizar o comando:

gzip -k nome_arquivo
Para descomprimir um arquivo, basta utilizar o comando:

gzip -d nome_arquivo.gz

printenv: para encontrar as variáveis existentes no Ubuntu basta aplicar o comando

Quando há a necessidade de realizar buscas no sistema, é possível utilizar a junção de duas técnicas: Grep e Expressões regulares.

	⁃	sudo -i
	⁃	sudo su
	
	o sudo atribui poderes de admin. enquanto que o su troca para o usuário admin.

--------------

aperta ESC
depois SHIFT :
e ai digita
:q!

-------------------------------------
#l/bin/bash

sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
-------------------------------------

o bash mostra "usuario@maquina:diretorio$" enquanto o sh mostra só "$"

Lembre-se de executar os comandos como usuário comum e não como root, visto que, como root tudo será aceito e, dependendo do que você fizer, isto pode gerar danos ao sistema operacional. Uma maneira fácil de verificar é abrir o terminal e se o símbolo antes do cursor é o $, você está como usuário comum, mas se é o #, você está como root. Para sair do modo root, digite EXIT

No Linux e em outros sistemas semelhantes ao Unix, você tem várias opções de shells.

O shell é responsável não apenas por desenhar o seu pequeno prompt, mas também por interpretar seus comandos, especialmente se você colocar uma lógica complicada como pipes, condicionais e assim por diante.

bash é o shell mais comum, usado como shell padrão para usuários de sistemas Linux . É um descendente espiritual de outros shells usados em toda a história do Unix. Seu nome, bash é uma abreviatura de Bourne-Again Shell, uma homenagem ao shell Bourne que foi projetado para substituir, embora também incorpore recursos do C Shell e do Korn Shell.

Ele é executado, atualmente, em /bin/bash - qualquer sistema com o bash o terá acessível aqui.

-----

Shell é um programa que controla sistemas operacionais, inclusive em hospedagens gerenciadas, por meio de uma GUI (Graphical User Interface ou interface gráfica do usuário) ou de uma CLI (Command Line Interface ou interface de linha de comando).

Shells GUI estão presentes, por exemplo, no Windows 10 — permite que os usuários controlem o sistema operacional do dispositivo acionando botões na barra de tarefas e em menus. Entretanto, o bash é um shells CLI e, para funcionar, necessita que o usuário escreva comandos em consoles e ambientes de desenvolvimento integrado (IDEs), assim como é feito com outras linguagens de programação. O software, então, busca nomes de diretórios, de arquivos e de programas para atender a intenção do usuário.

----

/etc/shadow : onde estão as senhas criptografadas


apt list | grep -i "python"

/home/$USER/.local/share/Trash
/home/nome_do_seu_usuario

----------

USUÁRIO:
de serviço: que são utilizados nos servidores
de sistema: que administram o sistema

USUÁRIOS COM PERMISSÃO DE LOGIN: final: /bin/bash
USUÁRIOS SEM PERMISSÃO DE LOGIN: final: nologin OU /bin/false
TIRAR PERMISSÃO DO USUÁRIO DE FAZER LOGIN: sudo usermod -s /bin/false nome_usuario

ADCIONAR USUÁRIO:
useradd: sem colocar os parâmetros
adduser: adicionando os parâmetros

ADICIONAR USUÁRIO AO GRUPO SUDO:
sudo gpasswd -a nome_usuario sudo
sudo adduser nome_usuario sudo

ADICIONAR GRUPO: addgroup nome_grupo
APAGAR GRUPO: delgroup nome_grupo

APAGAR USUÁRIO: deluser -d nome_usuario
APAGAR USUÁRIO DO GRUPO SUDO: deluser nome_usuario sudo

VER QUAIS USUÁRIOS ESTÃO NO GRUPO SUDO: cat /etc/group | grep sudo

PESQUISAR DADOS USUÁRIO:
cat /etc/passwd | grep nome_usuario
EX: cat /etc/passwd | grep gabriela
retorno: gabriela:x:1000:1000:,,,:/home/gabriela:/bin/bash
o 'x' é o campo da senha, que está criptografada pelo S.O.
depois é o nº do ID do usuário
depois o ID do grupo
depois informações do usuário
depois diretório do usuário
depois o shell de login

VER SENHAS CRIPTOGRAFADAS: cat /etc/shadow
VER GRUPOS: cat /etc/group

ALTERAR SENHA: passwd

LISTAR ALGUM PACOTE: ex python: apt list | grep python
LISTAR PACOTES INSTALADOS: ex python: apt list --installed | grep python

ZIPAR PASTAS:
EX pasta 'deva': sudo zip deva.zip deva
sudo tar -cvf deva2.tar deva2
p/ fazer a zipagem RECUSIVA: sudo zip -r deva.zip deva

DEZIPAR:
sudo unzip deva.zip

REMOVER PASTA:
EX pasta 'deva': sudo rm -rf deva

CRIAR ARQUIVO OCULTO: ex: vim .arquivo_oculto

FLAGS:
-a : append
-d : delete

d: diretório
rwx: permissão (r: read, w: write, x: execute)
1º grupo de permissão: refere-se ao USUÁRIO RESPONSÁVEL PELO DIRETÓRIO/ARQUIVO: u
2º grupo de permissão: refere-se ao GRUPO RESPONSÁVEL PELO DIRETÓRIO/ARQUIVO: g
3º grupo de permissão: refere-se a TODOS OS OUTROS USUÁRIOS: o

TROCAR O USUÁRIO DE UM DIRETÓRIO/ARQUIVO: chown nome_novo_usuario nome_diretorio_arquivo
TROCAR O GRUPO DE UM DIRETÓRIO/ARQUIVO: chown :nome_novo_grupo nome_diretorio_arquivo
TROCAR O USUÁRIO E GRUPO DE UM DIRETÓRIO/ARQUIVO: chown nome_novo_usuario:nome_novo_grupo nome_diretorio_arquivo

FAZER A TROCA DE FORMA RECURSIVA: chown -R nome_novo_usuario:nome_novo_grupo nome_diretorio_arquivo

MUDAR PERMISSÕES: chmod - muda permissões
EX: chmod u-w arquivo.txt = tira a permissão do usuário de escrever no arquivo

MUDAR DONOS DOS ARQUIVOS: chown

Read (r) - 4
Write (w) - 2
Execute (x) - 1
Nenhuma permissão - 0

chmod u=rwx g=rwx o=rwx
EX: chmod 760

Sempre teremos as permissões assim - 
rwx - da direita para esquerda - 421

Logo, se eu quiser permissão total para usuário e apenas leitura para grupos e outros, eu faço a continha, exemplo:

Total = 4 + 2 + 1 = 7
Apenas leitura = 4 + 0 + 0 = 4

-----
#!/bin/bash

echo "EU SOU UMA VARIAVEL DE AMBIENTE"
echo $MODULO
cd /home
mkdir eu_fui_criado_por_um_script
-----
UM DOS ARQUIVOS DE CONFIGURAÇÃO DE INICIALIZAÇÃO DO S.O.: bash
vim /etc/bash.bashrc COMANDO QUE ESTÁ PRESENTE NA INCIALIZAÇÃO DO S.O. -> quando o sistema subir ele vai executar todos os comandos que estão dentro desse comando

export MODULO=KUBERNETES
export VARIAVEL=GLOBAL

--------

VISUALIZAR AS VARIÁVEIS DE AMBIENTE: printenv

printenv | grep PATH

PATH: variável de ambiente mais importante

ACRESCENTAR CAMINHO NO PATH: export PATH=$PATH:/nome_caminho_diretorio

BASH: interpretador de comandos, serviço que recebe os comandos e os interpreta
SHELL: interface entre o usuário e o S.O. para executar os comandos/executáveis, tela preta, CLI (comand line interface)

ls /usr/bin/ | grep script.sh

export PATH=$PATH:/home/scripts

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/home/diretorio/scripts

CURL: Client URL -> client imbutido no S.O. que consigo fazer requisições para algum site ou API
os navegadores são clients tbm

curl --help
curl --help all

curl -i site: obter status http de uma requisição
curl -O site: fazer download de um arquivo

ABRIR HTML DE UM SITE: ctrl + u

curl https://api.adviceslip.com/advice

curl -i https://api.adviceslip.com/advice

curl -O http://testdomain.com/testfile.tar.qz

curl -i https://api.adviceslip.com/advice && echo

cd /etc/netplan/

echo "ada-server" > /proc/sys/kernel/hostname

cat /proc/sys/kernel/hostname

hostnamectl set-hostname ada-server

sudo apt install python-is-python3

python -m http.server 8080

http://54.211.202.120:8080/

-----------

PARA RODAR ARQUIVO EXECUTÁVEL DENTRO DA PASTA QUE ELE ESTÁ: colocar ./ na frente do nome do arquivo
 
REDE: conexão entre 1 e/ou mais dispositivos, tanto logicamente (a nível de configuração) como fisicamente (a nível de cabo)
centraliza em um SWITCH
para fazer a comunicação é preciso de um endereço IP

IP público: exposto para a internet, modem ou servidor
IP privado: para a rede interna

IFCONFIG: mostra informações de rede
INTERFACES DE REDE:
eth0: conexão com a rede interna/local e tbm utilizada para conectar com a internet
lo (look back): conexão local da própria máquina, para se conectar com ela mesma

é comum que servidores possuam várias interfaces de rede / nic / conector rj45

posso ter uma interface/placa de rede fixa e virtualizar várias interfaces de rede lógicas em cima da física

DIRETÓRIO DE CONFIGURAÇÃO DOS SERVIÇOS: etc

para alterar a configuração da placa de rede: /etc/netplan

PROXY: serviço que age como um intermediário entre o usuário e a internet, recebe e repassa todas as suas requisições ao site que vc tá acessando -> filtra as requisições para saber o que é permitido fazer e o que não é

PROXY REVERSO: um ou mais clientes que vai acessar um servidor

TOR: navegador/browser para conseguir acessar a deep web, que não deixa muitos rastros no caminho, deixa infos mais sigilosas, oculta elas

SSH: Secury Shell - serviço para logar no servidor, conexão criptografada, comunicação entre o cliente e o servidor ocorre de forma criptografada, mas não é uma VPN, é só uma conexão entre 2 computadores na mesma rede ou até em redes diferentes, conexão local ou pela internet
não ocorre nativamente sob uma VPN (Virtual Private Network = Rede Particular Virtual)
cliente consegue se conectar/logar com um servidor/host de forma remota e criptografada, embora seja parecida com o HTTPS, não é uma VPN

/etc/host OU hostname:  informação do nome da minha máquina / do meu serviço

DIRETÓRIO proc: responsável por conter as informações sobre nosso hardware, o gerenciamento dos periféricos

echo 'ada-server' > /proc/sys/kernel/hostname
cat /proc/sys/kernel/hostname

sinal > : sobrescreve o que tá escrito no arquivo
senal >> : acrescenta ao que tá escrito no arquivo

a CHAVE PRIVADA fica do lado do CLIENTE (não pode perder essa chave!)
a CHAVE PÚBLICA fica do lado do SERVIDOR (não tem problema vazar)

o + importante é a chave privada, quando a minha conexão da minha chave privada chegar no meu servidor, a minha chave pública vai conseguir fechar essa comunicação e ver que essa requisição é de um cliente seguro/autorizado -> a conexão SSH acontece dessa forma
a chave pública vai crptografar alguma coisa e a chave privada vai descriptografar

ssh -i demo-deva.pem ubuntu@

service ssh start
service ssh status

chmod 400 demo-deva.pem

sudo apt install ufw
sudo ufw enable
sudo ufw status
sudo ufw app list
sudo ufw allow ssh

/etc : confgurações dos serviços disponíveis

/etc/apache2/ -> onde fica os arquivos estáticos

SSH -> configurando o CLIENT
SSHD -> configurando o DAEMON = SERVIDOR

AUTENTICAÇÃO é você mostrar sua credencial e AUTORIZAÇÃO é você verificar se essa credencial está autorizada ou não