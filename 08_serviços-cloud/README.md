# MÓDULO: SERVIÇOS CLOUD

* `docker run --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management`
* `docker run -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management`
* `rabbitmqadmin publish exchange=amq.default routing_key=hello payload="olar"`
* `docker exec -ti idcontainer bash`

* `pip3 install sys`
* `pip3 install os`

***

#### O protocolo AMQP na versão 0-9-1 fornece 5 tipos de exchange:

*DEFAULT EXCHANGE:*
	- exchange padrão fornecida pelo broker (não possui nome);
	- toda fila criada é automaticamente associada a ela com uma rota que é igual ao nome da fila;
	- usado em caso de sistemas simples, onde é possível ir criando filas conforme sua necessidade e produzindo mensagens de acordo com a fila que deseja utilizar;
	- exemplo: uma máquina de estados.

*DIRECT EXCHANGE:*
	- possui nome e seu comportamento é de encaminhar mensagens que possuam exatamente a mesma rota das filas associadas a este exchange;
	- é uma ótima opção para trabalhar com diversos consumers de maneira balanceada, já que o algoritmo utilizado pelo RabbitMQ para distribuição de mensagens entre consumers é o round-robin;
	- usado em casos em que se precisa distribuir mensagens entre diversos consumers, já que apenas mensagens com rotas específicas serão distribuídas.

*FANOUT EXCHANGE:*
	- ignora a rota;
	- seu comportamento resume-se em mandar uma cópia das mensagens para todas as filas que estão associadas a ele;
	- usando quando se precisa que as mensagens produzidas sejam replicadas para mais de uma fila.

*TOPIC EXCHANGE:*
	- encaminha mensagens de acordo com a rota definida na mensagem e o padrão definido na associacão da fila ao exchange;
	- usando quando é necessário um pouco mais de flexibilidade para o encaminhamento das mensagens, pois possibilita a construção de padrões de rota.

*HEADERS EXCHANGE:*
	- tipo menos comum de exchange;
	- ignora a rota e encaminha as mensagens usando seu cabeçalho;
	- usado caso se precise de condições mais complexas que as citadas anteriormente ou não quer/pode usar uma string como rota.

***

> Como podemos monitorar filas e quais ferramentas nos ajudam com isso
