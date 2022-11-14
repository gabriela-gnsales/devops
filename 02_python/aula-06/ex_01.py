# Crie um algoritmo que escreva do 1 a 100 dentro do arquivo dados.txt

arquivo = open("E:\\04_Cursos\Programação\Let's Code\DevOps\devops\python\\aula-06\dados.txt", "a", encoding="utf-8")

for n in range(1, 101):
    # arquivo.write(str(n) + ' ')
    arquivo.write(f'\n{n} - ' + ' ')
