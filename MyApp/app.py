from flask import Flask, request
import joblib
app = Flask(__name__)

vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load('model.pkl')

@app.route("/")
def hello():
    return "Spam Detector"

@app.route("/predict", methods = ['POST'])
def predict():
    message = request.args.get('message')
    vect_message = vectorizer.transform([message])
    result  = model.predict(vect_message)[0]
    return result

if __name__=="__main__":
    app.run(port = 8080)