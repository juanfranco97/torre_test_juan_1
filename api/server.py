"""This is the main  file that control all aplication internal  flow"""
#Flask
from flask import Flask, make_response, jsonify, redirect, url_for
from ../configuration import Configuration
from flask_cors import CORS, cross_origin
from utils import Utils




# Initializing app
app = Flask(__name__)
app.config.from_object(Configuration)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'torre_test'


# Routes
@app.route('/', methods=['GET'])
@cross_origin()
def init():
    return "Welcome to We deal, this api is only available to We Deal developers"





if __name__ == "__main__":
    app.run()