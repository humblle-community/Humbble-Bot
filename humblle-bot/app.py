from flask import Flask
from flask_restful import Api

app = Flask(__name__, template_folder='templates')
api = Api(app)

@app.route('/')
def main():
    return {'message' : 'Hello'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)