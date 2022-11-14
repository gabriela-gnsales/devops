#                   MODOS DE ABERTURA DE ARQUIVOS
# ==================================================================
#                        |    TEXTO         |    BINARIO
# ==================================================================
# Leitura                |     "r"          |     "rb"
# Leitura/Atualização    |     "r+"         |     "rb+"
# ------------------------------------------------------------------
# Escrita                |     "w"          |     "wb"
# Escrita/Atualização    |     "w+"         |     "wb+"
# ------------------------------------------------------------------
# Anexar                 |     "a"          |     "ab"
# Anexar/Leitura         |     "a+"         |     "ab+"
#

# encoding = "utf-8"
texto = 'Manipulação de Arquivos - DEVA'

# arquivo = open("E:\\04_Cursos\Programação\Let's Code\DevOps\devops\python\\aula-06\dados.txt", "w", encoding="utf-8")
# arquivo.write(texto)

# arquivo = open("E:\\04_Cursos\Programação\Let's Code\DevOps\devops\python\\aula-06\dados.txt", "r", encoding="utf-8")
# retorno = arquivo.read()
# print(retorno)

# arquivo2.write(texto + " - " + retorno)

# try:
#     arquivo = open('./dados', 'r+')
#     arquivo.write('Alterei o começo do arquivo\n')
#     arquivo.close()
# except:
#     print('Erro no arquivo.')

texto_2 = '\nAdicionando informações.'
arquivo = open("E:\\04_Cursos\Programação\Let's Code\DevOps\devops\python\\aula-06\dados.txt", "a", encoding="utf-8")
arquivo.write(texto_2)

arquivo_img = open("E:\\04_Cursos\Programação\Let's Code\DevOps\devops\python\\aula-06\logo_ada.jpg", "rb")
retorno_img = arquivo_img.read()
print(retorno_img)
arquivo_img.close()

arquivo_img_saida = open("E:\\04_Cursos\Programação\Let's Code\DevOps\devops\python\\aula-06\logo_ada_saida.jpg", "wb")
arquivo_img_saida.write(retorno_img)
arquivo_img_saida.close()


