
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Flask works!'

if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1')
