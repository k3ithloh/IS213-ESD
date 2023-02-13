#write me a flask program
from flask import Flask
app = Flask(__name__)

@app.route("/hello")
@app.route("/")
# def hello():
#     return "Hello World!"

if __name__ == "_main_":
    app.run()