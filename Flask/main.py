from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return(f"Hello, BU: {1650705419}")

if __name__ == '__main__':
    app.run(debug=True)