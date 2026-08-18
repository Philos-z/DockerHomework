from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return "Flask is working!"


@app.get("/api/hello")
def hello():
    return jsonify(message="Hello World")


if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8000, debug=True)
    app.run(host="127.0.0.1", port=8000, debug=True)