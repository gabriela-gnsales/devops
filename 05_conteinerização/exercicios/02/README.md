**Construindo a imagem**
* `docker build -t exercicio-2:1 .`

**Rodando o container**
* `docker run -d -p "8081:8081" --name exercicio-2 exercicio-2:1`