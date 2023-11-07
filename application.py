import numpy as np
from flask import Flask, request, render_template
import pickle

application = Flask(__name__)  # Initialize the Flask App
model = pickle.load(open('5G_Quality.pkl', 'rb'))

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/pred')  # Use a unique endpoint name, e.g., '/pred'
def pred():
    return render_template('pred.html')

@application.route('/prediction', methods=['POST'])
def prediction():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('pred.html', prediction_text='Resource Allocation percentage is {}'.format(output))

if __name__ == "__main__":
    application.run(debug=True)
