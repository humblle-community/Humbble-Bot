from flask import Flask, render_template, request
from flask_restful import Api
from extension.ext_database import db
from models.imageDB import ImageDB

app = Flask(__name__, template_folder='templates') 
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image', methods=['GET', 'POST'])
def up_image():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        return {'method': 'not found'}
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)