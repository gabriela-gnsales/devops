from flask import Flask
from flask_caching import Cache
import random

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis', 
                            'CACHE_REDIS_URL': 'redis://localhost:6379/0'})

@app.route('/')
@cache.cached(timeout=10)

def route():
    data = str(random.randint(0, 1000)) + '\n'
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083)
