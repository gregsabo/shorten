import md5
import base64
import random

from flask import Flask
from flask import request, redirect
import redis
app = Flask(__name__)

# DB

redis_connection = redis.StrictRedis("localhost", 6379)

# TESTS

def test_lookup():
    random_url = "Test URL: %s" % random.random()
    code = create_code_for_url(random_url)
    assert random_url == get_url_for_code(code)

# LIB

def minihash(url):
    return base64.b64encode(md5.new(url).digest())[:6]

def create_code_for_url(url):
    #TODO: handle collisions
    code = minihash(url)
    redis_connection.set(code, url)
    return code

def get_url_for_code(code):
    return redis_connection.get(code)

# ROUTES

@app.route("/create")
def route_create():
    url = request.args.get('url')
    return create_code_for_url(url)

@app.route("/<path:path>")
def route_redirect(path):
    return redirect(get_url_for_code(path))
    
# STARTUP

if __name__ == "__main__":
    app.debug = True
    app.run()