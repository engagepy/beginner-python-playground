
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """ This is the beginning of a new age"""

@app.route("/zurl")
def hello2():
	return "this is just another story"
if __name__ == '__main__':
	app.run(debug=True, port=80)
