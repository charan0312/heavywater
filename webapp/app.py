import traceback, json
import pandas as pd
import numpy as np

from flask import Flask, request, jsonify, render_template
from keras.models import load_model
from sklearn.feature_extraction.text import TfidfVectorizer

# Your API definition
app = Flask(__name__)


@app.route('/')
def home():
    return "Hi Charan"

#@app.route('/about/')
#def about():
#    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    if loaded_model:
        try:
            json_ = request.json
            print(json_)
            query = pd.DataFrame(json_)
            

            
            
            labels = ['APPLICATION', 'BILL', 'BILL BINDER', 'BINDER', 'CANCELLATION NOTICE',
       'CHANGE ENDORSEMENT', 'DECLARATION', 'DELETION OF INTEREST',
       'EXPIRATION NOTICE', 'INTENT TO CANCEL NOTICE', 'NON-RENEWAL NOTICE',
       'POLICY CHANGE', 'REINSTATEMENT NOTICE', 'RETURNED CHECK']
            


            padded_1 = vectorizer.transform(query.values)

            pred_1 = loaded_model.predict(padded_1)
            

            return jsonify({'prediction': str(labels[np.argmax(pred_1)]) + str(max(pred_1[0]))})

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')
    
    
if __name__ == '__main__':
    try:
        port = int(sys.argv[1]) # This is for a command-line input
    except:
        port = 12345 # If you don't provide any port the port will be set to 12345

    #lr = joblib.load("model.pkl") # Load "model.pkl"
    loaded_model = load_model('nn_model.h5')
    print ('Model loaded')
    #model_columns = joblib.load("model_columns.pkl") # Load "model_columns.pkl"
    print ('Model columns loaded')

    app.run(port=port, debug=True)