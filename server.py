"""This is the main  file that control all aplication internal  flow"""
#Flask
from flask import Flask, jsonify
from configuration import Configuration
from flask_cors import CORS, cross_origin

#test torre
from utils import Utils

#more
import joblib




# Initializing app
app = Flask(__name__)
app.config.from_object(Configuration)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'torre_test'


# Routes
@app.route('/', methods=['GET'])
@cross_origin()
def init():
    return "Welcome to my test in torre"

@app.route('/predict/<id_job_offer>', methods=['GET'])
@cross_origin()
def predict(id_job_offer):
    if id_job_offer >= 50000:
        return f"We do not have a job offer with id {id_job_offer}"
    else:
        X_test = Utils.get_x_test(id_job_offer)
        prediction = model.predict(X_test.reshape(1,-1))
        prediction = list(prediction)
        return jsonify({'prediccion' : prediction[0]})



if __name__ == "__main__":
    model = joblib.load('./models/best_model.pkl')
    app.run()