# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)
USERNAME = 'leexha'
PASSWORD = 'Password123_!'
PORT = '27017'
HOST = '54.255.141.174'

app.config['MONGO_DBNAME'] = 'DATA_DB'
app.config['MONGO_HOST'] = HOST
app.config['MONGO_PORT'] = PORT
app.config['MONGO_USERNAME'] = USERNAME
app.config['MONGO_PASSWORD'] = PASSWORD

mongo = PyMongo(app)

@app.route('/get_all', methods=['GET'])
def get_all_data():
  results = mongo.db.collection
  output = []
  for s in results.find():
    output.append({'title' : s['title'], 'URL' : s['URL']})
  return jsonify({'result' : output})


if __name__ == '__main__':
    app.run(debug=True)
