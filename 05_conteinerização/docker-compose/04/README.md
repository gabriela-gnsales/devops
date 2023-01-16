**Construindo a imagem do redis**
* `docker build -t nomes_redis:1 -f build/Dockerfile-redis .`
    * f = file

<!-- * `cd src`
* `pip freeze > requirements.txt` -->

**Construindo a imagem da aplicação**
* `docker build -t nomes_app:1 -f build/Dockerfile-app .`

**Criando a rede**
* `docker network create nomes_network`

**Rodando o container do redis colocando na rede criada**
* `docker run -d --name servidor_redis --network nomes_network nomes_redis:1`

**Rodando o container da aplicação**
* `docker run -d --name servidor_app -e REDIS_HOST=servidor_redis -e REDIS_CHAVE_NOMES=nomes --network nomes_network -p "8000:5000" nomes_app:1`
    * foi possível colocar `REDIS_HOST=nomes_redis` porque estão na mesma rede