from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Making sure this demo still works."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
