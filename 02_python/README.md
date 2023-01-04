# PYTHON

PARA IDENTAR AUTOMÁTICO NO PYCHARM: Ctrl + Alt + I/L

brew install python3 -> PROBLEMA: normalmente, não instala a última versão

pip install ipython

ipython -i tupla.py

Set-ExecutionPolicy Unrestricted -Force


https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

no Pycharm por padrão ele inicia automático
mas deixa eu resumir uns comandos
python3 -m venv nome_da_venv Deva

pip list
pip -m pip install --upgrade pip

Ativando no Windows - .\diretorio\nome_diretorio\activate

Ativando no Linux e Mac - source diretorio/bin/activate

Desativar - deactivate

User
Access key ID
Secret access key
python_svc
AKIARQVW6NUZERLJ7D74 
+5Vua3uIZoRq92hxeizdHr8JVAK1ZBQm7dbLUSpl


easier to ask forgiveness than permission (EAFP)
look before you leap (LBYL)

ARQUITETURA DE 3 CAMADAS: interface, negócio, banco de dados

UI = Controller
BLL = Service
DAL = Model


To activate your venv on Windows, you need to run a script that gets installed by venv. If you created your venv in a directory called myenv, the command would be:
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1