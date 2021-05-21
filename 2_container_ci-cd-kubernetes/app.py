from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world, this is the final demo of this presentation!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
