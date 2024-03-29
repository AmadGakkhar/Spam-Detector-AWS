from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World"

@app.route('/home', methods = ['POST'])
def home():
  message = request.args.get("message")
  return message + ' returned'


if __name__ == '__main__':
  app.run(port = 8080)

