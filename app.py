from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/predecir", methods=['POST'])
def predecir():
    Cuartos = int(request.form['Cuartos'])
    Distancia = int(request.form['Distancia'])
    prediction = model.predict([[Cuartos, Distancia]])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f'La casa con {Cuartos} cuartos y esta a una distancia  {Distancia} km tiene un valor de ${output}K')

if __name__ == "__main__":
     app.run()