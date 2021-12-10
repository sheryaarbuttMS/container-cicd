from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello kubeclub. Weird stuff is happening in testing.!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
