# Projeto final - turma 910

### Criar a rede

`docker network create rede_ada_projeto_final`

### Montar a imagem

`docker build -f build/Dockerfile.app -t app_projeto_final:1 .` 

### Rodar os containers

| Container | Comando | 
| --- | --- | 
| Postgres | `docker run -d --env-file env.dev.psql --name psql_projeto_final --network rede_ada_projeto_final -v ${pwd}/psql_start:/docker-entrypoint-initdb.d -p 5432:5432 postgres:15-alpine` | 
| Aplicação | `docker run -d --env-file env.dev.app --name app_projeto_final --network rede_ada_projeto_final -p 8080:5000 app_projeto_final:1` |