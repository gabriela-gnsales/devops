import redis
import json

redis_cli = redis.Redis(host='localhost', port=6379)

product = {'id': 1, 'in_stock':True, 'name': 'bolacha', 'price': 3.5}

redis_cli.set('product', json.dumps(product))

redis_cli.get('product')