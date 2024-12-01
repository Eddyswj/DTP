from flask import Flask, request, render_template, session
from flask_socketio import SocketIO
from Webapp.app.ML import run

app = Flask(__name__)
socketio = SocketIO(app)
# development key, replace with your own
app.secret_key = 'dtp'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/select", methods = ["POST"])
def select():
    if request.method == "POST":
        crops = request.form.getlist("crops[]")
        session['crops'] = crops
        return render_template("variables.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        temperature= float(request.form["temperature"])
        air_pollution = float(request.form["pollution"])
        pesticides = float(request.form["pest"])
        rainfall = float(request.form["rainfall"])
        crops = session.get('crops', [])

        bcrop = run(temperature, air_pollution, pesticides, rainfall, crops)
        
        if bcrop == []:
            statement = "No crops can be planted"
            image_file = "empty.jpg"
        else:
            statement = f"{bcrop} should be planted for most yield"
            image_file = f"{bcrop}.jpg"

        return render_template("crop prediction.html", prediction_text=statement, image_file=image_file)
    return render_template("crop prediction.html")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port= 8000)