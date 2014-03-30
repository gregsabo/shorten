from flask import Flask
from flask import request
import md5
import base64
app = Flask(__name__)

def minihash(url):
    return base64.b64encode(md5.new(url).digest())[:6]

@app.route("/create")
def route_create():
    url = request.args.get('url')
    code = minihash(url)
    return "Would save shortcode: %s" % code
    
if __name__ == "__main__":
    app.run()