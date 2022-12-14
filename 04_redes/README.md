# MÓDULO: REDES

### História Internet
* rede mundial de computadores
* década de 40: computadores gigantes para cálculos matemáticos através de alavancas e ? perfurados
* década de 60: 
 * mainframe computadores grandes
 * grande evento → Guerra Fria (EUA X URSS) → avanços tecnológicos
 * DARPA (departaemnto de defesa dos EUA) faz um estudo para aumentar a comunicação nos EUA → Projeto DARPANET (semente da Internet)
 * compartilharam o projeto com as Universidades Americanas, que criaram uma atualização → ARPANET
 * Universidades Americanas compartilharam o projeto com Universidades de outros países 
 * cada país começou a desenvolver seu prórpio projeto com base no ARPANET → os padrões desenvolvidos não se conversavam
 * Internet
  > em síntese: devido a necessidade de comunicação, principlamente pela situação da Guerra → teve um cheque em branco para avançar no desenvolvimento de tecnologia
* surgimento dos __principais players do mercado de redes:__ Cisco, Juniper Networks, Palo Alto Networks, Fortinet, Huawei
* surgimento de órgão reguladores (ICANN, ANSI, ISO, W3C)
> devido a necessidade de padronização

#### Modelo OSI (Open System Interconnection)
Esse modelo separa comunicação entre dispositivos em camadas, de tal forma que cada camada é responsável por uma determinada parte do processo de comunicação, e estabelece protocolos que devem ser utilizados e quais as boas práticas de comunicação.
O modelo OSI é dividido em sete camadas, sendo elas:
* __7 - Application (Aplicação):__ Responsável pela interação com o usuário, é nesta camada que temos os protocolos mais conhecidos como o HTTP, DNS, SMTP, FTP, entre outros, sendo realizada a coleta dos dados que são então enviados para a camada 6 (Apresentação).
* __6 - Presentation (Apresentação):__ Responsável pela criptografia e compactação dos dados antes de enviá-los para a camada 5 (Sessão).
* __5 - Sessão (Session):__ Responsável por estabelecer a comunicação entre dois dispositivos, denominada sessão, e pelo seu encerramento.
* __4 - Transporte (Transport):__ Responsável por receber os dados da camada 5 (Sessão) e transformá-los em segmentos. Essa camada determina o controle de fluxo e a velocidade da transmissão entre remetente e receptor, e tem a preocupação de confirmar a integridade da mensagem entre origem e destino, seus principais protocolos são TCP e UDP. 
* __3 - Rede (Network):__ Responsável pela transformação dos segmentos vindo da camada 4 em pacotes. Essa camada é responsável pela comunicação entre redes diferentes através do roteamento destes pacotes. O principal protocolo da camada 3 (Rede) é o protocolo IP, ele é responsável pelo endereçamento dos pacotes de rede, ou seja, é responsável por gerar um endereço ao seu computador, ou qualquer servidor, no momento que este conecta-se à internet. Atualmente existem dois formatos IPV4 e IPV6. O primeiro foi criado na década de 80 e é utilizado até hoje, ele possibilita o uso de aproximadamente 4 bilhões de endereços. Por mais que a quantidade de IP's disponíveis na versão 4 seja grande a internet como um todo cresceu demais e os IP's estão cada vez mais escassos, para resolver esse problema foi criado o IPV6 que tem capacidade de alocar por volta de 340 undecilhões de endereços.
* __2 - Enlace (Data Link):__ Responsável pela fragmentação do pacote vindo da camada de rede em pequenos quadros. A ideia dessa camada é trabalhar com a comunicação entre dispositivos da mesma rede, onde cada quadro conterá o endereço físico de origem e destino de cada dispositivo. Este endereço é denominado MAC (Media Access Control), e é responsável por endereçar fisicamente cada placa de rede às chamadas NIC 's (Network Interface Card). Os principais protocolos desta camada são: Ethernet, PPP e Token Ring. 
* __1 - Física (Physical):__ Responsável pela padronização do hardware da rede, através de padrões de cabos, fibras, wireless e a conexão física entre esses dispositivos. Essa camada transforma o dado em bit para a comunicação elétrica no meio físico. Essa transformação acontece geralmente por meio do modem que tem a função de modular de demodular o sinal vindo do ISP. O sinal pode vir tanto por pulso elétrico através de um meio guiado como de ondas de rádio de um meio wireless.

#### Modelo TCP/IP
Modelo mais usado atualmente, sendo seu nome em referência a uns dos principais protocolos da Internet, o protocolo TCP, da camada 4 (Transporte), e o protocolo IP, da camada 3 (Redes). A ideia do modelo TCP/IP é agrupar camadas do OSI com responsabilidades semelhantes, transformando a representação de 7 camadas em apenas 4.

#### Reguladores internacionais
* __ICANN__ (Internet Corporation for Assigned Names and Numbers): regulamentar a distribuição dde ranges de IP's (endereços) para os continentes / regiões do planeta e responsável também pelo gerenciamento dos servidores de DNS's
* __ANSI__ (American National Standards Institute): padronização internacional de cabeamento estruturado
* __ISO__ (International Organization for Standardization): padronização internacional de normas
* __W3C__ (World Wide Web Consortium): consórcio formado por empresas de tecnologia  que desenvolvem padrões para a criação e manutenção de websites; responsável pelos padrões HTML e CSS

#### Reguladores nacionais
* __Anatel__ (Agência Nacional de Telecomunicações): agência reguladora responsável  pelo setor de comunicação brasileira (comunicação geral, não só Internet)
* __ABNT__ (Associação Brasileira de Normas Técnicas): entidade responsável pela padronização de normas brasileiras; utilizada para definir as padronizações de cabeamento estruturado no Brasil como, por exemplo, a ABNT NBR 14565
* __CGI__ (Comitê Gestor da Internet): órgão responsável pelos serviços de Internet no Brasil; responsável pelos servidores de domínio `.br` (focado no tráfego / comunicação na Internet em si)
* __Registro BR:__ site responsável pela aquisição de domínios `.br`

#### Certificações mais importantes
* CCNA - Cisco Certified Network Associate
* CCNP - Cisco Certified Network Professional
* CompTIA Network +

### Rede
* troca de informação / conteúdo / de pulsos elétricos (0 e 1)
* dispositivo lógico (máquinas virtuais...)
* conexão entre 2 ou mais dispositivos
* configuração física (por meio de ccabos ou ondas de rádio) e lógica
* endereço
  * lógico (decimal): __IP__ → muda a todo momento, toda vez que a máquina é iniciada...
  * físico (hexadecimal → presença de nºs e letras): __MAC__ (Media Access Control address) → não muda (cravado na placa de rede / NIC (Network Interface Card) / interface)
  * __máscara de rede__: diz qual parte do endereço corresponde ao endereço da rede e qual parte corresponde ao endereço host

> 1 = positivo (emissão de pulso elétrico)
> 0 = negativo (ausência de pulso elétrico)
> Bit: 0 ou 1
> Byte: conjunto de 8 Bits = ex: 10110110

__Cisco Packet Tracer:__ principal simulador na área de redes

* __PAN (Personal Area Network):__ 
  * rede que permite a conexão de dispositivos em nível pessoal
  * alcance de metros, em alguns casos cm
  * conexão via rádio / wireless
  * dispositivos: smartwatches, fone bluetooth...
* __LAN (Local Area Network):__ 
  * rede de casa / trabalho
  * alcance maior, a nível de m
  * conexão via cabo ou wireless
  * conexão de mais dispositivos (smart tv, celular, notebook, geladeira smart...)
* __MAN (Metropolitan Area Network):__
  * rede em nível de cidade, metrópole e/ou Estado: operadores de telecom (TIM, VIVO...), operadoras de TV (sky...)
  * alcance a nível de km ou +
  * conexão via cabo ou wireless com repetidores
* __WAN (Wide Area Network):__
  * internet
  * nível global / intercontinental

#### Protocolos
* __ARP (Adress Resolution Protocol):__ protocolo de mapeamento; manda a informação para o switch; verifica / faz a resolução dos endereços físicos (MAC)
  * switch dispara a informação para todas as portas conectadas nele; a informação fica por um tempo no switch, ela tem um tempo de vida (TTL); a tabela de mapeamento? é então resetada
* __ICMP (Internet Control Message Protocol):__ comunicação de um ponto a outro
* __DHCP (Dynamic Host Configuration Protocol):__ protocolo que configura os dispositivos de forma automática; atua na camada 7 do Modelo OSI; responsável pela alocação de informações de rede (endereço IP, máscara, gateway e DNS) dos novos dispositivos; é bom para centralizar responsabilidades, automatizar processos e manter uma certa proteção
* __DNS (Domain Name System):__ protocolo responsável pela resolução de nomes na rede; atua na camada 7 do Modelo OSI
* __HTTP (Hypertext Transfer Protocol):__ protocolo responsável pela transferência de arquivos entre origem e destino através da internet; atua na camada 7 do Modelo OSI; protocolo web para acessar informações
* __HTTPS (Hypertext Transfer Protocol Secure):__ protocolo responsável pela transferência de arquivos entre origem e destino através da internet de forma SEGURA, por meio de um certificado válido; garante a criptografia em trânsito
  * certificados - protocolos:
    * SSL: Secure Socket Layer → mais antigo
    * TLS: Transport Layer Security → sucessor / atualização do SSL; mais utilizado
  __OBS:__ normalmente, todos so certificados são chamados de SSL, porque o nome "pegou", mesmo sendo na realidade TLS
* __IP:__ protocolo responsável pelo endereçamento dos pacotes de rede na camada 3 do Modelo OSI
  * atualmente existem dois formatos: IPV4 e IPV6
  * o endereço IP é dividido em 2 partes: endereço de rede e de host; essa divisão ocorre de acordo com a máscara que o endereço da rede seguir
* __TCP (Transmission Control Protocol):__ protocolo que permite ordenar os pacotes, retentativas e confirmar a entrega dos pacotes; é mais lento que o UDP; usado nromalmente para conexões clientes servidores, para acessar praticamente a maioria dos serviços utilizados hoje
* __UDP (User Datagram Protocol):__ protocolo utilizado para aplicações realtime e stream (lives, videochamadas...); não ordena pacotes e nem garante a entrega

→ protocolos TCP e UDP atuam na camada 4 do Modelo OSI, estabelecendo a conexão, abrindo a porta de origem e fixando com a porta de destino

__OBS:__ criptografia em repouso: informação guardada, ex: banco de dados

__Latência:__ duração da requisição desde a saída até a resposta do destino

__Cache:__ serviço que armazena as informações mais acessadas em servidores mais próximos do solicitante

__TTL (Time to Live):__ não é regra / unidade de mensuração, é conceito

* __Switch:__ comutador/redirecionador de chamadas, é visto como uma central/ponto de segurança/confiança; consegue diferenciar de onde estou saindo e para onde quero chegar; não obstrui a passagem, pode receber várias iinformações ao mesmo tempo; dispositivo que possibilita a coenxão de diversos aparelhos; está na CAMADA 2
  * _comutação:_ capacidade de sair de um lugar e mandar a informação para um único dispositivo da rede; troca ou encaminhamento de informação
* __Hub:__ repetidor; mesmo após a rede mapeada, ele envia para todos os dispositivos/pontas que estão concetados a ele; precisa que a informação seja enviada, para liberar a passagem, obstrui o meio; está na CAMADA 1 → pega os pulsos elétricos (0 e 1) e envia para todos os pontos conectados a ele

#### Arquiteturas
* __Estrela:__ todos os membros da rede se conectam através de um centralizador, geralmente o Switch; ideia de centralização; ex: máquinas EC2; centralização das informações em um meio comutado (switch);configuração: host conectados a um ponto central e a comunicação vai acontecer passando por esse ponto; benefício: centralizar a informação, dá até para homologar/filtrar o que está passando ali (colocar um proxy...); ponto negativo: se o ponto central falhar, toda a rede para de conversar (necessário uma certa redundância, balancemaneto de carga... para manter a arquitetura disponível mesmo que uma das peças caia, vários swithcs para caso um falhe, aponte para o outro); não há obstrução de passagem, nem colisão de dados/pacotes/quadros
* __Cliente Servidor:__ cliente solicita informação para um servidor; servidor pode ser tanto um computador normal ou uma máquina mais potente; a ideia é o host (cliente) solicitar um arquivo para um computador central (servidor) que é responsável por centralizar e armazenar os documentos e ainda enviar o documento solicitado para aquele determinado cliente
* __Barramento:__ centraliza a informação em um ponto e a repete para todos os dispositivos conectados e ele; um meio que vai permitir que os dispositivos se comuniquem (camada 2); ocorre obstrução de passagem, só permite o envio de outra informação quando a primeira for concluída; dispositivos compartilham o mesmo meio físico para transmissão de dados, quando um faz um envio, o outro precisa aguardar o término para iniciar um novo requisição, senão haverá conflitos de mensagens
* __Ponto a Ponto (Peer to Peer):__ uma máquina faz requisição como servidor, mas também está apta a disponibilizar informações como servidor; pode solicitar (receber) como disponibilizar informação; necessário antigamente pela internet reduzida (limite escasso de banda, internet discada) e falta de servidores potentes para centralizar a informação e permitir que muita gente se conectasse, questão da latência também 
* __SDN (Software Definition Network):__ construir uma rede a nível de software; abstração da arquitetura física; semelhante à arquitetura de Cloud ex: virtualização de uma rede;
* __Cloud:__ arquitetura global, redundante e altamente disponível; cria uma VPC no provedor de Cloud e já vem tudo embutido, já abstrai a informação da configuração de switchs, roteadores...; infra como software; tudo é via chamada de API

#### Conexões
* 1:1 __Unicast__ → ex: protocolo ICMP (quando comunica com apenas 1 dispositivo)
* 1:N __Multicast__ → ex: protocolo ICMP
* N:N __Broadcast__ → conceito de fazer comunicação com todo mundo da rede e todos responderem; IP Broadcast por padrão é o último IP disponível da rede; ex: protocolo ARP 
* __Anycast__

> __Diferença interfaces FastEthernet e GigabitEthernet__
> Capacidade de trafegar bits
> FastEthernet: limite de 100 Mb
> GigabitEthernet: limite de 1000 Mb

> __Diferença de Switch e Roteador__
> Switch trafega quadros em uma rede local, baseado a nível de ARP e endereço MAC, da camada 2 (enlace) 
> Roteador trafega pacotes, atrelado ao endereço IP da camada 3 (rede)

__Conversão de decimal para binário:__
1   | 2   | 3   | 4   | 5   | 6   | 7   | 8
--- | --- | --- | --- | --- | --- | --- | --- 
2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 
128 | 64  | 32  | 16  | 8   | 4   | 2   | 1

__Classes IP:__ primeiro octeto
* __A:__ 1 a 127 → 2^24 = 16.777.216 possibilidades (milhões)
* __B:__ 128 a 191 → 2^16 = 65.536 possibilidades (milhares)
* __C:__ 192 a 223 → 2^8 = 256 possibilidades (centenas)
* __D:__ 224 a 239 → multicast
* __E:__ 240 a 255 → teste de novas tecnologias
>__OBS:__ 255 é o valor máximo obetido utilizando os 8 bits do octeto por causa do 2^8 = 256 números no total (de 0 a 255)
> __Classe A:__ 1.0.0.0 a 127.255.255.255 (na prática vai até o 126.255.255.255 porque o 127 trata-se da rede localhost)
> __Classes D e E:__ não têm endereçamentos possíveis, são reservadas / específicas para um determinado fim

##### IPs restritos e privados
* 10.0.0.0/8 
* 172.16.0.0/12 
* 192.168.0.0/16 
* 127.0.0.0 → todos os IPs iniciando pelo octeto 127 correspondem ao endereço da própria máquina e próprio dispositivo
* 169.254.0.0 → endereço de IP APIPA, utilizado quando não é encontrado um roteador na rede
* 0.0.0.0 → IP de inicialização da máquina

##### Máscaras
* __Classe A:__ 255.0.0.0 → 1º octeto é a rede; os octetos restantes são os endereços de host → R.H.H.H 
  * __OBS:__ por isso para a classe A há 2^24 possibilidades, que são as combinações possíveis dos 3 ocetos de host (0.0.0) = 256 x 256 x 256 = 16.777.216
* __Classe B:__ 255.255.0.0 → 1º e 2º octetos são a rede → R.R.H.H
* __Classe C:__ 255.255.255.0 → 1º, 2º e 3º octetos são a rede → R.R.R.H

__Endereço de Broadcast:__ utilizado na comunicação com todos os dispositivos da rede (analogia: portaria de um condomínio)

Rede | Host | Broadcast
---- | ---- | ---------
Condomínio | Casas | Portaria
192.168.1.0 (1º nº possível) | 192.168.1.1 até 192.168.1.254 | 192.168.1.255 (último nº possível)


>__Decimal:__ 10.0.0.0/8 → 8 primeiros números do primeiro octeto correspondem ao endereço de Rede (00001010)
>__Binário:__ 00001010.00000000.00000000.00000000

>__Decimal:__ 10.0.0.0/8
>__Binário:__ 11111111.00000000.00000000.00000000

> __127.x.x.x__ → destinado para o localhost = loopback 
> rede que aponta/ligada ao próprio computador
> não é exposta para a internet, é uma rede local

> 2 endereços:
> * Rede: 10.0.0.0
> * Host: 10.x.x.x

__Rede:__ 192.168.10.0/24
__Máscara:__ 255.255.255.0

muito comum: /8 /16 /24
`/alguma coisa` são os bits fixos...

11000000.10101000.00001010.00000000/00011000

Rede: 11000000.10101000.00001010.00000000
Máscara: 11111111.1111111.1111111.00000000

> Hosts: 2^n - 2 = 254
> n = número de bits do octeto de hosts
> 
> 2^(32 - bitsmascara) - 2
> onde a máscara, nesse caso, seria 24

* Endereço da rede
* Endereço de broadcast
##### RFC (Request For Comments)
Descritivo de como o protocolo deve ...? 
* RFC 1918 - Address Allocation for Private Internets
* RFC 5735 - Special Use IPv4 Addresses

__Gateway:__ representa o roteador que está conectando

__OBS:__ 
* `ping <site>` (Windows e Linux)
  * comando para testar conectividade através do protocolo ICMP
  * informa o tempo de resposta (latência)
  * o ping (Packet Internet Network Groper) é responsável por enviar uma quantidade de pacotes ao endereço especificado para verificar se o endpoint de destino é conhecido na rede
  * indica o TTL (Time to Live), que é o tempo de vida do pacote na rede e o tempo de resposta do endpoint
  * o fato de não ter um ping com sucesso não significa que não há conexão com o destino, mas sim que pode existir um firewall ou proxy barrando esse tipo de conexão
* `ping 127.0.0.1` ou qualquer outro endereço de IP que inicia com 217 (diz respeito a própria máquina) = testar placa de rede 
* `tracert <site>` (Windows) `tracerout <site>` (Linux) = traça a rota, mostra todos os locais por onde o sinal passa até chagar em casa 
* `ipconfig`
  * mostra todas as placas de rede, adaptadores e os IPs configurados
  * tem como finalidade apresentar as configurações atuais das interfaces de rede
  * são exibidos endereços IPV6 e IPV4, máscara de sub-rede e gateway padrão
  * esse comando exibe todas as interfaces de redes do host, desde as destinadas a conexões Ethernet, Wireless ou interfaces virtualizadas
* `ipconfig /flushdns`
  * esse parâmetro utilizado com o `ipconfig` indica a ordem de realizar uma limpeza dos endereços de servidores DNS´s salvos em cache no host
  * esse comando pode ajudar na correção de erros na resolução de nomes DNS's e nos redirecionamentos aos sites

> __Diferença entre IP de Classe 5 e Máscara__
> Verificar se o octeto é misto (0 e 1 misturado)
> Caso apresente apenas números 1 no início é um octeto de máscara

#### Cálculo de sub-redes
* 1º passo: olhar a máscara e identificar o octeto misto 
* 2º passo: determinar o salto (variação entre as sub-redes) → fazer subratação de 256 e do número do octeto misto 
* 3º passo: determinar todos os endereços de rede
* 4º passo: determinar todos os endereços de broadcast
* 5º passo: determinar todos os hosts

> __Exemplo:__ IP = 192.168.1.10 (Classe C)
> * Máscara: 255.255.255.192
> * Salto: 256 - 192 = 64 IPs (incluindo os endereços de rede e de broadcast)
> * Endereços de rede: 
>   * 192.168.1.0
>   * 192.168.1.64 (soma o salto no último octeto)
>   * 192.168.1.128
>   * 192.168.1.192
>     * 192.168.1.256 (DESCONSIDERAR → SÓ PARA VERIFICAR → no final SEMPRE tem que bater no 256)
> * Endereços de broadcast:
>   * 192.168.1.63 (diminui 1 do último octeto do próximo endereço de rede = 64 - 1 = 63)
>   * 192.168.1.127
>   * 192.168.1.191
>   * 192.168.1.255
> * Hosts
>   * 192.168.1.1 a 192.168.1.62
>   * 192.168.1.65 a 192.168.1.126
>   * 192.168.1.129 a 192.168.1.190
>   * 192.168.1.193 a 192.168.1.254

__CIDR (Classes Inter-Domain Routing):__ informa qual a faixa de IPs pode usar

__Máscara:__ 
* objetivo: diferenciar o que será rede e o que será host
* para segurança, para não ficar exposto

***

#### Exercício 1

Rede Empresa: DevaRede Deva
Deva: 192.168.0.0/26
Rede classe C e privada (trabalhar com uma LAN local)

Departamentos:
* RH: 60
* TI: 60
* Financeiro: 60
* Marketing: 60

> __CIDR: /26__
nºs de 1 = 26
11111111.11111111.11111111.11000000
2^7 + 2^6 = 128 + 64 = 192

> __Máscara:__ 255.255.255.192

> __Salto:__
256 - 192 = 64 → nºs de IPs em cada sub-rede (subnet)

Departamento | Rede | Host | Broadcast
------------ | ---- | ---- | ---------
RH | 192.168.0.0 | 192.168.0.1 a 192.168.0.62 | 192.168.0.63
TI | 192.168.0.64 | 192.168.0.65 a 192.168.0.126 | 192.168.0.127
Financeiro | 192.168.0.128 | 192.168.0.129 a 192.168.0.190 | 192.168.0.191
Marketing | 192.168.0.192 | 192.168.0.193 a 192.168.0.254 | 192.168.0.255

***

#### Exercício 2

Rede Empresa: DevaRede Deva
Deva: 192.168.0.0/27
Rede classe C e privada (trabalhar com uma LAN local)

Departamentos:
* RH: 30
* TI: 30
* Financeiro: 30
* Marketing: 30

> __CIDR: /27__
nºs de 1 = 27
11111111.11111111.11111111.11100000
2^7 + 2^6 + 2^5 = 128 + 64 + 32 = 224

> __Máscara:__ 255.255.255.224

> __Salto:__
256 - 224 = 32 → nºs de IPs em cada sub-rede (subnet)

Departamento | Rede | Host | Broadcast
------------ | ---- | ---- | ---------
Marketing | 192.168.0.0 | 192.168.0.1 a 192.168.0.30 | 192.168.0.31
Financeiro | 192.168.0.32 | 192.168.0.33 a 192.168.0.62 | 192.168.0.63
TI | 192.168.0.64 | 192.168.0.65 a 192.168.0.94 | 192.168.0.95
RH | 192.168.0.96 | 192.168.0.97 a 192.168.0.126 | 192.168.0.127

__Configuração roteador para virtualizar 2 interfaces:__
```
interface GigabitEthernet 0/0.1
encapsulation dot1Q 10
ip address 192.168.0.1 255.255.255.224

interface GigabitEthernet 0/0.2
encapsulation dot1Q 40
ip address 192.168.0.97 255.255.255.224
```

***

#### Exercício 3

Rede Empresa: DevaRede Deva
Deva: 192.168.0.0/24
Rede classe C e privada (trabalhar com uma LAN local)

Departamentos:
* RH: 6
* TI: 20
* Financeiro: 60
* Marketing: 120

__VLSM (Variable Lenght Subnet Mask):__ técnica que permite a divisão de uma rede em quantidades menores; devido a limitação do IPV4, é muito comum as empresas terem um endereço de rede que precisa ser distribuído em redes menores para alocar cada departamento
* 1º ordenar de forma decrescente
* Marketing: 2^7 = 128
  * total de hosts: 128
  * total de hosts úteis: 126 
* Financeiro: 2^6 = 64
  * total de hosts: 64
  * total de hosts úteis: 62
* TI: 2^5 = 32
  * total de hosts: 32
  * total de hosts úteis: 30
* RH: 2^4 = 8
  * total de hosts: 8
  * total de hosts úteis: 6 

> __CIDR: /24__
nºs de 1 = 24
11111111.11111111.11111111.00000000

> __Máscara:__ 255.255.255.224
192.168.0.224: 11111111.11111111.11111111.11100000

> __Salto:__
Marketing: 256 - 128 = 128
Financeiro: 128 + 64 = 192
TI: 192 + 32 = 224
RH: 224 + 8 = 232

Departamento | Rede | Host | Broadcast
------------ | ---- | ---- | ---------
Marketing | 192.168.0.0 | 192.168.0.1 a 192.168.0.126 | 192.168.0.127
Financeiro | 192.168.0.128 | 192.168.0.129 a 192.168.0.190 | 192.168.0.191
TI | 192.168.0.192 | 192.168.0.193 a 192.168.0.222 | 192.168.0.223
RH | 192.168.0.224 | 192.168.0.225 a 192.168.0.230 | 192.168.0.231

***

__OBS:__ é comum / convenção que o primeiro endereço de host disponível seja alocado ao GATEWAY 

***
#### CABOS
* Diretos: dispositivos diferentes
* Cruzados: dispositivos iguais (ex: 2 switches); ponta cruzada para não gerar conflitos de pacotes
* RJ45 Pinout T-568A
* RJ45 Pinout T-568B
* padrão UTP: mais antigo, não tem isolamento entre o cabo, ocorre interferências 
* padrão STP: mais utilizado, possui uma divisão de plástico para isolar mais cada parte do cabo e uma embalagem de alumínio para diminuir o ruído
* coaxial: mais utilizado para disponibilizar sinais de televisão, mas consegue passar internet também
* fibra óptica: mais utilizado para internet; diferente do UTP, STP e coaxial, ele não é ligado a um par de cobre, tem pequenos pedaços de vidro dentro, pulso de luz refletido de um lado pro outro até chegar no destino final, transferência na velocidade da luz
  * fibras monomodo: 80 m
  * fibras multimodo: 300 m
* categorias (5, 6, 7...): refere-se a velocidade → quanto maior a categoria, maior a capacidade de passar bits

##### Cabeamento estruturado:
Visa a estruturação do cabeamento padronizada, para que a rede seja:
* confiável: confiança de que a rede funcionará sem (muitas) falhas
* escalável: conseguir aumentar ou diminuir a capacidade da rede conforme a necessidade de utilização
* resiliente: mesmo sofrendo instabilidade, consegue voltar ao estado normal

__7 estruturas:__
* entrada do edifício: ponto inicial que conecta a rede externa (WAN) até a rede interna (LAN); ex: até onde a vivo/claro chega com a internet
* sala de equipamentos: onde concentra os equipamentos mais utilizados (modens, switchs, roteadores, firewalls...)
* em cada andar há um cabeamento horizontal, um switch específico para conectar cada departamento e uma área de trabalho
* backbone: cabeamento veritical que conecta os switchs dos andares à sala dos equipamentos (ao switch principal)
* rack: armário onde estão organizados todos os dispositivos/equipamentos (switchs, roteadores...)

***

#### IPV4
* criado por volta das décadas de 70/80
* permite +/- 4 bilhões de dispositivos
* formato de 32 bits
* 4 octetos divididos por ponto
* sistema decimal: 0 a 9
* intervalo de cada octeto: 0 a 255 (256 números no total)
* há o conceito de subnet porque há mais dispositivos do que IP
* ex: 192.168.0.1

#### IPV6
* sucessor do IPV4 
* criado na década de 90
* suporta dispositivos na casa dos undecilhões (nº composto por 36 zeros)
* sistema hexadecimal (letras e nºs)
* formato de 128 bits
* dividido em 8 blocos com 16 bits cada
* não há o conceito de subnet
* ainda utiliza a conotação de máscara (para diferenciar rede e hosts)
* status atual: 35% da internet utilizando
* muito utilizado nas operadores/telecomunicações, roteamento na internet, configuração na placa de rede (semidisponibilizado)
* ex: 1050:0000:0000:0000:0005:0600:300c:326b
* os pares que contêm 0 à esquerda podem ser limitados a um único 0
  * ex: 1050:0:0:0:5:600:300c:326b

#### NAT - Network Address Translation
* protocolo utilizado para suprir a escassez dos endereços IPV4
* ideia de postergar o fim do IPV4
* permite a conexão dos dispositivos locais com a internet através de um único IP público (gateway)
* tradução de uma rede privada para uma rede pública
* 3 tipos:
  * __Static NAT:__ mapear um IP privado para um IP público
  * __Dynamic NAT:__ mapear diversos IPs privados para um IP público
  * __PAT (Port Address Translation):__ mapear diversos IPs privados para um IP público através da utilização de portas (faz a tradução com nível de portas)

__PORTA__
* camada 4 - transporte
* na minha máquina / no meu IP tenho uma variação de portas disponíveis de 0 a 65535
* cada porta corresponde a um serviço
* a porta tem a função de estabalecer uma conexão entre dispositivos
* do switch:
  * porta access: trafega apenas 1 VLAN; acessar uma informação
  * porta trunk: trafega todas as VLANs do switch 

***

### Wireless
* padrão 802.11n
* redes sem fio
* WiFi
* AP Access Point
* SSID → nome da rede
* banda
  * canal
  * tem uma função de ser uma RODOVIA
  * 2,4 Ghz
    * padrão:
    * prós:
    * contras:
  * 5 Ghz
    * padrão: 802.11ac
    * prós:
    * contras:
  * 6 Ghz
    * padrão: 802.1ax
    * prós: maior taxa de dados, menos propensos a interferências, padrão mais novo
    * contras:
* faixas
  * frequência
  * podem variar +/- de 20-160 Mhz


***

### Segurança de Rede

#### Física
* isolar meus equipamentos de rede e servidores
* habilitar modelos de segurança
  * reconhecimento facial
  * leitura biométrica
  * acesso por senha
* desativar o acesso dos periféricos dos dispositivos
* trocar as senhas padrões dos dispositivos
* atualizar o firmeware
* engenharia social

#### Lógica
* cofre de senhas
  * Vault Hashicorp
  * Zohoo
  * Bitwarden 
  * 1password
  * Keeper
* SSO Single Sign On
  * base de dados principal
  * primeiro autenticar
  * segundo autorizar
* certificados
  * HTTPS
  * certificados digitais
  * MFA
    * email
    * redes sociais
    * AWS ...
* firewall
  * nível de rede
  * nível de máquina: antivírus
* backup
  * full: backup completo diário
  * incremental: realizar um 1º backup full e nos próximos dias realizará um backup incremental
  * realizar frequentemente exercícios de DS
* atualização
  * sistemas
  * serviços ...
* VPN - Virtual Private Network
  * conexão criptografada
  * Site to Client: conexão entre o servidor de VPN da empresa com o seu notebook, através de um software como Cisco VPN
  * Site to Site: conexão entre o servidor de VPN da empresa matriz com a empresa filial

#### Principais ataques
* Ransomware → acessar a rede e criptografar todos os dados
* Dos: ataque de negação de serviço
* DDoS
* SQL: Injection → obter dados do banco de produção
* Main in the Middle
