from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Atlanta Code camp! I'm so glad to be outside of the house again."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
