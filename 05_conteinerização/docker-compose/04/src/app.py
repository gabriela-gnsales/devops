import os

from flask import Flask
from redis import Redis

app = Flask(__name__)
app.debug = True

redis_client = Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, db=2, decode_responses=True)

redis_chaves_nomes = os.getenv('REDIS_CHAVE_NOMES', 'nomes')

@app.route('/pessoa', methods=['GET'])
def get_from_redis():
    all_items = redis_client.smembers(redis_chaves_nomes)
    return 'Nomes no banco de dados: ' + ', '.join(sorted(all_items))

@app.route('/pessoa/<nome>', methods=['GET'])
def set_on_redis(nome: str):
    all_items = redis_client.smembers(redis_chaves_nomes)
    if nome in all_items:
        return "Nome já existe!!!"
    else:
        redis_client.sadd(redis_chaves_nomes, nome)
        return "Nome adicionado :)"