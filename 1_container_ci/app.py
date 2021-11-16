from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Uantwerpen! I'm so glad to be in Belgium again."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
