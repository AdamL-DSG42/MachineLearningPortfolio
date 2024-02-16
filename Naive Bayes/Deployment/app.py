from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open('model.pkl','rb') as pickle_file:
    model = pickle.load(pickle_file)

with open('vectoriser.pkl','rb') as pickle_file:
    vectoriser = pickle.load(pickle_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']

    text_vectorised = vectoriser.transform([text])

    prediction = model.predict(text_vectorised)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)