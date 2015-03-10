from flask import Flask, jsonify
from redis import Redis
app = Flask(__name__)
app.debug = True;
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/json')
def json():
    return jsonify(
            username="hello",
            email="hello@example.com",
            size=14)

@app.route('/hits')
def hits():
    redis.incr('hits')
    return 'This page has been hit %s times' % redis.get('hits')

@app.route('/reset')
def reset():
    redis.set('hits', 0)
    return 'Hits counter reset to {0}'.format(redis.get('hits'))


if __name__=='__main__':
    app.run()
