# MÓDULO: OBSERVABILITY

### Observability: 
Definida como uma medida de quão bem os estados internos de um sistema podem ser inferidos a partir do conhecimento das saídas externas desse sistema. Simplificando, observabilidade é quão bem você pode entender seu sistema complexo. Em resumo, através de saídas do sistema (outputs) é possível coletar informações de como ele está funcionando (métricas).

#### Importância da Observability
- Dimensionar corretamente os recursos;
- Acompanhar a saúde do sistema;
- Coletar informações sobre a aplicação e infraestrutura;
- Ajudar na tomada de decisões.

#### Relação da Observability com o DevOps e SRE
- DevOps
    - Colaboração entre os times de Operação e Desenvolvimento;
    - Automação de processos e tarefas visando a entrega mais rápida, qualificada e eficaz dos projetos;
    - Atuando com as metodologias ágeis;
- SRE - Site Reliability Engineer
    - Responsável por manter a confiabilidade das aplicações;
    - Confiabilidade:
        - Gerenciamento do sistema;
        - Performance;
        - Escalabilidade;
        - Resiliência;
        - Observabilidade e monitoramento;
        - Automação de tarefas.
- DevOps vs SRE
    - O SRE é a implementação da cultura DevOps


**OBS:** futuro sucesso: Data Platform

***

## Projeto 

- Criar projeto no PyCharm com ambiente virtual (venv)
- Iniciar repositório git e criar branch develop (além da main/master)
- Na branch develop:
    - Adicionar arquivo *app.py* com código do projeto (API Flask)
    - Adicionar arquivo *requirements.txt* → arquivo de dependências do python (onde estão listados os programas a serem instalados)
    - Código para instalar o que estiver no *requirements.txt* (executá-lo no terminal): `pip install -r requirements.txt` 
        - `-r` → recursivo, instalar linha por linha

### Containerizar a aplicação

**Método 1**
- Adicionar arquivo *Dockerfile* para criar imagem do container
- Código para subir imagem do container: `docker image build -t ada-deva-observatility .`
- Código para rodar o container da aplicação: `docker run -p 5000:5000 -d ada-deva-observatility`

**Método 2:** utilizando *docker-compose*
- Adicionar arquivo *docker-compose.yml* para criar o container que irá rodar a aplicação
- Código para rodar o *docker-compose*: `docker compose up`
    - é possível colocar nele o comando para buildar direto a imagem do container, sem ter que fazer o passo anterior de subir a imagem do container antes
