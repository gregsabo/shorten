import md5
import base64
import random
import json
from uuid import uuid4

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

def test_analytics():
    random_url = "Test URL: %s" % random.random()
    code = create_code_for_url(random_url)
    assert get_analytics_for_code(code)['hits'] == 0
    get_url_for_code(code, captureAnalytics=True)
    get_url_for_code(code, captureAnalytics=True)
    get_url_for_code(code, captureAnalytics=True)
    print get_analytics_for_code(code)
    assert get_analytics_for_code(code)['hits'] == 3

# LIB

def random_minicode():
    return base64.b64encode(uuid4().get_bytes())[:6]

def create_code_for_url(url):
    #TODO: handle collisions
    code = random_minicode()
    redis_connection.set(code, url)
    return code

def get_url_for_code(code, captureAnalytics=False):
    url = redis_connection.get(code)
    redis_connection.incr("CODE_HITS::%s" % code)
    return url

def get_analytics_for_code(code):
    hits = int(redis_connection.get("CODE_HITS::%s" % code) or 0)
    return dict(
        hits=hits
    )

# ROUTES

@app.route("/create")
def route_create():
    url = request.args.get('url')
    return create_code_for_url(url)

@app.route("/analytics/<path:path>")
def route_analytics(path):
    return json.dumps(
        get_analytics_for_code(path)
    )

@app.route("/<path:path>")
def route_redirect(path):
    return redirect(get_url_for_code(path, captureAnalytics=True))
    
# STARTUP

if __name__ == "__main__":
    app.debug = True
    app.run()