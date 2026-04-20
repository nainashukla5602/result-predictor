from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    hours = int(request.form["hours"])
    attendance = int(request.form["attendance"])
    marks = int(request.form["marks"])

    result = model.predict([[hours, attendance, marks]])[0]

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)