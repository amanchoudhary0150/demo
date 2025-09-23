from flask import Flask

app = Flask(__name__)

@app.route("/")
def imdex():
    return "Hello"

if __main__=="__main__":
    app.route(host="127.0.0.1",port=5000)
    
    