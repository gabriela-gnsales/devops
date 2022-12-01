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
  * físico (hexadecimal → presença de nºs e letras): __MAC__ → não muda (cravado na placa de rede / NIC / interface)
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
* __ARP:__ Adress Resolution Protocol: endereço físico (MAC); protocolo de mapeamento
* __ICMP:__ Internet Control Message Protocol
* __HTTP:__ protocolo web, para aacessar informações

__TTL:__ Time to Live → não é regra / unidade de mensuração, é conceito

__Switch:__ comutador/redirecionaro de chamadas, é visto como uma central/ponto de segurança/confiança; consegue diferenciar de onde estou saindo e para onde quero chegar; não obstrui a passagem, pode receber várias iinformações ao mesmo tempo
__Hub:__ repetidor; mesmo após a rede mapeada, ele envia para todos os dispositivos/pontas que estão concetados a ele; precisa que a informação seja enviada, para liberar a passagem, obstrui o meio

#### Arquiteturas
* __Estrela:__ ideia de centralização (switch), ex: máquinas EC2; centralização das informações em um meio comutado (switch)
* __Cliente Servidor:__
* __Barramento:__

#### Conexões
* 1:1 → __Unicast__
* 1:N → __Multicast__
* N:N → __Broadcast__ → ex: protocolo ARP 

