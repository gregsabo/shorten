from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/create")
def route_create():
    url = request.args.get('url')
    return "Would make a shortcode for: %s" % url
    
if __name__ == "__main__":
    app.run()