#flask allows to write a python service which can serve http request
from flask import Flask,request,jsonify
import util
import json
app = Flask(__name__)

@app.route("/get_location_names")
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route("/predict_home_price",methods=["POST"])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])

    response = jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bath,bhk)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


#main function
if __name__ == "__main__":
    print("Starting Python Flask Server For House Pricing Prediction")
    util.load_saved_artifacts()
    app.run(host='0.0.0.0',port=8080)
