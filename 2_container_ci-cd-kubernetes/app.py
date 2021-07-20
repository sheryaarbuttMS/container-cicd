from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello amazing crowd in the Spark conference, we are running this from a CD pipeline in GitHub Actions."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
