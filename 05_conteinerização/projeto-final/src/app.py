import os

from flask import Flask
import psycopg2 

app = Flask(__name__)
app.debug = True


dsn = 'dbname={dbname} user={user} password={password} host={host}'.format(
    dbname=os.getenv('PSQL_DBNAME'),
    user=os.getenv('PSQL_USER'),
    password=os.getenv('PSQL_PASSWORD'),
    host=os.getenv('PSQL_HOST'),
)
psql_connect = psycopg2.connect(dsn)


@app.route('/pessoa', methods=['GET'])
def get_from_redis():
    cur = psql_connect.cursor()
    cur.execute('SELECT * FROM nomes;')
    all_data = cur.fetchall()
    all_data_list = []    
    for item in all_data:
        all_data_list.append(item[0])
    cur.close()    
    return ', '.join(all_data_list)


@app.route('/pessoa/<nome>', methods=['GET'])
def set_on_redis(nome: str):
    cur = psql_connect.cursor()
    cur.execute("SELECT * FROM nomes WHERE nome = %s;", (nome.strip(), ))
    if cur.rowcount > 0: 
        return "Este nome já foi registrado anteriormente na base de dados."
    
    cur.execute('INSERT INTO nomes VALUES (%s)', (nome.strip(), ))
    psql_connect.commit()
    return "Nome registrado."

    cur.close()
